# BEAST
### Prerequisites
- Java (JRE 8 or higher) installed and on your PATH.
- BEAST package (includes BEAUti, BEAST, Tracer, FigTree) downloaded and installed:

Tip: After installation, you should have icons or executables for BEAUti, BEAST, Tracer and FigTree.
## BEAUTi
BEAUti is a graphical app for designing your Bayesian analysis and **generating a BEAST XML control file**. 
You’ll see a window with a toolbar and a row of tabs along the top (Partitions, Taxa, Tips, …).   
### Import Your Alignment
In BEAUti, choose File → Import Data…, or click the “+” button, or drag-and-drop your data into the main window.

You should now see the dataset listed under Partitions.

Note: BEAUti accepts aligned FASTA, NEXUS (partitions) or BEAST XML files.

You can now Double-click the partition row to view the full alignment matrix.

### Set Calibration Points
- Click the Tips tab.
- When working with modern species, leave all tip dates = 0 (default).
- Uncheck “Use tip dates” to treat them as contemporaneous.

### Choose an Evolutionary Model
- Go to the Sites tab.  
- For nucleotide data, the default HKY model is selected. 
- Here you can select “Partition into codon positions”
- You can also select models like HKY, or whatever you ModelFinder run found most accurate

### Pick a Molecular Clock
In the Clock tab you can select which type of clock you want to use (i.e. Strict clock = all branches same rate or Relaxed clocks if you need rate variation).

### Select a Tree Prior
Click Trees.

Under Tree Prior, you choose within the Speciation menu: e.g. Yule process (species-level branching). 

You can also leave Random starting tree on (BEAST will pick a random initial tree).

Finally you can Review Priors and Operators

### Configure MCMC Parameters
Switch to the MCMC tab.

Select Chain Length (steps)

Log every (yields samples)

Echo state to screen → 10000 (keeps console output manageable)

Filenames for .log and .trees will default to output.log and output.trees.

You can increase chain length later if ESS (Effective Sample Size) is too low. 

### Save & Generate XML
File → Save to store your BEAUti settings (extension .beauti).
File → Generate XML → save as output.xml.

On Windows, you may need .xml.txt to see both extensions. 

### Run BEAST
Double-click the BEAST icon (or run beast on your xml in a terminal).

In the dialog, click Choose File…, select xml, then Run. 

BEAST will print progress to the screen and write:

output.log (parameter traces)

output.trees (sampled trees)

### Next Steps
Once the run finishes explore results with:

Tracer (inspect ESS, posterior distributions)
TreeAnnotator (summarize tree set into a consensus tree)
FigTree (visualize your annotated tree)
