# type: ignore
import pubchempy as pcp  # type: ignore
import streamlit as st
from streamlit_ketcher import st_ketcher
from organomind.draw3D import draw_molecule_3d
from organomind.functional_groups import detect_functional_groups_df
from organomind.stereo import chiral_center, color_chiral, find_isomers
from organomind.acidity import acid_base_estimate
from organomind.aromatic import detect_aromatic
from organomind.point_groups import find_group
from organomind.nucelo_electro import electro_nucleo_sites_hsab
from organomind.highlight_functional_groups import draw_molecule_with_functional_groups
from organomind.cas import filter_cas


# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="OrganoMind",
    page_icon="🧪",
    layout="wide"
)

# =========================
# HEADER
# =========================
st.title("🧪 OrganoMind")
st.caption("Organic Chemistry Assistant · PubChem + RDKit")
st.caption("EPFL · 2nd Year · Practical Programming in Chemistry · 2026")

st.markdown("---")

# =========================
# INTRODUCTION
# =========================
st.markdown("""
**OrganoMind** is an organic chemistry assistant that enables **3D visualization of molecules**
with built-in features providing chemical and stereochemical properties — helping you better
understand reactivity and chemical processes. Enter a molecule by name, formula, SMILES or
draw it directly, and OrganoMind gives you everything you need.
""")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("🧬 3D Visualization")
    st.markdown("🔄 Stereochemistry")
    st.markdown("🔷 Point Groups")
with col2:
    st.markdown("🔬 Functional Groups")
    st.markdown("⚗️ Acidity / Basicity")
    st.markdown("🏷️ IUPAC Naming")
with col3:
    st.markdown("⭕ Aromaticity")
    st.markdown("⚡ Nucleophilicity")
    st.markdown("🔑 CAS / SMILES")

st.markdown("---")
st.markdown("👥 **Team:** Théo Vienne · Noam Balter-Dejeux · Tolga Seckin · Théo Morales Crassier")
st.markdown("---")

# =========================
# SIDEBAR OPTIONS
# =========================
st.sidebar.header("⚙️ Analysis Options")

info = st.sidebar.multiselect(
    "Select information to display:",
    [
        "Molecular formula",
        "Molecular weight",
        "IUPAC name",
        "SMILES",
        "CAS",
        "Rotatable bonds",
        "Stereochemistry",
        "Functional groups",
        "Aromaticity",
        "Acidity/Basicity",
        "Nucleophilicity/Electrophilicity",
        "Point groups",
        "3D drawing"
    ],
    default=["Molecular formula", "Molecular weight", "IUPAC name"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Tip: SMILES gives most accurate structure results")

# =========================
# HELPERS
# =========================

def show(label, value):
    st.write(f"**{label}** {value}")

# =========================
# RESULT DISPLAY
# =========================
def display_results(c):

    st.subheader("📋 General Information")

    if "Molecular formula" in info:
        show("Formula:", c.molecular_formula)

    if "Molecular weight" in info:
        show("Weight:", f"{c.molecular_weight} g/mol")

    if "IUPAC name" in info:
        show("IUPAC:", c.iupac_name)

    if "SMILES" in info:
        st.code(c.smiles)

    if "CAS" in info:
        show("CAS:", filter_cas(c.synonyms) or "N/A")

    if "Rotatable bonds" in info:
        show("Rotatable bonds:", c.rotatable_bond_count)



    if "Stereochemistry" in info:
        st.subheader("🔄 Stereochemistry")
        col1, col2 = st.columns(2)
        with col1:
            st.write("Chiral centers:", chiral_center(c.smiles))
        with col2:
            st.write("Possible isomers:", find_isomers(c.smiles))
        
        img = color_chiral(c.smiles)
        if img is None:
            st.info("No chiral centers found.")
        else:
            st.image(img, caption="Highlighted chiral centers")


    if "Functional groups" in info:
        st.subheader("🔬 Functional Groups")
        st.dataframe(detect_functional_groups_df(c.smiles))
        draw_molecule_with_functional_groups((c.smiles), filename=None, show_streamlit=True)

    if "Aromaticity" in info:
        st.subheader("⭕ Aromaticity")
        st.dataframe(detect_aromatic(c.smiles))

    if "Acidity/Basicity" in info:
        st.subheader("⚗️ Acidity / Basicity")
        acidic, basic = acid_base_estimate(c.smiles)
        col1, col2 = st.columns(2)
        with col1:
            st.write("🔴 Acidic sites")
            st.dataframe(acidic)
        with col2:
            st.write("🔵 Basic sites")
            st.dataframe(basic)

    if "Nucleophilicity/Electrophilicity" in info:
        st.subheader("⚡ Reactivity")
        st.dataframe(electro_nucleo_sites_hsab(c.smiles))

    if "Point groups" in info:
        st.subheader("🔷 Symmetry")
        st.write("Point group:", find_group(c.smiles))

    if "3D drawing" in info:
        st.subheader("🧬 3D Structure")
        draw_molecule_3d(c.smiles)

# =========================
# TABS
# =========================
tab1, tab2 = st.tabs(["🔍 Search", "✏️ Draw"])

# =========================
# TAB 1 - SEARCH
# =========================
with tab1:
    st.subheader("Molecule Search")
    col1, col2 = st.columns([1, 2])
    with col1:
        search_type = st.selectbox(
            "Search by:",
            ["Name", "Formula", "SMILES", "Inchi", "Inchikey"]
        )
    with col2:
        query = st.text_input("Enter molecule")

    if query:
        with st.spinner("Searching PubChem..."):
            results = pcp.get_compounds(query, search_type)
            if results:
                compound = results[0]
                st.success(f"Found: {compound.iupac_name or query}")
                display_results(compound)
            else:
                st.error("No compound found")

# =========================
# TAB 2 - DRAW
# =========================
with tab2:
    st.subheader("Draw Molecule")
    st.info("Draw a molecule to analyze its structure")
    drawing = st_ketcher()

    if drawing:
        with st.spinner("Processing molecule..."):
            result = pcp.get_compounds(drawing, "smiles")
            if result:
                compound = result[0]
                st.success(f"Identified: {compound.iupac_name or 'Unknown'}")
                display_results(compound)
            else:
                st.error("Molecule not found in PubChem")