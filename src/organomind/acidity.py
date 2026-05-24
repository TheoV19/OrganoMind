import pubchempy as pcp # type: ignore
import rdkit as rd
from rdkit import Chem 
from organomind.functional_groups import detect_functional_groups #type: ignore
from organomind.data.acid_base_data import acid_base_info
import pandas as pd #type: ignore

def acid_base_estimate (smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError("Invalid Molecule inserted.")
    
    detected_groups = detect_functional_groups(smiles, return_df = False)
    acidic_groups=[]
    basic_groups=[]
    
    for group, group_info in detected_groups.items():
        if group not in acid_base_info:
            continue
        values=acid_base_info[group]
        result = {
            "group": group,
            "count": group_info["amount"],
            "positions": group_info["position"],
            "type": values["type"],
            "strength": values["strength"],
            "pka_range": values["pka_range"],
            "priority": values["priority"]
        }
        
        if values["type"]=="acidic":
            acidic_groups.append(result)
        elif values["type"]=="basic":
            basic_groups.append(result)
        
    acidic_groups.sort(key=lambda x: x["priority"])
    basic_groups.sort(key=lambda x: x["priority"])

    df_acidic = pd.DataFrame(acidic_groups)
    df_basic = pd.DataFrame(basic_groups)
    
    

    return df_acidic, df_basic
