# AliView Tutorial

## Introduction
AliView is an alignment viewer and editor. It supports various sequence formats and offers multiple alignment, editing, and visualization features.

### Key Features:
- Supports **FASTA, Nexus, Phylip, Clustal, and MSF** formats
- Allows **manual and automatic alignment** (MUSCLE, MAFFT, or external aligners)
- **On-the-fly nucleotide translation** to amino acids
- **Degenerate primer finder** for conserved regions
- **Visual cues** for consensus and deviations
- **Easy file and sequence management** (copy, paste, drop, remove)
- **External tool integration** (e.g., FastTree, FigTree)

## Getting Started
### Opening an Alignment File
1. Launch AliView.
2. Click **File > Open** or drag and drop a sequence file into the application.
3. Select your alignment file format (FASTA, Nexus, etc.).

### Navigating the Interface
- **Main Window**: Displays the sequence alignment.
- **Toolbar**: Provides quick access to common actions (alignment, editing, etc.).
- **Status Bar**: Displays alignment details such as sequence length and format.

## Editing Sequences
### Manual Editing
- Click on a sequence to edit individual nucleotides or amino acids.
- Use **Ctrl + Z** (Windows/Linux) or **Cmd + Z** (macOS) to undo changes.
- Copy/paste sequences using standard shortcuts.

### Automatic Alignment
1. Use **Ctrl+A** (Windows/Linux) or **Cmd + A** (macOS) to select all sequeces 
2. Go to **Align > Align with MUSCLE or MAFFT**.
3. Choose an alignment method.
4. Adjust parameters as needed and run the alignment.

### Translating Nucleotides to Amino Acids
1. Select a sequence or alignment region.
2. Click **Tools > Translate Nucleotides**.
3. Choose a reading frame.

### Exporting Alignments
- Go to **File > Save As** and select the desired format.
- Export edited alignments for further analysis.

## External Tool Integration
1. Set up external programs in **Settings > External Programs**.
2. Send alignments to tools like **FastTree** or **FigTree** for phylogenetic analysis.
3. Results will be automatically opened in the corresponding application.

#### **Official Documentation**: [AliView Help](http://www.ormbunkar.se/aliview/#TOP_HELP)
#### **Webpage**: [AliView Homepage](www.ormbunkar.se/aliview)


