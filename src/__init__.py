# Autor: Gabriel Nobre
# Data: 20 de Setembro de 2024
# Descrição: Este arquivo contem a inicialização da aplicação para verificação dos
# consumos das máquinas virtuais acessíveis pelo CIT da UNICIN.
# License: 

# Imports
import streamlit as st

st.set_page_config( layout='wide' )

pg = st.navigation(
    [st.Page('app/paginas/visualizacao.py'),
#     st.Page('app/paginas/home.py')
     ]
    )

# Main app
if __name__ == "__main__":
    pg.run()