import streamlit as st

st.set_page_config(page_title="Inicio", layout="wide")

pag_inicio = st.Page("pages/00_Home.py", title="Inicio")
pag_Images = st.Page("pages/01_Images.py", title="Imagens")
pag_Mapa = st.Page("pages/02_Mapa.py", title="Mapa")

pg = st.navigation({
    "Principal": [pag_inicio,],
    "Herramientas": [pag_Images, pag_Mapa],
})

pg.run()

