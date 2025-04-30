#!/usr/bin/env python3
"""
term_script_cds_rRNA.py

Fetch each mito genome with full parts, extract only CDS + 12S/16S rRNAs,
split per species and aggregate per gene across all species.

If the RefSeq entry lacks rRNA features, we detect the “identical to”
GenBank accession from the COMMENT and fetch that to harvest 12S & 16S.
We also clear out any old s_rRNA/l_rRNA FASTAs before aggregating.
"""

import os
import re
import shutil
from collections import defaultdict
from Bio import Entrez, SeqIO
from Bio.SeqRecord import SeqRecord

# — USER SETTINGS —
Entrez.email = "your.email@example.com"
# Entrez.api_key = "YOUR_NCBI_API_KEY"  # optional

DIR_SPLIT = "genes_by_species"
DIR_AGG   = "genes_by_all_species"

# ensure clean aggregate directory
if os.path.isdir(DIR_AGG):
    for fn in os.listdir(DIR_AGG):
        if fn.endswith(".fasta") and fn in ("s_rRNA.fasta","l_rRNA.fasta"):
            os.remove(os.path.join(DIR_AGG, fn))
else:
    os.makedirs(DIR_AGG)

os.makedirs(DIR_SPLIT, exist_ok=True)

# List of (species_name, accession)                                                                                                                           
SPECIES = [                                                                                                                                                   
    ("Reticulitermes_flavipes",    "NC_009498.1"),                                                                                                            
    ("Reticulitermes_santonensis", "NC_009499.1"),                                                                                                            
    ("Reticulitermes_virginicus",  "NC_009500.1"),                                                                                                            
    ("Reticulitermes_hageni",      "NC_009501.1"),                                                                                                            
    ("Reticulitermes_chinensis",   "NC_025567.1"),                                                                                                            
    ("Reticulitermes_aculabialis", "NC_026695.1"),                                                                                                            
    ("Reticulitermes_grassei",     "NC_030035.1"),                                                                                                            
    ("Reticulitermes_nelsonae",    "NC_030036.1"),                                                                                                            
    ("Reticulitermes_labralis",    "NC_030262.1"),                                                                                                            
    ("Reticulitermes_flaviceps",   "NC_031162.1"),                                                                                                            
    ("Reticulitermes_leptomandibularis","NC_042419.1"),                                                                                                       
    ("Reticulitermes_tibialis",    "NC_045231.1"),                                                                                                            
    ("Reticulitermes_lucifugus",   "NC_045240.1"),                                                                                                            
    ("Reticulitermes_ovatilabrum","NC_053728.1"),                                                                                                             
    ("Reticulitermes_affinis",     "NC_062660.1"),                                                                                                            
    ("Reticulitermes_citrinus",    "NC_062661.1"),                                                                                                            
    ("Reticulitermes_dabieshanensis","NC_062662.1"),                                                                                                          
    ("Reticulitermes_luofunicus",  "NC_062663.1"),                                                                                                            
    ("Reticulitermes_parvus",      "NC_062664.1"),                                                                                                            
    ("Coptotermes_formosanus",     "NC_015800.1"),                                                                                                            
    ("Coptotermes_lacteus",        "NC_018125.1"),                                                                                                            
    ("Coptotermes_testaceus",      "NC_028722.1"),                                                                                                            
    ("Coptotermes_amanii",         "NC_030011.1"),                                                                                                            
    ("Coptotermes_elisae",         "NC_030012.1"),                                                                                                            
    ("Coptotermes_frenchi",        "NC_030013.1"),                                                                                                            
    ("Coptotermes_gestroi",        "NC_030014.1"),                                                                                                            
    ("Coptotermes_heimii",         "NC_030015.1"),                                                                                                            
    ("Coptotermes_kalshoveni",     "NC_030016.1"),                                                                                                            
    ("Coptotermes_michaelseni",    "NC_030017.1"),                                                                                                            
    ("Coptotermes_remotus",        "NC_030018.1"),                                                                                                            
    ("Coptotermes_sepangensis",    "NC_030019.1"),                                                                                                            
    ("Coptotermes_sjoestedti",     "NC_030020.1"),                                                                                                            
    ("Coptotermes_travians",       "NC_030021.1"),                                                                                                            
    ("Coptotermes_suzhouensis",    "NC_037018.1"),                                                                                                            
] 

def sanitize(x):
    return re.sub(r'\W+', '_', x)

