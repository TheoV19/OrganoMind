#type: ignore
from organomind.nucleo_electro import electro_nucleo_sites_hsab
import pytest
import pandas as pd

def test_electro_nucleo_is_electro():
    elec, nuc = electro_nucleo_sites_hsab("[CH3+]")
    assert elec["symbol"] == "C"
    assert nuc["functional group"] == "none"
    assert nuc["type"] == "electrophile"
    assert elec["symbol"] == "C"
    assert elec["functional group"] == "none"
    assert elec["type"] == "electrophile"

def test_electro_nucleo_is_nucleo():
    elec, nuc = electro_nucleo_sites_hsab("CCN")
    assert nuc["symbol"] == "N"
    assert nuc["functional group"] == "primary amine"
    assert nuc["type"] == "nucleophile"
    assert elec["symbol"] == "C"
    assert elec["functional group"] == "primary amine"
    assert elec["type"] == "nucleophile"


def test_electro_nucleo_is_both():
    elec, nuc = electro_nucleo_sites_hsab("CC(=O)OC1=CC=CC=C1C(=O)O")
    assert nuc["symbol"] == "O"
    assert nuc["functional group"] == "carboxylic acid"
    assert nuc["type"] == "nucleophile"
    assert elec["symbol"] == "C"
    assert elec["functional group"] == "ester"
    assert elec["type"] == "electrophile"

def test_electro_nucleo_invalid_smiles():
    with pytest.raises(Exception):
        electro_nucleo_sites_hsab("invalid_smiles")