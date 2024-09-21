# Autor: Gabriel Nobre
# Data: 20 de Setembro de 2024
# Descrição: Este arquivo é responsável por fazer os tratamentos das bases de dados enviadas para
# consumo na aplicação.
# License: 

# Imports

import os
import pickle
import pandas as pd

# Code

def importar_arquivos()-> pd.DataFrame:
    """
    Método para importar os DataFrames salvos no formato pkl.
    Por enquanto não vamos receber dados externos, mas no futuro isso será implementado.
    """
    #ceaec = pickle.load(open("E:/4_arquivos/1_projeto/modelo_unicin/src/data/processed/2_0_eda_ceaec.pkl","rb"))
    #reposicons = pickle.load(open("E:/4_arquivos/1_projeto/modelo_unicin/src/data/processed/2_0_eda_reposicons.pkl","rb"))
    
    ceaec = pickle.load(open("./src/data/processed/2_0_eda_ceaec.pkl","rb"))
    reposicons = pickle.load(open("./src/data/processed/2_0_eda_reposicons.pkl","rb"))
    
    return reposicons, ceaec

def mesclar_arquivos()-> pd.DataFrame:
    """
    Método para meclar os DataFrames. Aporveito para acrescentar 1 coluna de identificação da tabela.
    Preciso colocar essa identificação para não misturar os dados na hora da análise.
    """
    reposicons, ceaec = importar_arquivos()
    
    reposicons['maquina'] = "Reposicons"
    ceaec['maquina'] = "CEAEC"
    
    df_pronto = pd.concat([reposicons,ceaec], ignore_index=True)
    
    return df_pronto

def df_pronto_para_consumo()-> pd.DataFrame:
    
    df_pronto = mesclar_arquivos()
    
    return df_pronto

if __name__ == "__main__":
    
    df_pronto_para_consumo()