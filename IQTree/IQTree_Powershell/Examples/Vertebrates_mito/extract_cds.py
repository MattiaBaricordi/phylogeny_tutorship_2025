
#!/usr/bin/env python3

import sys

from Bio import SeqIO


if len(sys.argv) < 3:

    print("Usage: extract_cds.py input.gb output.fasta [override_species]")

    sys.exit(1)


input_file = sys.argv[1]

output_file = sys.argv[2]

override = None

if len(sys.argv) >= 4:

    override = sys.argv[3]


records = list(SeqIO.parse(input_file, "genbank"))

with open(output_file, "w") as out_f:

    for record in records:

        if override:

            species = override

        else:

            species = record.annotations.get("organism", record.id).replace(" ", "_")

        for feature in record.features:

            if feature.type == "CDS":

                gene = feature.qualifiers.get("gene", ["unknown"])[0]

                seq = feature.extract(record.seq)

                out_f.write(">%s_%s\n%s\n" % (species, gene, seq))

