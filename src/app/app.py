# Autor: Gabriel Nobre
# Data: 20 de Setembro de 2024
# Descrição: Este arquivo contem a inicialização da aplicação para verificação dos
# consumos das máquinas virtuais acessíveis pelo CIT da UNICIN.
# License: 

# Imports
import streamlit as st
from multiapp import MultiApp
from paginas import ceaec, outros, home

def app_run():
    """
    Este método define toda a aplicação no streamlit e faz sua inicialização
    """
    
    app = MultiApp()
    # Inicialização do app
    app.add_app("1. Home Page",home.app)
    app.add_app("2. CEAEC",ceaec.app )
    app.add_app("3. outros",outros.app )
    
    app.run()

# Main app
if __name__ == "__main__":
    
    st.set_page_config( layout='wide' )
    
    app_run()