## Using IQ-TREE for Phylogenetic Analysis
**IQ-TREE is a software for phylogenomic inference, uses a stochastic algorithm to infer phylogenetic trees by Maximum Likelihood.**
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
