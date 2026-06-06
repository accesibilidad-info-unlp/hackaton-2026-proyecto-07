import streamlit as st


<<<<<<< HEAD
niveles={
nivel1:{aula1{
    ESI{"x":"1","y":"2"}    1,5   5,1   5,5}
    ESD:{x:1,y:5}
    EII:{x5:,y:1}
    EID:{x:5,y:5}
}
nivel2:
veni3:
veni4:
}
=======
st.set_page_config(page_title="Inicio", layout="wide")

pag_inicio = st.Page("pages/00_Home.py", title="Inicio")
pag_Images = st.Page("pages/01_Images.py", title="Imagens")
pag_Mapa = st.Page("pages/02_Mapa.py", title="Mapa")

pg = st.navigation({
    "Principal": [pag_inicio,],
    "Herramientas": [pag_Images, pag_Mapa],
})

pg.run()

>>>>>>> 0e93e0c2f84ec0af269e41195674e1031aec27bb
