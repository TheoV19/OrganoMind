from rdkit import Chem 
from rdkit.Chem import Draw
from rdkit.Chem.EnumerateStereoisomers import EnumerateStereoisomers, StereoEnumerationOptions



def chiral_center(smiles: str):
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    
    center = Chem.FindMolChiralCenters(molecule, includeUnassigned=True) #includeUnassigned=True also counts chiral center not specified in smiles
    number = len(center)
    return number
    


def find_isomers(smiles: str):
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    
    options = StereoEnumerationOptions(unique=True, onlyUnassigned=False, tryEmbedding=True)
    isomers = tuple(EnumerateStereoisomers(molecule, options=options))
    
    number = len(isomers)
    return number




def color_chiral(smiles: str):
    molecule = Chem.MolFromSmiles(smiles)
    if molecule is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    stereocenters = Chem.FindMolChiralCenters(molecule, includeUnassigned=True)
    chiral_atoms = [idx for idx, _ in stereocenters]
    if not chiral_atoms:
        return None
    img = Draw.MolToImage(molecule, size=(400, 300), highlightAtoms=chiral_atoms, highlightColor=(0, 1, 0))
    return img









