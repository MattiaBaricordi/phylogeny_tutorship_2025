#!/bin/bash

# mito_pipeline.sh

#

# This script downloads RefSeq mitogenomes for a set of species, extracts CDS regions

# (using a Python helper script), splits the 13 mitochondrial protein-coding genes

# (ND1, ND2, ND3, ND4, ND4L, ND5, ND6, COX1, COX2, COX3, ATP6, ATP8, CYTB) into separate folders,

# aligns each gene with MAFFT, and concatenates the aligned genes.

#

# FASTA files are named with the species name (spaces replaced by underscores)

# and organized by CDS/gene name.

#

# Species and Accession Numbers:

#   Branchiostoma floridae      [NC_000834.1]

#   Protopterus annectens        [NC_018822.1]

#   Lepidosiren paradoxa         [NC_003342.1]

#   Pyxicephalus adspersus       [NC_044480.1]

#   Ambystoma mexicanum          [NC_005797.1]

#   Rhinatrema bivittatum        [NC_006303.1]

#   Abronia graminea             [NC_005958.1]

#   Pogona vitticeps             [NC_006922.1]

#   Python regius                [NC_007399.1]

#   Uroplatus ebenaui            [NC_025783.1]

#   Sphenodon punctatus          [NC_004815.1]

#   Crocodylus niloticus         [NC_008142.1]

#   Crocodylus porosus           [NC_008143.1]

#   Falco peregrinus             [NC_000878.1]

#   Dinornis giganteus           [NC_002672.1]

#   Sarcophilus harrisii         [NC_018788.1]

#   Ursus arctos                 [NC_003427.1]

#   Vulpes vulpes                [NC_008434.1]

#   Pongo abelii                 [NC_002083.1]

#   Asterias amurensis           [NC_006665.1]

#   Epiperipatus biolleyi        [NC_009082.1]


#########################################

# Step 0: Environment and Tools Check

#########################################


# (Assumes mamba is already installed.)

if ! command -v mamba &> /dev/null; then

    echo "Mamba not found. Please install mamba first."

    exit 1

fi


ENV_NAME="mitogenome_env"

# Create environment if needed, including biopython now.

if ! mamba env list | grep -q "^$ENV_NAME\s"; then

    echo "Creating mamba environment '$ENV_NAME' with entrez-direct, seqkit, mafft, and biopython..."

    mamba create -y -n $ENV_NAME -c bioconda entrez-direct seqkit mafft biopython

else

    echo "Mamba environment '$ENV_NAME' already exists."

fi


# Activate environment.

source "$(mamba info --base)/etc/profile.d/conda.sh"

mamba activate $ENV_NAME


# Verify required commands.

for cmd in efetch seqkit mafft python3; do

    if ! command -v $cmd &> /dev/null; then

         echo "$cmd is not installed. Please check your environment."

         exit 1

    else

         echo "$cmd is installed."

    fi

done


#########################################

# Create Python helper: extract_cds.py

#########################################


if [ ! -f extract_cds.py ]; then

    cat << 'EOF' > extract_cds.py

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

EOF

    chmod +x extract_cds.py

fi


#########################################

# Step 1: Define species & Download Mitogenomes

#########################################


# Map accession numbers to species names (use names as you wish; must match your desired header)

declare -A species_map=(

  ["NC_000834.1"]="Branchiostoma_floridae"

  ["NC_018822.1"]="Protopterus_annectens"

  ["NC_003342.1"]="Lepidosiren_paradoxa"

  ["NC_044480.1"]="Pyxicephalus_adspersus"

  ["NC_005797.1"]="Ambystoma_mexicanum"

  ["NC_006303.1"]="Rhinatrema_bivittatum"

  ["NC_005958.1"]="Abronia_graminea"

  ["NC_006922.1"]="Pogona_vitticeps"

  ["NC_007399.1"]="Python_regius"

  ["NC_025783.1"]="Uroplatus_ebenaui"

  ["NC_004815.1"]="Sphenodon_punctatus"

  ["NC_008142.1"]="Crocodylus_niloticus"

  ["NC_008143.1"]="Crocodylus_porosus"

  ["NC_000878.1"]="Falco_peregrinus"

  ["NC_002672.1"]="Dinornis_giganteus"

  ["NC_018788.1"]="Sarcophilus_harrisii"

  ["NC_003427.1"]="Ursus_arctos"

  ["NC_008434.1"]="Vulpes_vulpes"

  ["NC_002083.1"]="Pongo_abelii"

  ["NC_006665.1"]="Asterias_amurensis"

  ["NC_009082.1"]="Epiperipatus_biolleyi"

)


