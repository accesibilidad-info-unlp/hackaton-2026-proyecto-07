import streamlit as st
import plotly as pl

import streamlit_image_coordinates as sic


st.title("Mapa de la Facultad de Informática")


image = sic.streamlit_image_coordinates(
    "https://placecats.com/200/300",
    key="url",
)

st.write(image)
