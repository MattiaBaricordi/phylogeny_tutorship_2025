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
```
IQ-TREE multicore version 2.4.0 for Windows 64-bit built Feb  7 2025
Developed by Bui Quang Minh, Nguyen Lam Tung, Olga Chernomor, Heiko Schmidt,
Dominik Schrempf, Michael Woodhams, Ly Trong Nhan, Thomas Wong

Host:    SGCSA-L138179DW (AVX2, FMA3, 15 GB RAM)
Command: C:\Users\mattia.baricordi\Desktop\iqtree-2.4.0-Windows\bin\iqtree2.exe -s ../example.phy
Seed:    820468 (Using SPRNG - Scalable Parallel Random Number Generator)
Time:    Fri Mar 07 09:47:55 2025
Kernel:  AVX+FMA - 1 threads (4 CPU cores detected)

HINT: Use -nt option to specify number of threads because your CPU has 4 cores!
HINT: -nt AUTO will automatically determine the best number of threads to use.

Reading alignment file ../example.phy ... Phylip format detected
Alignment most likely contains DNA/RNA sequences
Alignment has 17 sequences with 1998 columns, 1152 distinct patterns
1009 parsimony-informative, 303 singleton sites, 686 constant sites
           Gap/Ambiguity  Composition  p-value
Analyzing sequences: done in 0.0001222 secs
   1  LngfishAu    0.15%    passed      6.20%
   2  LngfishSA    0.00%    failed      0.62%
   3  LngfishAf    0.05%    failed      1.60%
   4  Frog         0.05%    passed     58.01%
   5  Turtle       0.15%    passed     44.25%
   6  Sphenodon    0.10%    passed     59.78%
   7  Lizard       0.90%    passed     38.67%
   8  Crocodile    0.35%    failed      2.51%
   9  Bird         0.00%    failed      0.00%
  10  Human        0.00%    failed      0.85%
  11  Seal         0.00%    passed     68.93%
  12  Cow          0.00%    passed     59.11%
  13  Whale        0.00%    passed     97.83%
  14  Mouse        0.05%    failed      1.43%
  15  Rat          0.00%    passed     39.69%
  16  Platypus     0.00%    failed      3.46%
  17  Opossum      0.00%    failed      0.01%
****  TOTAL        0.11%  8 sequences failed composition chi2 test (p-value<5%; df=3)
```
---
```
Create initial parsimony tree by phylogenetic likelihood library (PLL)... 0.002 seconds
Perform fast likelihood tree search using GTR+I+G model...
Estimate model parameters (epsilon = 5.000)
Perform nearest neighbor interchange...
Estimate model parameters (epsilon = 1.000)
1. Initial log-likelihood: -21149.102
Optimal log-likelihood: -21148.966
Rate parameters:  A-C: 3.87058  A-G: 5.36996  A-T: 3.97471  C-G: 0.43083  C-T: 15.77686  G-T: 1.00000
Base frequencies:  A: 0.355  C: 0.228  G: 0.192  T: 0.225
Proportion of invariable sites: 0.157
Gamma shape alpha: 0.739
Parameters optimization took 1 rounds (0.026 sec)
Time for fast ML tree search: 0.300 seconds

NOTE: ModelFinder requires 6 MB RAM!
ModelFinder will test up to 484 DNA models (sample size: 1998 epsilon: 0.100) ...
 No. Model         -LnL         df  AIC          AICc         BIC
  1  GTR+F         22701.550    39  45481.100    45482.693    45699.496
  2  GTR+F+I       21615.547    40  43311.095    43312.771    43535.091
  3  GTR+F+G4      21155.969    40  42391.939    42393.615    42615.935
  4  GTR+F+I+G4    21148.849    41  42379.699    42381.460    42609.295
  5  GTR+F+R2      21235.660    41  42553.320    42555.080    42782.916
  6  GTR+F+R3      21147.078    43  42380.156    42382.093    42620.952
  7  GTR+F+R4      21146.626    45  42383.251    42385.372    42635.247
 14  GTR+F+I+R2    21174.433    42  42432.866    42434.714    42668.062
 15  GTR+F+I+R3    21147.078    44  42382.155    42384.183    42628.551
 16  GTR+F+I+R4    21146.748    46  42385.496    42387.712    42643.092
 25  SYM+G4        21317.773    37  42709.546    42710.981    42916.743
 26  SYM+I+G4      21306.386    38  42688.772    42690.285    42901.568
 47  TVM+F+G4      21300.238    39  42678.475    42680.069    42896.871
 48  TVM+F+I+G4    21288.405    40  42656.810    42658.486    42880.806
 69  TVMe+G4       21422.114    36  42916.229    42917.587    43117.825
 70  TVMe+I+G4     21407.662    37  42889.325    42890.759    43096.521
 91  TIM3+F+G4     21367.928    38  42811.857    42813.370    43024.653
 92  TIM3+F+I+G4   21359.550    39  42797.099    42798.693    43015.496
113  TIM3e+G4      21717.449    35  43504.899    43506.183    43700.895
114  TIM3e+I+G4    21708.477    36  43488.955    43490.313    43690.551
135  TIM2+F+G4     21159.731    38  42395.462    42396.975    42608.259
136  TIM2+F+I+G4   21152.612    39  42383.224    42384.818    42601.620
157  TIM2e+G4      21320.879    35  42711.758    42713.042    42907.754
158  TIM2e+I+G4    21309.057    36  42690.115    42691.473    42891.711
179  TIM+F+G4      21368.784    38  42813.567    42815.080    43026.364
180  TIM+F+I+G4    21360.272    39  42798.544    42800.137    43016.940
201  TIMe+G4       21718.123    35  43506.246    43507.531    43702.243
202  TIMe+I+G4     21709.149    36  43490.297    43491.656    43691.894
223  TPM3u+F+G4    21488.913    37  43051.825    43053.260    43259.022
224  TPM3u+F+I+G4  21474.794    38  43025.589    43027.102    43238.385
245  TPM3+G4       21847.238    34  43762.476    43763.689    43952.873
246  TPM3+I+G4     21833.462    35  43736.924    43738.208    43932.920
267  TPM2u+F+G4    21303.762    37  42681.524    42682.958    42888.720
268  TPM2u+F+I+G4  21291.568    38  42659.137    42660.650    42871.933
289  TPM2+G4       21424.805    34  42917.610    42918.822    43108.006
290  TPM2+I+G4     21410.108    35  42890.215    42891.499    43086.212
311  K3Pu+F+G4     21489.343    37  43052.687    43054.122    43259.883
312  K3Pu+F+I+G4   21475.259    38  43026.518    43028.031    43239.315
333  K3P+G4        21847.491    34  43762.981    43764.194    43953.378
334  K3P+I+G4      21833.614    35  43737.229    43738.513    43933.226
355  TN+F+G4       21369.057    37  42812.114    42813.549    43019.310
356  TN+F+I+G4     21360.716    38  42797.432    42798.945    43010.228
377  TNe+G4        21718.193    34  43504.387    43505.599    43694.783
378  TNe+I+G4      21709.196    35  43488.392    43489.677    43684.389
399  HKY+F+G4      21489.748    36  43051.496    43052.854    43253.092
400  HKY+F+I+G4    21475.591    37  43025.182    43026.617    43232.378
421  K2P+G4        21847.674    33  43761.348    43762.491    43946.145
422  K2P+I+G4      21833.840    34  43735.679    43736.892    43926.076
443  F81+F+G4      22031.579    35  44133.158    44134.443    44329.155
444  F81+F+I+G4    22019.146    36  44110.291    44111.650    44311.888
465  JC+G4         22258.086    32  44580.171    44581.246    44759.368
466  JC+I+G4       22245.386    33  44556.772    44557.914    44741.568
Akaike Information Criterion:           GTR+F+I+G4
Corrected Akaike Information Criterion: GTR+F+I+G4
Bayesian Information Criterion:         TIM2+F+I+G4
Best-fit model: TIM2+F+I+G4 chosen according to BIC

All model information printed to ../example.phy.model.gz
CPU time for ModelFinder: 4.969 seconds (0h:0m:4s)
Wall-clock time for ModelFinder: 5.092 seconds (0h:0m:5s)
```
---
```
Estimate model parameters (epsilon = 0.100)
Thoroughly optimizing +I+G parameters from 10 start values...
Init pinv, alpha: 0.000, 1.018 / Estimate: 0.000, 0.482 / LogL: -21159.749
Init pinv, alpha: 0.038, 1.018 / Estimate: 0.040, 0.528 / LogL: -21157.099
Init pinv, alpha: 0.076, 1.018 / Estimate: 0.080, 0.585 / LogL: -21154.875
Init pinv, alpha: 0.114, 1.018 / Estimate: 0.114, 0.643 / LogL: -21153.445
Init pinv, alpha: 0.153, 1.018 / Estimate: 0.144, 0.706 / LogL: -21152.668
Init pinv, alpha: 0.191, 1.018 / Estimate: 0.171, 0.775 / LogL: -21152.623
Init pinv, alpha: 0.229, 1.018 / Estimate: 0.184, 0.808 / LogL: -21152.856
Init pinv, alpha: 0.267, 1.018 / Estimate: 0.185, 0.809 / LogL: -21152.836
Init pinv, alpha: 0.305, 1.018 / Estimate: 0.186, 0.814 / LogL: -21152.890
Init pinv, alpha: 0.343, 1.018 / Estimate: 0.188, 0.819 / LogL: -21152.938
Optimal pinv,alpha: 0.171, 0.775 / LogL: -21152.623

Parameters optimization took 1.614 sec
Wrote distance file to... 
Computing ML distances based on estimated model parameters...
Calculating distance matrix: done in 0.0020944 secs
Computing ML distances took 0.002418 sec (of wall-clock time) 0.000000 sec (of CPU time)
Setting up auxiliary I and S matrices: done in 8.83e-005 secs
Computing RapidNJ tree took 0.000974 sec (of wall-clock time) 0.000000 sec (of CPU time)
Log-likelihood of RapidNJ tree: -21161.717
--------------------------------------------------------------------
|             INITIALIZING CANDIDATE TREE SET                      |
--------------------------------------------------------------------
Generating 98 parsimony trees... 0.247 second
Computing log-likelihood of 98 initial trees ... 0.313 seconds
Current best score: -21152.623

Do NNI search on 20 best initial trees
Estimate model parameters (epsilon = 0.100)
BETTER TREE FOUND at iteration 1: -21152.595
Iteration 10 / LogL: -21152.682 / Time: 0h:0m:7s
Iteration 20 / LogL: -21152.717 / Time: 0h:0m:7s
Finish initializing candidate tree set (2)
Current best tree score: -21152.595 / CPU time: 1.196
Number of iterations: 20
--------------------------------------------------------------------
|               OPTIMIZING CANDIDATE TREE SET                      |
--------------------------------------------------------------------
Iteration 30 / LogL: -21152.705 / Time: 0h:0m:8s (0h:0m:7s left)
Iteration 40 / LogL: -21152.632 / Time: 0h:0m:8s (0h:0m:5s left)
Iteration 50 / LogL: -21157.804 / Time: 0h:0m:9s (0h:0m:4s left)
Iteration 60 / LogL: -21153.168 / Time: 0h:0m:9s (0h:0m:2s left)
Iteration 70 / LogL: -21152.643 / Time: 0h:0m:9s (0h:0m:2s left)
Iteration 80 / LogL: -21152.659 / Time: 0h:0m:10s (0h:0m:1s left)
Iteration 90 / LogL: -21157.770 / Time: 0h:0m:10s (0h:0m:0s left)
UPDATE BEST LOG-LIKELIHOOD: -21152.595
Iteration 100 / LogL: -21158.437 / Time: 0h:0m:10s (0h:0m:0s left)
TREE SEARCH COMPLETED AFTER 102 ITERATIONS / Time: 0h:0m:10s

--------------------------------------------------------------------
|                    FINALIZING TREE SEARCH                        |
--------------------------------------------------------------------
Performs final model parameters optimization
Estimate model parameters (epsilon = 0.010)
1. Initial log-likelihood: -21152.595
2. Current log-likelihood: -21152.528
Optimal log-likelihood: -21152.519
Rate parameters:  A-C: 5.71080  A-G: 7.82260  A-T: 5.71080  C-G: 1.00000  C-T: 23.07389  G-T: 1.00000
Base frequencies:  A: 0.355  C: 0.228  G: 0.192  T: 0.225
Proportion of invariable sites: 0.169
Gamma shape alpha: 0.764
Parameters optimization took 2 rounds (0.023 sec)
BEST SCORE FOUND : -21152.519
Total tree length: 4.220

Total number of iterations: 102
CPU time used for tree search: 4.406 sec (0h:0m:4s)
Wall-clock time used for tree search: 4.114 sec (0h:0m:4s)
Total CPU time used: 11.031 sec (0h:0m:11s)
Total wall-clock time used: 10.900 sec (0h:0m:10s)

Analysis results written to: 
  IQ-TREE report:                ../example.phy.iqtree
  Maximum-likelihood tree:       ../example.phy.treefile
  Likelihood distances:          ../example.phy.mldist
  Screen log file:               ../example.phy.log

```
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
