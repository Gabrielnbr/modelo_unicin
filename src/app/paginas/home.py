# Autor: Gabriel Nobre
# Data: 20 de Setembro de 2024
# Descrição:
# License: 

# Imports

import streamlit as st
from src.app.tratamento import tratar_dados as trd

# Code

def home():
    df = trd.df_pronto_para_consumo()
    st.dataframe(df)

def app():
    home()

if __name__ == "__main__":
    app()