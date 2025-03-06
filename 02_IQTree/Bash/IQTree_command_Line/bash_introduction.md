# Phylogeny Survival 101 using the bash commandline
Managing Sequences, Alignments, and IQ-TREE in Bash

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
# Bash Screen Functioning Manual

## Introduction to GNU Screen
Create, manage, and navigate multiple terminal sessions within a single window.   
It is especially useful for managing long-running processes, preventing SSH session disconnections, and multitasking efficiently in the command line.   
A.K.A. The way to run your processes and log out from your PC

## Basic Screen Commands
### Starting a New Screen Session
```bash
screen -S my_session
```

### Detaching from a Screen Session
To detach from a screen session without terminating it:
- Press **`Ctrl + A`**, then **`D`**
- This will leave the session running in the background.

### Listing Active Screen Sessions
To view all running screen sessions:
```bash
screen -ls
```
Example output:
```
There are screens on:
    1234.my_session (Detached)
    5678.another_session (Detached)
```

### Reattaching to a Screen Session
To resume a previously detached session:
```bash
screen -r my_session
```
Or, if there’s only one session:
```bash
screen -r
```
If multiple sessions are running, you must specify the session name or ID.

### Killing a Screen Session
To terminate a screen session:
1. Reattach to the session: `screen -r my_session`
2. Exit normally by typing:
   ```bash
   exit
   ```
3. Alternatively, inside the screen, press **`Ctrl + A`**, then **`K`**, and confirm with `Y`.

### Force Killing a Screen Session
To forcibly remove a screen session:
```bash
screen -X -S my_session quit
```

## Navigating and Managing Multiple Windows in a Screen Session
Once inside a screen session, you can create and navigate between multiple windows.

### Creating a New Window
Inside a screen session, press:
- **`Ctrl + A`**, then **`C`** → Creates a new window.

### Switching Between Windows
- **`Ctrl + A`**, then **`N`** → Switch to the next window.
- **`Ctrl + A`**, then **`P`** → Switch to the previous window.
- **`Ctrl + A`**, then **`0-9`** → Jump to a specific window by its number.

### Scrolling Inside Screen
To scroll inside a screen session:
- **`Ctrl + A`**, then **`Esc`** → Enter copy mode.
- Use **Arrow Keys** or **Page Up/Page Down** to scroll. !!No mouse wheel!!
- Press **`Q`** to exit copy mode.

## Exiting and Cleaning Up
### Exiting a Screen Session
To exit and terminate a screen session:
```bash
exit
```
Or, use **`Ctrl + D`**.

For more resources: https://github.com/filonico/UNIX_and_bash_basics/tree/main

