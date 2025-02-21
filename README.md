# phylogeny_tutorship_2025
# Phylogeny Class Tutorial: Managing Sequences, Alignments, and IQ-TREE in Bash

## Introduction to the Command Line
The command line (or terminal) allows users to interact with the computer using text-based commands. This is essential for bioinformatics tasks like sequence alignment and phylogenetic analysis.

### Why Use the Command Line?
- Automates repetitive tasks
- Handles large datasets efficiently
- Runs bioinformatics tools that lack graphical interfaces

### Basic Commands

#### Important Note on Special Characters in Sequence Names
Not all special characters are allowed in sequence names, because they may interfere with the structure encoding in the Newick tree files. To avoid problems with downstream software (like tree viewers), IQ-TREE (and also other phylogenetic software) checks the names for such potentially interfering characters and substitutes them by underscores `_`. Permitted characters in sequence names are alphanumeric letters, underscores `_`, dash `-`, dot `.`, slash `/` and vertical bar `|`. All other characters are substituted, like e.g. `hawk's-eye` is converted to `hawk_s-eye` as which it will appear in the tree.

Please note, this can lead to duplicate names if you, for instance, already have two sequences named `hawk_s-eye` and `hawk's-eye`. In such cases, you will obtain an error and need to adjust the names in the original input alignment.

- **`rm -r directory_name`**: Remove a directory and its contents (use with caution)
  - Example: `rm -r old_project`
- **`pwd`**: Print the current working directory
- **`ls`**: List files in the current directory
  - Use `ls -l` for detailed information
  - Use `ls -a` to show hidden files
- **`cd directory_name`**: Change to a specific directory
  - Example: `cd Documents`
- **`mkdir folder_name`**: Create a new directory
  - Example: `mkdir new_project`
- **`cp file1 file2`**: Copy a file
  - Example: `cp original.fasta backup.fasta`
- **`mv file1 file2`**: Move or rename a file
  - Example: `mv data.fasta sequences.fasta`
- **`rm file`**: Remove a file (use with caution)
  - Example: `rm old_sequences.fasta`
- **`nano file`**: Open a file in a simple text editor
  - Example: `nano sequences.fasta`
- **Using Wildcards (`*`) in File Operations**
  - List all FASTA files in a directory:
    ```bash
    ls *.fasta
    ```
  - Copy all FASTA files to another directory:
    ```bash
    cp *.fasta backup/
    ```
  - Remove all FASTA files in a directory (use with caution):
    ```bash
    rm *.fasta
    ```
  - Create a multi-FASTA file by concatenating multiple FASTA files:
    ```bash
    cat *.fasta > combined_sequences.fasta
    ```

### Advanced Text Processing Commands
- **`grep`**: Search for patterns in a file
  - Example: `grep '^>' sequences.fasta` (Find sequence headers in a FASTA file)
- **`sed`**: Stream editor for modifying files
  - Example: `sed 's/old/new/g' file.txt > newfile.txt` (Replace 'old' with 'new' in a file)
- **`awk`**: Process and analyze text-based data
  - Example: `awk '/^>/ {print $0}' sequences.fasta` (Print only the sequence headers)

### Navigating Folders and Subfolders
Consider the following directory structure:
```
/home/user/project/
├── data/
│   ├── sequences.fasta
│   ├── alignment.fasta
├── scripts/
│   ├── analysis.sh
├── results/
│   ├── tree.nwk
```
To navigate through this structure:
- Move into the `project` directory:
  ```bash
  cd /home/user/project/
  ```
- List contents:
  ```bash
  ls
  ```
- Move into the `data` subdirectory:
  ```bash
  cd data
  ```
- Move back to the parent directory:
  ```bash
  cd ..
  ```
- Move into the `scripts` subdirectory and run a script:
  ```bash
  cd scripts
  bash analysis.sh
  ```
- Move back to home from any location:
  ```bash
  cd ~
  ```

### Introduction to Bash Scripts
A Bash script is a file containing a sequence of commands that automate tasks.

#### Structure of a Bash Script
```bash
#!/bin/bash
# This is a comment

echo "Starting analysis..."
cd /home/user/project/data
iqtree -s alignment.fasta -m MFP -bb 1000 -alrt 1000
echo "Analysis complete!"
```
#### Running a Bash Script
```bash
bash script.sh
```

## Using IQ-TREE for Phylogenetic Analysis

### Example of a Maximum-Likelihood Tree Output
At the end of the run, IQ-TREE generates an ML tree that may look like this:
```
![Untitled design (1)](https://github.com/user-attachments/assets/b78b07e8-ec30-46af-9196-0a2016fda60c)

```
This tree makes sense as mammals (Human to Opossum) form a clade, while reptiles (Turtle to Crocodile) and birds form a sister clade. IQ-TREE produces an unrooted tree by default, simply ordering the taxa as they appear in the alignment.

### Running a Basic Maximum-Likelihood Analysis
```bash
iqtree -s example.phy
```
This command reconstructs a maximum-likelihood tree from the provided alignment file. At the end of the run, IQ-TREE generates several output files:
- **example.phy.iqtree**: The main report file with computational results and a textual tree representation.
- **example.phy.treefile**: The ML tree in NEWICK format, viewable with FigTree or iTOL.
- **example.phy.log**: A log file of the run, useful for debugging.

### Resuming Interrupted Runs
If a run is interrupted, IQ-TREE saves a checkpoint file (e.g., `example.phy.ckp.gz`). To resume the run:
```bash
iqtree -s example.phy
```
If the run was successful and you re-run the command, IQ-TREE will return an error message. To force a re-run:
```bash
iqtree -s example.phy -redo
```

### Specifying an Output Prefix
To prevent overwriting files when performing multiple analyses on the same alignment:
```bash
iqtree -s example.phy --prefix myprefix
```

### Choosing the Right Substitution Model
To automatically select the best substitution model:
```bash
iqtree -s example.phy -m MFP
```
For a more computationally thorough analysis:
```bash
iqtree -s example.phy -m MF -mtree
```
