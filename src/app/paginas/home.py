# Autor: Gabriel Nobre
# Data: 20 de Setembro de 2024
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina Cidades"
# no aplicativo Streamlit. Ele define a estrutura da página, bem como a inicialização
# da página "Pagina Cidades"
# License: 

# Imports

import streamlit as st
from tratamento import tratamento

# Code

def home():
    df = tratamento.df_pronto_para_consumo()
    st.dataframe(df)

def app():
    home()

if __name__ == "__main__":
    app()