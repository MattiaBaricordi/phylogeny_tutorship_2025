# Installing IQ-TREE Using Conda on Linux

## Understanding Conda Environments
Conda environments are isolated spaces where you can install specific software and dependencies without interfering with the system’s default packages.   
They help manage software dependencies efficiently, making it easier to work on multiple projects with different package requirements.  

Each environment acts as a self-contained workspace where you can:  
- Install software without affecting other applications.  
- Use different versions of the same package for different projects.  
- Easily share and reproduce computational workflows.  

## 1. Installing Conda (If Not Already Installed)  
Before installing IQ-TREE, ensure you have Conda installed. To check:  
```bash
conda --version
```
If Conda is installed, you should see an output like:  
```
conda 23.1.0
```
If not installed, refer to the [Miniconda installation guide](https://docs.conda.io/en/latest/miniconda.html).  

## 2. Creating a Conda Environment  
To avoid conflicts with system-wide packages, it is recommended to create a new Conda environment for IQ-TREE:  
```bash
conda create -n phylo_env 
```
Activate the environment:
```bash
conda activate phylo_env
```

## 3. Installing IQ-TREE
Once inside the Conda environment, install IQ-TREE from the **bioconda** channel:
```bash
conda install -c bioconda iqtree -y
```

## 4. Verifying the Installation
After installation, verify that IQ-TREE is installed
```bash
#open the manual
iqtree -h
iqtree --help
#check the path
which iqtree
```
If the installation is successful, you should see the IQ-TREE help menu.
Alternatively, check the installed version with:
```bash
iqtree --version
```

## 5. Updating or Removing IQ-TREE
To update IQ-TREE:
```bash
conda update -c bioconda iqtree -y
```

## 6. Deactivating the Conda Environment
After using IQ-TREE, deactivate the Conda environment:
```bash
conda deactivate
```
To completely remove the environment:
```bash
conda env remove -n phylo_env
```

