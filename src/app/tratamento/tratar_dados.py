# Autor: Gabriel Nobre
# Data: 20 de Setembro de 2024
# Descrição: Este arquivo é responsável por fazer os tratamentos das bases de dados enviadas para
# consumo na aplicação.
# License: 

# Imports

import os
import pickle
import inflection

import pandas       as pd
import streamlit    as st

#todo: a ideia é quando o usuário apertar um botão ele será chamado
#todo: quando chamado ele vai verificar se está tudo correto com o dataframe
#todo: se estiver tudo correto, então faz os tratamentos, se não, volta uma msg para o usuário.
#todo: vê se faz aqui ou se faz na página mesmo do formulário "update_dados"
def receber_df()-> pd.DataFrame:
    ...

def importar_arquivos()-> pd.DataFrame:
    """
    Método para importar os DataFrames salvos no formato pkl.
    Por enquanto não vamos receber dados externos, mas no futuro isso será implementado.
    """
    #ceaec = pickle.load(open("E:/4_arquivos/1_projeto/modelo_unicin/src/data/processed/2_0_eda_ceaec.pkl","rb"))
    #portal = pickle.load(open("E:/4_arquivos/1_projeto/modelo_unicin/src/data/processed/2_0_eda_portal.pkl","rb"))
    
    ceaec = pickle.load(open("./src/data/processed/2_0_eda_ceaec.pkl","rb"))
    portal = pickle.load(open("./src/data/processed/2_0_eda_portal.pkl","rb"))
    
    return portal, ceaec

def mesclar_arquivos()-> pd.DataFrame:
    """
    Método para meclar os DataFrames. Aporveito para acrescentar 1 coluna de identificação da tabela.
    Preciso colocar essa identificação para não misturar os dados na hora da análise.
    """
    portal, ceaec = importar_arquivos()
    
    portal['maquina'] = "Portal"
    ceaec['maquina'] = "CEAEC"
    
    df_pronto = pd.concat([portal,ceaec], ignore_index=True)
    
    return df_pronto

# Tem que rever o que vai fazer com isso aqui.

def mundaca_tipo_date(df: pd.DataFrame)-> pd.DataFrame:
    
    df['date'] = pd.to_datetime( df['date'] )
    
    return df

def renomear_colunas(df: pd.DataFrame)-> pd.DataFrame:
    
    columns_old = df.columns
    snakecase = lambda x : inflection.underscore(x)
    columns_new = list(map(snakecase,columns_old))
    df.columns = columns_new
    
    return df

#todo: Essa função aqui tem que ser repensada, já será passada os DataFrames. O negócio é salvar depois.
def df_pronto_para_consumo()-> pd.DataFrame:
    
    df_pronto = mesclar_arquivos()
    
    return df_pronto

if __name__ == "__main__":
    
    df_pronto_para_consumo()