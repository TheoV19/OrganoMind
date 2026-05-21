![OrganoMind Logo](assets/image.png)

<h1 align="center">
OrganoMind
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue"/>
  <img src="https://img.shields.io/badge/Streamlit-blue?logo=streamlit"/>
  <img src="https://img.shields.io/badge/RDKit-green"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow"/>
</p>


<p align="center">
  <img src="assets/interface-full.PNG" alt="OrganoMind interface" width="900"/>
</p>



## 📚General informations📚
OrganoMind is a project developped as part of Practical Progamming in chemistry EPFL (2026) during second year of study. OrganoMind is thought as a organic chemistry assistant that allows 3D visualization of molecules with built-in features that give both chemical and stereochemical properties that allows better understanding of chemical processes. 

### 💪Features💪 
- 3D visualization of molecules and IUPAC naming.
- Detection and 2D visualization of functionnal groups. 
- Detection of aromatic groups and nomenclature of the group.
- Detection of chiral centers, number of isomers and 2D visualization of the chiral center. 
- Detection of acidic and basic groups, and estimation of the pKa of the molecule.
- Detection of nucleophilic and electrophilic groups with attribution of the nucleophilic/electrophilic level.
- Determination of molecule's point group.

### 👥Contributions👥
Théo Vienne
[![GitHub](https://img.shields.io/badge/GitHub-TheoV19-181717?logo=github)](https://github.com/TheoV19)  

Noam Balter-Dejeux
[![GitHub](https://img.shields.io/badge/GitHub-NoamBalter-181717?logo=github)](https://github.com/NoamBalter)  

Tolga Seckin
[![GitHub](https://img.shields.io/badge/GitHub-tolgaseckin-181717?logo=github)](https://github.com/tolgaseckin)  

Théo Morales Crassier
[![GitHub](https://img.shields.io/badge/GitHub-theo--moralescrassier-181717?logo=github)](https://github.com/theo-moralescrassier)  


### 📈A useful assistant📈
Organomind is thought as a tool to simplify the understanding of the reactivity of complex chemical compounds. By either putting directly the structure or the name or the formula or even the smile of a molecule, organomind will give you all the characteritcis you need to work on your problem.

#### You need compute a reaction path for a synthesis ? 
Put your reactants in organomind and it will tell you which group of your molecule are nucleophilic and electrophilic with all functional groups, allowing you to determine accuratly which part will react and with what.

#### Struggle with a MO diagram ? 
Organomind will give you the point group allowing to simplify your work and focus on the important part of your search.

#### Working on a stereospcific synthesis ?
Organomind will give you the number of chiral centers and 2D view of them with the number of stable isomers which then allow you properly classify the stereo-isomers of your molecule.

Already convinced ? Let us show you how to install it and enjoy all the features of this framework ! 🎉

## ⚙️ Installation ⚙️

### Prerequisites
- Python 3.10.20
- pip

### Steps

**1. Create a CONDA virtual environment (recommended)**
```bash
#Open bash or terminal
#Name the environment as you wish and specify python 3.10
conda create -n env.name python=3.10

#Activate your environment
conda activate env.name
```

**2. Two ways to proceed**

*A. Using the repo:*
```bash
#Clone the repository
git clone https://github.com/TheoV19/OrganoMind.git

#Naviguate to the OrganoMind folder
cd path/to/organomind

#Installs the dependencies locally as a user, make sure to activate your environment before doing so 
pip install .
    or
#Installs the dependencies locally in editable mode, make sure to activate your environment before doing so
pip install -e . 
```

*B. Only using the package:*
```bash
pip install organomind 
    or
pip install git+https://github.com/TheoV19/OrganoMind.git
```


**3. Run the app**
```bash
#In your terminal, you can now run the program with:
organomind-ui
```

The app will open automatically in your browser at `http://localhost:8501`.


 

 
## 🧠How to use🧠
 
### ✍️Write your molecule anyway you want✍️
OrganoMind supports multiple input formats. In the Search tab, select your search type and enter your query:
 
| Input type | Example |
|------------|---------|
| Name | `aspirin` |
| Formula | `C9H8O4` |
| SMILES | `CC(=O)Oc1ccccc1C(=O)O` |
| InChI | `InChI=1S/C9H8O4/...` |
| InChIKey | `BSYNRYMUTXBXSQ-UHFFFAOYSA-N` |
 
> **Tip:** SMILES input gives the most accurate structure results.
 
 <p align="center">
  <img src="assets/search-aspirin.PNG" alt="Search aspirin" width="900"/>
</p>

 
### 🎨Draw a molecule🎨
 
Switch to the Draw tab to use the built-in Ketcher molecular editor. Draw your molecule directly on the canvas and OrganoMind will automatically identify and analyze it.

<p align="center">
  <img src="assets/ketcher-aspirin.PNG" alt="Aspirin drawn in Ketcher editor" width="900"/>
</p>
 

 
### Select the information to display
 
Use the **sidebar** on the left to select which properties you want to compute:
 
- **Molecular formula / weight / IUPAC name / SMILES / CAS** — General information
- **Rotatable bonds** — Conformational flexibility
- **Stereochemistry** — Chiral centers, number of stable isomers, 2D view
- **Functional groups** — Detection and 2D visualization
- **Aromaticity** — Aromatic ring detection and nomenclature
- **Acidity / Basicity** — Acidic and basic site detection with pKa estimation
- **Nucleophilicity / Electrophilicity** — Reactive site detection with HSAB-based level attribution
- **Point groups** — Symmetry group determination
- **3D drawing** — Interactive 3D visualization

## Requirements

OrganoMind requires the following dependencies, which are automatically installed when you install the package:

- `rdkit`
- `pubchempy`
- `streamlit`
- `pandas`
- `py3dmol`
- `streamlit-ketcher`
- `pillow`
- `plotly`
- `pymatgen`

If you encounter missing package errors, you can install them manually:
```bash
pip install rdkit pubchempy streamlit pandas py3dmol streamlit-ketcher pillow plotly pymatgen
```

## Need help ?
If you encounter issues or the program doesn't work, try the following steps:

1. Verify your active environment
Make sure you are working in the environment where OrganoMind is installed.
```bash
# Check which Python executable is currently active
which python
```
If it's not the correct environment, activate it:
```bash
# Activate your conda environment
conda activate your_env_name
```
2. Check and update OrganoMind
```bash
pip show organomind
```
If needed, update to the latest version:
```bash
pip install --upgrade git+https://github.com/TheoV19/OrganoMind.git
```
If problems continue, try uninstalling and reinstalling OrganoMind:
```bash
pip uninstall organomind
pip install git+https://github.com/TheoV19/OrganoMind.git
```
3. Update pip if necessary
Sometimes, issues may arise due to an outdated pip. Thus, to update pip:
- For virtual environments
```bash
pip install --upgrade pip
```
- For Linux or macOS systems
```bash
python3 -m pip install --upgrade pip
```


## 📄 License

MIT License








