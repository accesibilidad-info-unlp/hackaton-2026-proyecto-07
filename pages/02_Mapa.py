import streamlit as st
import plotly as pl
import streamlit_image_coordinates as sic
from pathlib import Path
from shapely.geometry import Point, Polygon

#los niveles se representan por piso, cada piso tiene 
#atributos (salas, baños, etc). cada atributo tiene 4 coordenadas
#se accede por ej: niveles[planta_baja][{atributo}][{area}]
BASE_DIR = Path("resources/images/Levels")

niveles = {
    "Planta baja": {
        "aula1": {
            "ESI": {"X": 843, "Y": 355},
            "ESD": {"X": 882, "Y": 376},
            "IID": {"X": 850, "Y": 436}, 
            "EII": {"X": 811, "Y": 415},
        }
    },
    "Nivel 1": {},
    "Nivel 2": {},
    "Techo": {}
}

st.title("Mapa de la Facultad de Informática")

lista_archivos = [f.name for f in BASE_DIR.iterdir() if f.is_file()]

imagen=st.selectbox("Selecciona un nivel:",
                  options=list(lista_archivos))

ruta=Path(BASE_DIR)/(imagen)
st.write(ruta)
value = sic.streamlit_image_coordinates(
    ruta, 
    key="ruta"
)
def es_clic_valido(x, y):
    aula1 = niveles["Planta baja"]["aula1"]
    
    puntos_rombo = [
        (aula1["ESI"]["X"], aula1["ESI"]["Y"]),
        (aula1["ESD"]["X"], aula1["ESD"]["Y"]),
        (aula1["IID"]["X"], aula1["IID"]["Y"]),
        (aula1["EII"]["X"], aula1["EII"]["Y"])
    ]
    
    rombo = Polygon(puntos_rombo)
    punto_clic = Point(x, y)
    
    return rombo.contains(punto_clic)

# Procesamos el clic
if value is not None:
    x_clic = value["x"]
    y_clic = value["y"]
    
    if es_clic_valido(x_clic, y_clic):
        st.success(f"Área Válida Clic dentro de Aula 1 en X: {x_clic}, Y: {y_clic}")
    else:
        st.error(f"Fuera del rombo. Clic en X: {x_clic}, Y: {y_clic}")