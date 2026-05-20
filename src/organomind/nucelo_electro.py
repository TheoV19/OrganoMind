import rdkit as rd
from rdkit.Chem import AllChem, rdPartialCharges
from rdkit import Chem 
from organomind.data.nucleo_data import HSAB_rules
from organomind.functional_groups import detect_functional_groups #type: ignore
import pandas as pd #type: ignore
import streamlit as st  #type:ignore

 
def electro_nucleo_sites_hsab(mol):
    """
    Find the most electrophilic and nucleophilic sites using Gasteiger
    charges corrected by HSAB theory and functional group detection.
    Assumes neutral environment (pH = 7):
        - Amines (pKa ~9-11) are protonated → poor nucleophiles
        - Carboxylic acids (pKa ~4-5) are deprotonated → good nucleophiles (COO-)
        - Alcohols, phenols, thiols are neutral
 
    Args:
        mol (str or rdkit.Chem.Mol): SMILES string or RDKit Mol object.
 
    Returns:
        tuple: (most_electrophilic, most_nucleophilic) where each element
               is a dictionary with the following keys:
                   - atom_idx        (int)   : atom index in the molecule
                   - symbol          (str)   : atomic symbol
                   - functional_group(str)   : detected functional group
                   - type            (str)   : 'electrophile' or 'nucleophile'
                     
    """
    smiles = mol if isinstance(mol, str) else Chem.MolToSmiles(mol)
    if isinstance(mol, str):
        mol = Chem.MolFromSmiles(mol)
 
    rdPartialCharges.ComputeGasteigerCharges(mol)
 
    
    groups = detect_functional_groups(smiles, return_df=False)
 
    
    atom_to_group = {}
    for group_name, info in groups.items():
        if group_name not in HSAB_rules:
            continue
        for match in info["position"]:
            for atom_idx in match:
                if atom_idx not in atom_to_group:
                    atom_to_group[atom_idx] = group_name
                else:
                    current = HSAB_rules[atom_to_group[atom_idx]]
                    new     = HSAB_rules[group_name]
                    if (abs(new["nucleo"]) + abs(new["electro"]) >
                        abs(current["nucleo"]) + abs(current["electro"])):
                        atom_to_group[atom_idx] = group_name
 
    results = []
    for atom in mol.GetAtoms():
        if atom.GetAtomicNum() == 1:
            continue
 
        idx          = atom.GetIdx()
        charge       = atom.GetDoubleProp("_GasteigerCharge")
        group        = atom_to_group.get(idx, None)
        hsab         = HSAB_rules.get(group, {"nucleo": 0.0, "electro": 0.0})
        formal_charge = atom.GetFormalCharge()
 
        
        formal_bonus = 0.0
        if formal_charge < 0:
            formal_bonus = -0.50  
        elif formal_charge > 0:
            formal_bonus =  0.50 
 
        nuc_score  = round(charge + hsab["nucleo"]  + formal_bonus, 4)
        elec_score = round(charge + hsab["electro"], 4)
 
        results.append({
            "atom idx":         idx,
            "symbol":           atom.GetSymbol(),
            "charge":           round(charge, 4),
            "functional group": group if group else "none",
            "nuc score":        nuc_score,
            "elec score":       elec_score,
            "type":             "electrophile" if charge > 0 else "nucleophile"
        })
 
    df = pd.DataFrame(results)

    if df.empty:
        st.write("No results found.")
        return df

    most_electrophilic = df.loc[df["elec score"].idxmax()]
    most_nucleophilic  = df.loc[df["nuc score"].idxmin()]

    most_electrophilic_drop = most_electrophilic.drop(
        labels=["charge", "nuc score", "elec score"]
    )

    most_nucleophilic_drop = most_nucleophilic.drop(
        labels=["charge", "nuc score", "elec score"]
    )
 
 
    return most_electrophilic_drop, most_nucleophilic_drop


