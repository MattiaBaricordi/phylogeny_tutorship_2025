# IQ-TREE Installation and PowerShell Basics Tutorial

This document provides a step-by-step guide on installing and running IQ-TREE using Conda on Windows with PowerShell, along with a brief introduction to some basic PowerShell concepts. It is designed for users who are new to PowerShell and phylogenetic analysis using IQ-TREE.

---

## Table of Contents

1. [PowerShell Basics](#powershell-basics)
2. [Installing IQ-TREE Using Conda on Windows (PowerShell)](#installing-iq-tree-using-conda-on-windows-powershell)
   - [Understanding Conda Environments](#understanding-conda-environments)
   - [Using IQ-TREE for Phylogenetic Analysis](#using-iq-tree-for-phylogenetic-analysis)
   - [Running a Basic Maximum-Likelihood Analysis](#running-a-basic-maximum-likelihood-analysis)
   - [Resuming Interrupted Runs](#resuming-interrupted-runs)
   - [Specifying an Output Prefix](#specifying-an-output-prefix)
   - [Choosing the Right Substitution Model](#choosing-the-right-substitution-model)
   - [Using Codon Models](#using-codon-models)
   - [Bootstrap Trees](#bootstrap-trees)
   - [Partitioned Analysis for Multi-Gene Alignments](#partitioned-analysis-for-multi-gene-alignments)
   - [Conda Installation and IQ-TREE Setup](#conda-installation-and-iq-tree-setup)

---

## PowerShell Basics

**What is PowerShell?**  
PowerShell is a powerful command-line shell and scripting language built on the .NET framework. It is used for task automation and configuration management and is especially popular for system administration on Windows.

**Key Features:**
- **Command-Line Interface (CLI):** Run commands interactively.
- **Scripting:** Automate tasks with scripts saved as `.ps1` files.
- **Cmdlets:** Specialized commands that perform specific functions (e.g., `Get-Help`, `Get-Command`).
- **Pipelines:** Pass output from one cmdlet to another.

**Basic Commands:**

- **Get-Help:** Provides detailed help information on cmdlets and functions.
  ```powershell
  Get-Help Get-Process
  ```
Get-Command: Lists all available cmdlets and functions.
```powershell
Get-Command
```
Set-ExecutionPolicy: Sets the user’s ability to run scripts.
```powershell
Set-ExecutionPolicy RemoteSigned
```
Get-ChildItem: Lists the files and folders in the current directory (similar to ls or dir)
```
Get-ChildItem
```
change directory (Set-Location): Changes the current directory
```powershell
cd C:\Path\To\Directory
```
Tips for Beginners:

Use `Tab` for auto-completion of `cmdlet` names and paths.
Remember that PowerShell is case-insensitive.
Learn about pipelines to combine cmdlets effectively, e.g., `Get-Process | Where-Object {$_.CPU -gt 100}`.

## Installing IQ-TREE Using Conda on Windows (PowerShell)
# Conda and IQ-TREE Installation on Windows (PowerShell)

This guide provides a step-by-step process for installing Conda and IQ-TREE using PowerShell on Windows. It also includes verification steps to ensure everything is set up correctly.

---

## CONDA in PowerShell

## Installing Miniconda

Miniconda is a minimal installer for Conda, useful if you don’t need the full Anaconda package.

1. **Download Miniconda:**

   Go to the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html) and download the Windows installer for Python 3.x (64-bit).

2. **Install Miniconda:**

   Run the downloaded installer:
   - Choose "Add Miniconda to my PATH environment variable" (optional but recommended).
   - Select “Register Miniconda as my default Python 3.9” (recommended).

3. **Open PowerShell:**

   Press `Win + X` > **Windows PowerShell**.

4. **Verify the Installation:**

   ```powershell
   conda --version
   ```
5. Setting Up Conda for PowerShell
Run the following command to configure Conda for PowerShell:
```powershell
conda init powershell
```
Restart PowerShell to apply changes.

Check if Conda is working properly:
```powershell
conda info
```
6. Creating a Conda Environment for IQ-TREE
Create a new environment:
```powershell
conda create -n iqtree_env python=3.11
```
Replace 3.11 with the version of Python you prefer.   

7. Activate the environment:
```powershell
conda activate iqtree_env
```
8. Verify the environment:
```powershell
conda env list
```
You should see an asterisk (*) next to iqtree_env, this indicates you are in the iqtree environment.

9. Installing IQ-TREE
Install IQ-TREE via Bioconda:
First, add the Bioconda and Conda-Forge channels:
```powershell
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge

conda install iqtree
```
Confirm the installation when prompted (y).

Verifying the Installation
Check IQ-TREE version:

```powershell
iqtree -version
```
You should see a version number and license information.

Run a test command:
```powershell
iqtree -h
```
This should display the help information for IQ-TREE.
### Understanding Conda Environments
Conda environments are isolated spaces that let you install specific software and dependencies without affecting the system’s default packages. They help you work on multiple projects with different requirements seamlessly.

Before you proceed, ensure that Conda is configured to work with PowerShell. If not, initialize it by running:
`conda init powershell` Then, restart PowerShell to apply the changes.

## Using IQ-TREE for Phylogenetic Analysis
IQ-TREE is a software tool used for phylogenomic inference. It applies a stochastic algorithm to infer phylogenetic trees by Maximum Likelihood. By default, IQ-TREE produces an unrooted tree that lists taxa in the order they appear in the alignment.
-> IQTree Manual available at http://www.iqtree.org/doc/iqtree-doc.pdf  
-> WebServer available at http://iqtree.cibiv.univie.ac.at/  
### Example of a Maximum-Likelihood Tree Output
At the end of the run, IQ-TREE generates an ML tree that may look like this:  

![Untitled design (1)](https://github.com/user-attachments/assets/b78b07e8-ec30-46af-9196-0a2016fda60c)
This tree makes sense as mammals (Human to Opossum) form a clade, while reptiles (Turtle to Crocodile) and birds form a sister clade. 

### Running a Basic Maximum-Likelihood Analysis
```powershell
iqtree -s example.phy
```
This command reconstructs a maximum-likelihood tree from the provided alignment file. At the end of the run, IQ-TREE generates several output files:  
- **example.phy.iqtree**: The main report file with computational results and a textual tree representation.  
- **example.phy.treefile**: The ML tree in NEWICK format, viewable with FigTree or iTOL.  
- **example.phy.log**: A log file of the run, useful for debugging.  

### Resuming Interrupted Runs
IQ-TREE periodically writes a checkpoint file example.phy.ckp.gz (gzip-compressed to save space). This checkpoint file is used to resume an interrupted run, which is handy if you have a very large data sets or time limit (i.e. changing terminal or while working on a cluster with a queue system).   
If the run did not finish, invoking IQ-TREE again with the very same command line will recover the analysis from the last stopped point  

If the run successfully completed, running again will issue an error message:
```
ERROR: Checkpoint (example.phy.ckp.gz) indicates that a previous
run successfully finished
```
Use `-redo` option if you really want to redo the analysis and overwrite all output files. This prevents lost of data if you accidentally re-run IQ-TREE.   
However, if you want to re-run the analysis and overwrite all previous output files, use -redo option:   
```powershell
iqtree -s example.phy -redo
```
Finally, the default prefix of all output files is the alignment file name. You can
change the prefix with:
```powershell
iqtree -s example.phy --prefix myprefix
# for version 1.x change --prefix to -pre
This prevents output files being overwritten when you perform multiple analyses on
the same alignment within the same folder.
```
If a run is interrupted, IQ-TREE saves a checkpoint file (e.g., `example.phy.ckp.gz`). To resume the run:
```powershell
iqtree -s example.phy
```

### Specifying an Output Prefix
To prevent overwriting files when performing multiple analyses on the same alignment:
```powershell
iqtree -s example.phy --prefix myprefix
```

### Choosing the Right Substitution Model
**ModelFinder** to determine the best-fit model:
```powershell
iqtree -s example.phy -m MFP
# change -m MFP to -m TEST to resemble jModelTest/ProtTest
```
the flag `-m` is the option to specify the model name to use during the analysis.   
The special MFP key word stands for ModelFinder Plus, which tells IQ-TREE to perform ModelFinder and the remaining analysis using the selected model.    
ModelFinder computes the loglikelihoods of an initial parsimony tree for many different models and the **Akaike information criterion (AIC)**, **corrected Akaike information criterion (AICc)**, and the **Bayesian information criterion (BIC)**.   
Then ModelFinder chooses the model that minimizes the **BIC score** (you can also change to AIC or AICc by adding the option -AIC or -AICc, respectively).    
*TIP: Starting with version 1.5.4, `-m MFP` is the default behavior. Thus, this run is equivalent to iqtree `-s example.phy`.*
Once ModelFinder runs, IQ-TREE will write an additional file:  
• example.phy.model: log-likelihoods for all models tested. It serves as a checkpoint file to recover an interrupted model selection.   

Sometimes you only want to find the best-fit model **without doing tree reconstruction**, then run:
```powershell
iqtree -s example.phy -m MF
# change -m MF to -m TESTONLY to resemble jModelTest/ProtTest
```
If you already know which model to use for your analysis input it with the flag -m:
```powershell
iqtree -s example.phy -m <model>
#example with TIM2+I+G
iqtree -s example.phy -m TIM2+I+G
```

For a more computationally thorough analysis the flag `-mtree` makes a full tree search for each model considered
```powershell
iqtree -s example.phy -m MF -mtree
```

### Using codon models
IQ-TREE supports a number of codon models. You need to input a protein-coding DNA alignment and specify codon data by option `-st CODON` (Otherwise, IQ-TREE applies DNA model because it detects that your alignment has DNA sequences):
```powershell
iqtree -s coding_gene.phy -st CODON
```
**! If your alignment length is not divisible by 3, IQ-TREE will stop with an error message !**
IQ-TREE will group sites 1,2,3 into codon site 1; sites 4,5,6 to codon site 2; etc.
Moreover, any codon, which has at least one gap/unknown/ambiguous nucleotide, will be treated as unknown codon character.    

Note that the above command assumes the standard genetic code. If your sequences follow ‘The Invertebrate Mitochondrial Code’ (see the full list of supported genetic
code), then run:
```powershell
iqtree -s coding_gene.phy -st CODON5
```

### BOOTSTRAP Trees
#### Assessing branch supports with ultrafast bootstrap approximation
To overcome the computational burden required by the nonparametric bootstrap, IQTREE introduces an ultrafast bootstrap **approximation** (UFBoot) that is orders of magnitude faster than the standard procedure and provides branch support values.   
To run UFBoot:    
```powershell
iqtree -s example.phy -m TIM2+I+G -B 1000
# for version 1.x change -B to -bb
```
-B specifies the number of bootstrap replicates where 1000 is the minimum number recommended.     

The section MAXIMUM LIKELIHOOD TREE in example.phy.iqtree shows a textual representation of the maximum likelihood tree with branch support values in percentage.    
The NEWICK format of the tree is printed to the file example.phy.treefile. 
You are going to want to look at:    
• **example.phy.contree**: the consensus tree with assigned branch supports where branch lengths are optimized on the original alignment. And open it with programs like [FigTree](http://tree.bio.ed.ac.uk/software/figtree/) , [iTOL](https://itol.embl.de/upload.cgi) (web), [phylo.io](https://phylo.io/) (web) *enabling the bootstrap values on the nodes/Node labels*

#### Assessing branch supports with standard nonparametric bootstrap
The standard nonparametric bootstrap is invoked by the `-b` option:
```powershell
iqtree -s example.phy -m GTR+I+G -b 100
```
`-b` specifies the number of bootstrap replicates where 100 is the minimum recommended number. The output files are similar to those produced by the UFBoot procedure.

### Partitioned analysis for multi-gene alignments
Partitioning allows you to model different regions (e.g., genes or codon positions) of an alignment with separate substitution models. 
#### FASTA File Preparation

Before partitioning, a few tips:
- **Consistent Sequence Names:** Use consistent and unique names for each sequence.
- **Alignment Quality:** Make sure the sequences are properly aligned; misalignments can lead to incorrect partitioning.
- **Single Alignment File:** Combine all genes/regions of interest into a single alignment file (e.g., `example.phy` or `example.fasta`). **The site positions in this file will later be split into partitions based on a partition file**.

For example, your FASTA file may look like:

```fasta
>Sequence1
ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGCTA...
>Sequence2
ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGCTA...
```
Once your alignment is prepared, you can specify which regions belong to which partitions using a partition file. IQ-TREE supports both RAxML-style and NEXUS partition files.
#### Partitioned Analysis with IQ-TREE
`-q partition_file`: all partitions share the same set of branch lengths.
`-p partition_file` (-spp in version 1.x): like above but allowing each partition to have its own evolution rate.
`-Q partition_file` (-sp in version 1.x): each partition has its own set of branch lengths to account for, e.g. heterotachy.

NOTE: You can also perform all three analyses and compare e.g. the BIC scores to determine the best-fit partition model.   

IQ-TREE supports RAxML-style and NEXUS partition input file. The RAxML-style partition file may look like:  
```powershell
DNA, part1 = 1-100
DNA, part2 = 101-384
```
If your partition file is called `example.partitions`, the partition analysis can be run with: 
```powershell
iqtree -s example.phy -p example.partitions -m GTR+I+G
```
Using a partition file like this imposes all partitions to use the same rate heterogeneity model given in -m option (+I+G in this example).     
If you want to specify, say, `+G` for the first partition and `+I+G` for the second partition, then you need to create the more flexible **NEXUS** partition file. This file contains a `SETS` block with `CharSet` and `CharPartition` commands to specify individual genes and the partition, respectively.
```powershell
#nexus
begin sets;
charset part1 = 1-100;
charset part2 = 101-384;
charpartition mine = HKY+G:part1 , GTR+I+G:part2;
end;
```
If your NEXUS file is called example.nex, then you can use the option -p to input the file as following:
```powershell
iqtree -s example.phy -p example.nex
```
IQ-TREE partitions the alignment `example.phy` into 2 sub-alignments named `part1` and `part2` containing sites (columns) 1-100 and 101-384, respectively. Moreover, IQ-TREE applies the substitution models `HKY+G` and `GTR+I+G` to `part1` and `part2`, respectively.     
Substitution model parameters and trees with branch lengths can be found in the result file `example.nex.iqtree`.