def canonical_rRNA(raw: str) -> str:
    """
    Collapse any small‐subunit synonyms → 12S_rRNA
                any large‐subunit synonyms → 16S_rRNA
    """
    r = (raw or "").lower()
    if ("12s" in r
        or "small subunit" in r
        or "ssu" in r
        or "rrns" in r):
        return "12S_rRNA"
    if ("16s" in r
        or "large subunit" in r
        or "lsu" in r
        or "rrnl" in r):
        return "16S_rRNA"
    # fallback
    return sanitize(raw or "rRNA")

def fetch_record(acc: str):
    """Get GenBank with parts so we see 'gene' features."""
    with Entrez.efetch(db="nucleotide", id=acc,
                       rettype="gbwithparts", retmode="text") as h:
        return SeqIO.read(h, "genbank")

def find_alt_acc(comment: str) -> str:
    """Extract the 'identical to XXXXX' GenBank ID from the COMMENT."""
    m = re.search(r"identical to\s+([A-Z0-9_]+)", comment, re.IGNORECASE)
    return m.group(1) if m else None

def ensure_rRNAs(gmap: dict, rec):
    """If 12S or 16S still missing, fetch from the alt accession in COMMENT."""
    have12 = "12S_rRNA" in gmap
    have16 = "16S_rRNA" in gmap
    if have12 and have16:
        return

    alt = find_alt_acc(rec.annotations.get("comment",""))
    if not alt:
        return

    alt_rec = fetch_record(alt)
    for f in alt_rec.features:
        if f.type == "rRNA":
            raw = f.qualifiers.get("product",[""])[0] or f.qualifiers.get("gene",[""])[0]
            name = canonical_rRNA(raw)
            if (name=="12S_rRNA" and not have12) or (name=="16S_rRNA" and not have16):
                gmap[name] = f

def split_cds_rRNA(rec, outdir):
    """
    Extract 13 CDS + both rRNAs:
      1) protein genes via 'gene' features (skip trn*/rrn*)
      2) any stray CDS
      3) any rRNA
      4) fallback via COMMENT‐linked record
    Write per‐species FASTAs, return {gene_name: path}.
    """
    os.makedirs(outdir, exist_ok=True)
    feats = rec.features
    gmap  = {}

    # 1) all protein-coding genes
    for f in feats:
        if f.type=="gene" and "gene" in f.qualifiers:
            raw = f.qualifiers["gene"][0]
            if raw.lower().startswith("trn") or re.match(r"rrn[SL]", raw, re.I):
                continue
            gmap[sanitize(raw)] = f

    # 2) fallback: any CDS lacking a gene parent
    for f in feats:
        if f.type=="CDS":
            raw = f.qualifiers.get("gene",[""])[0] or f.qualifiers.get("product",[""])[0]
            nm  = sanitize(raw or "CDS")
            if nm not in gmap:
                gmap[nm] = f

    # 3) harvest rRNAs if present
    for f in feats:
        if f.type=="rRNA":
            raw = f.qualifiers.get("product",[""])[0] or f.qualifiers.get("gene",[""])[0]
            gmap[canonical_rRNA(raw)] = f

    # 4) if still missing 12S/16S, pull from COMMENT‐linked record
    ensure_rRNAs(gmap, rec)

    # 5) write out in genome order
    out = {}
    for nm, f in sorted(gmap.items(), key=lambda kv: int(kv[1].location.start)):
        seq   = f.extract(rec.seq)
        rec_o = SeqRecord(seq,
                          id=rec.annotations["accessions"][0],
                          description="")
        fp    = os.path.join(outdir, f"{nm}.fasta")
        SeqIO.write(rec_o, fp, "fasta")
        out[nm] = fp

    return out

def aggregate(all_maps):
    inv = defaultdict(list)
    for sp, mp in all_maps.items():
        for nm, fp in mp.items():
            inv[nm].append((sp, fp))

    for nm, lst in inv.items():
        recs = []
        for sp, fp in sorted(lst):
            r = SeqIO.read(fp, "fasta")
            r.id          = sp
            r.description = ""
            recs.append(r)
        out_fp = os.path.join(DIR_AGG, f"{nm}.fasta")
        SeqIO.write(recs, out_fp, "fasta")
        print(f"Wrote {len(recs)} records to {out_fp}")

def main():
    all_maps = {}
    for sp, acc in SPECIES:
        print(f"[{sp}] fetching {acc}…", end="", flush=True)
        rec = fetch_record(acc)
        od  = os.path.join(DIR_SPLIT, sp)
        mp  = split_cds_rRNA(rec, od)
        print(f" {len(mp)} genes → {od}")
        all_maps[sp] = mp

    print("\nAggregating per gene across all species:")
    aggregate(all_maps)
    print("Done.")

if __name__=="__main__":
    main()

