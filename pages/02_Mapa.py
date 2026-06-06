import streamlit as st

#los niveles se representan por piso, cada piso tiene 
#atributos (salas, baños, etc). cada atributo tiene 4 coordenadas
#se accede por ej: niveles[planta_baja][{atributo}][{area}]
niveles={
    planta_baja={
        {"aula1":{
            "ESI":{"X":884,"Y":354},
            "ESD":{"X":880,"Y":375},
            "EII":{"X":811,"Y":415},
            "IID":{"X":849,"Y":436}
        }
        }
    },
    nivel_1={},
    nivel_2={},
    techo={}
}

