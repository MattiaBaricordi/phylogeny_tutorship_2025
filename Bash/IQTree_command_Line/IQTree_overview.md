## Using IQ-TREE for Phylogenetic Analysis
**IQ-TREE is a software for phylogenomic inference, uses a stochastic algorithm to infer phylogenetic trees by Maximum Likelihood.** \
It produces an unrooted tree by default, simply ordering the taxa as they appear in the alignment.  

-> IQTree Manual available at http://www.iqtree.org/doc/iqtree-doc.pdf  
-> WebServer available at http://iqtree.cibiv.univie.ac.at/  
### Example of a Maximum-Likelihood Tree Output
At the end of the run, IQ-TREE generates an ML tree that may look like this:  

![Untitled design (1)](https://github.com/user-attachments/assets/b78b07e8-ec30-46af-9196-0a2016fda60c)

This tree makes sense as mammals (Human to Opossum) form a clade, while reptiles (Turtle to Crocodile) and birds form a sister clade. 

### Running a Basic Maximum-Likelihood Analysis
```bash
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
```bash
iqtree -s example.phy -redo
```
Finally, the default prefix of all output files is the alignment file name. You can
change the prefix with:
```bash
iqtree -s example.phy --prefix myprefix
# for version 1.x change --prefix to -pre
This prevents output files being overwritten when you perform multiple analyses on
the same alignment within the same folder.
```
If a run is interrupted, IQ-TREE saves a checkpoint file (e.g., `example.phy.ckp.gz`). To resume the run:
```bash
iqtree -s example.phy
```

### Specifying an Output Prefix
To prevent overwriting files when performing multiple analyses on the same alignment:
```bash
iqtree -s example.phy --prefix myprefix
```

### Choosing the Right Substitution Model
**ModelFinder** to determine the best-fit model:
```bash
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
```bash
iqtree -s example.phy -m MF
# change -m MF to -m TESTONLY to resemble jModelTest/ProtTest
```
If you already know which model to use for your analysis input it with the flag -m:
```bash
iqtree -s example.phy -m <model>
#example with TIM2+I+G
iqtree -s example.phy -m TIM2+I+G
```

For a more computationally thorough analysis the flag `-mtree` makes a full tree search for each model considered
```bash
iqtree -s example.phy -m MF -mtree
```

### Using codon models
IQ-TREE supports a number of codon models. You need to input a protein-coding DNA alignment and specify codon data by option `-st CODON` (Otherwise, IQ-TREE applies DNA model because it detects that your alignment has DNA sequences):
```bash
iqtree -s coding_gene.phy -st CODON
```
**! If your alignment length is not divisible by 3, IQ-TREE will stop with an error message !**
IQ-TREE will group sites 1,2,3 into codon site 1; sites 4,5,6 to codon site 2; etc.
Moreover, any codon, which has at least one gap/unknown/ambiguous nucleotide, will be treated as unknown codon character.    

Note that the above command assumes the standard genetic code. If your sequences follow ‘The Invertebrate Mitochondrial Code’ (see the full list of supported genetic
code), then run:
```bash
iqtree -s coding_gene.phy -st CODON5
```

### BOOTSTRAP Trees
#### Assessing branch supports with ultrafast bootstrap approximation
To overcome the computational burden required by the nonparametric bootstrap, IQTREE introduces an ultrafast bootstrap **approximation** (UFBoot) that is orders of magnitude faster than the standard procedure and provides branch support values.   
To run UFBoot:    
```bash
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
```bash
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
```bash
DNA, part1 = 1-100
DNA, part2 = 101-384
```
If your partition file is called `example.partitions`, the partition analysis can be run with: 
```bash
iqtree -s example.phy -p example.partitions -m GTR+I+G
```
Using a partition file like this imposes all partitions to use the same rate heterogeneity model given in -m option (+I+G in this example).     
If you want to specify, say, `+G` for the first partition and `+I+G` for the second partition, then you need to create the more flexible **NEXUS** partition file. This file contains a `SETS` block with `CharSet` and `CharPartition` commands to specify individual genes and the partition, respectively.
```bash
#nexus
begin sets;
charset part1 = 1-100;
charset part2 = 101-384;
charpartition mine = HKY+G:part1 , GTR+I+G:part2;
end;
```
If your NEXUS file is called example.nex, then you can use the option -p to input the file as following:
```bash
iqtree -s example.phy -p example.nex
```
IQ-TREE partitions the alignment `example.phy` into 2 sub-alignments named `part1` and `part2` containing sites (columns) 1-100 and 101-384, respectively. Moreover, IQ-TREE applies the substitution models `HKY+G` and `GTR+I+G` to `part1` and `part2`, respectively.     
Substitution model parameters and trees with branch lengths can be found in the result file `example.nex.iqtree`.
