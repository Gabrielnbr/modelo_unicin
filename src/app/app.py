# Autor: Gabriel Nobre
# Data: 20 de Setembro de 2024
# Descrição: Este arquivo contem a inicialização da aplicação para verificação dos
# consumos das máquinas virtuais acessíveis pelo CIT da UNICIN.
# License: 

# Imports
import streamlit as st

st.set_page_config( layout='wide' )

pg = st.navigation(
    [st.Page("paginas/visualizacao.py")]
    )

#test
# Main app
if __name__ == "__main__":
    pg.run()
    #app = MultiApp()
    #   Inicialização do app
    #app.add_app("1. Home Page",home.app() )
    #app.add_app("2. Visualizacao",visualizacao.app() )
    #app.add_app("3. Reposicons",reposicons.app() )
    #
    #app.run()
    