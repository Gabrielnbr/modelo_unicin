# Autor: Gabriel Nobre
# Data: 30 de Setembro de 2024
# Descrição: 
# License: 

# imports

import streamlit as st
import pandas as pd

from tratamento import tratar_dados as      td
from tratamento import verificar_dados as   vd

def form_receber_dados() -> pd.DataFrame:
    
    with st.form("Formulário"):
        st.header("Formulário de envio de dados em CSV")

        uploaded_file = st.file_uploader("Escolha um Arquivo CSV")
        if uploaded_file is not None:
            
            # Can be used wherever a "file-like" object is accepted:
            dataframe = pd.read_csv(uploaded_file)
            st.write(dataframe)
        
        st.form_submit_button(label="Enviar")
        
        return uploaded_file

def run():
    
    df = form_receber_dados()
    df = td.renomear_colunas(df)
    

run()

if __name__ == "__main__":
    run()