ACCESSIONS=("NC_000834.1" "NC_018822.1" "NC_003342.1" "NC_044480.1" "NC_005797.1" "NC_006303.1" "NC_005958.1" "NC_006922.1" "NC_007399.1" "NC_025783.1" "NC_004815.1" "NC_008142.1" "NC_008143.1" "NC_000878.1" "NC_002672.1" "NC_018788.1" "NC_003427.1" "NC_008434.1" "NC_002083.1" "NC_006665.1" "NC_009082.1")


# Create directories.

mkdir -p genomes genes alignments concatenated


echo "Downloading mitogenomes from NCBI..."

for acc in "${ACCESSIONS[@]}"; do

    species=${species_map[$acc]}

    echo "Downloading $acc ($species)..."

    efetch -db nucleotide -format fasta -id "$acc" > genomes/${species}.fasta

done


#########################################

# Step 2: Extract CDS from GenBank files

#########################################


echo "Extracting CDS (coding regions) from GenBank annotations..."

for acc in "${ACCESSIONS[@]}"; do

    species=${species_map[$acc]}

    echo "Processing $acc ($species)..."

    # Download GenBank file.

    efetch -db nucleotide -format gb -id "$acc" > genomes/${species}.gb

    # Use Python helper to extract CDS features.

    python3 extract_cds.py genomes/${species}.gb genes/${species}_CDS.fasta ${species}

done


#########################################

# Step 3: Organize individual genes by CDS name

#########################################


# List of 13 mitochondrial coding genes.

GENES=("ND1" "ND2" "ND3" "ND4" "ND4L" "ND5" "ND6" "COX1" "COX2" "COX3" "ATP6" "ATP8" "CYTB")


echo "Separating individual genes into folders..."

for gene in "${GENES[@]}"; do

    mkdir -p genes/${gene}

    for fasta in genes/*_CDS.fasta; do

        species=$(basename "${fasta}" _CDS.fasta)

        # Extract entries whose header contains the gene name (case insensitive),

        # and write to a file named: species_gene.fasta.

        seqkit grep -nirp "$gene" "$fasta" | \

            seqkit replace -p ".+" -r "${species}" > genes/${gene}/${species}_${gene}.fasta

    done

    # Concatenate all species sequences for this gene.

    cat genes/${gene}/*.fasta > genes/${gene}.fasta

done


#########################################

# Step 4: Align each gene using MAFFT

#########################################


echo "Aligning each gene using MAFFT..."

for gene in "${GENES[@]}"; do

    echo "Aligning $gene..."

    mafft --auto genes/${gene}.fasta > alignments/${gene}_aligned.fasta

done


#########################################

# Step 5: Concatenate all aligned genes

#########################################


echo "Concatenating all aligned genes..."

# Use the first gene alignment file to set species order.

seqkit seq -n alignments/${GENES[0]}_aligned.fasta > concatenated/species_order.txt


# Initialize concatenated alignment file.

> concatenated/concatenated_alignment.fasta


# For each species in the defined order, concatenate its aligned gene sequences.

while read species; do

    echo ">${species}" >> concatenated/concatenated_alignment.fasta

    full_seq=""

    for gene in "${GENES[@]}"; do

        gene_seq=$(seqkit grep -p "^${species}$" alignments/${gene}_aligned.fasta | seqkit seq -s | tr -d '\n')

        full_seq+="${gene_seq}"

    done

    echo "$full_seq" >> concatenated/concatenated_alignment.fasta

done < concatenated/species_order.txt


echo "Pipeline finished successfully."

