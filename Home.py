import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":derelict_house_building:",
)

st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #262730;
        }

        [data-testid="stSidebar"] .css-1d391kg {
            color: white;
        }

        }
    </style>
""", unsafe_allow_html=True)

st.write("# Bienvenido a la aplicación de Agent SQL ✨")

st.markdown(
    """
Agent SQL es una  herramienta diseñada para facilitarla interacción
con bases de datos SQL de manera intuitiva y eficiente.
En esta plataforma,  puedes realizar consultas a tu base de datos
y obtener respuestas en lenguaje natural, lo que te permite
interactuar con los datos de una forma más accesible y comprensible.

En el menú izquierdo, puedes encontrar **Agent SQL**
para realizar consultas y también **Tests**
para validar las respuestas del agente.
"""
)
