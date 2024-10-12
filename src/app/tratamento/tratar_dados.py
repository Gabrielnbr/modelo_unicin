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

__CAMINHO_RAW = './src/data/raw/'
__CAMINHO_PROCESSED = './src/data/processed/'

#todo: a ideia é quando o usuário apertar um botão ele será chamado
#todo: quando chamado ele vai verificar se está tudo correto com o dataframe
#todo: se estiver tudo correto, então faz os tratamentos, se não, volta uma msg para o usuário.
#todo: vê se faz aqui ou se faz na página mesmo do formulário "update_dados"
#todo: Testar todas as colunas com os formatos originais, se alguma tivar no formato diferente, então tenta trocar o formato, se não conseguir trocar, avisa ao usuário.
def receber_df(df:pd.DataFrame)-> pd.DataFrame:
    ...

def importar_arquivos()-> list:
    """
    Método para importar os DataFrames salvos no formato pkl.
    Por enquanto não vamos receber dados externos, mas no futuro isso será implementado.
    """
    #ceaec = pickle.load(open("E:/4_arquivos/1_projeto/modelo_unicin/src/data/processed/2_0_eda_ceaec.pkl","rb"))
    #portal = pickle.load(open("E:/4_arquivos/1_projeto/modelo_unicin/src/data/processed/2_0_eda_portal.pkl","rb"))
    
    
    arquivos = os.listdir(__CAMINHO_RAW)
    lista_arquivos = [arquivo for arquivo in arquivos if arquivo.endswith('.csv')]
    
    return lista_arquivos

def mesclar_arquivos(lista_arquivos: list)-> pd.DataFrame:
    """
    Método para meclar os DataFrames. Aporveito para acrescentar 1 coluna de identificação da tabela.
    Preciso colocar essa identificação para não misturar os dados na hora da análise.
    """
    dfs = pd.DataFrame()
    for arquivo in lista_arquivos:
    
        df = pd.read_csv( os.path.join( __CAMINHO_RAW, arquivo ) )
        maquina = arquivo.split('_')[1]
        df['maquina'] = maquina
    
        df = renomear_colunas(df)
        df = mundaca_tipo_date(df)

        if dfs.empty:
            dfs = df
        else:
            if maquina in dfs['maquina'].values:

                date = dfs.loc[dfs['maquina'] == maquina, 'date']
                filtro = date.max()
                df = df.loc[df['date'] > filtro]
                
                dfs = pd.concat([dfs,df], ignore_index=True)
            else:
                dfs = pd.concat([dfs,df], ignore_index=True)

    return dfs

def mundaca_tipo_date(df: pd.DataFrame)-> pd.DataFrame:
    
    df['date'] = pd.to_datetime( df['date'] )
    
    return df


def renomear_colunas(df: pd.DataFrame)-> pd.DataFrame:
    
    columns_old = df.columns
    snakecase = lambda x : inflection.underscore(x)
    columns_new = list(map(snakecase,columns_old))
    df.columns = columns_new
    
    return df

def novas_colunas_date(df:pd.DataFrame)-> pd.DataFrame:
    # year
    df['year'] = df['date'].dt.year
    # month
    df['month'] = df['date'].dt.month
    # day
    df['day'] = df['date'].dt.day
    # week of year
    df['week_of_year'] = df['date'].dt.isocalendar().week
    # year week
    df['year_week'] = df['date'].dt.strftime('%Y-%W')
    # year month
    df['year_month'] = df['date'].dt.strftime('%Y-%m')

    df['data_br'] = df['date'].dt.strftime('%d/%m/%Y')
    
    return df

#todo: Essa função aqui tem que ser repensada, já será passada os DataFrames. O negócio é salvar depois.

def df_pronto_para_consumo()-> pd.DataFrame:
    
    lista_arquivos = importar_arquivos()
    
    df_pronto = mesclar_arquivos(lista_arquivos)
    
    df_pronto = novas_colunas_date(df_pronto)
    # exportar_arquivo(df_pronto)
    
    return df_pronto

if __name__ == "__main__":
    
    df_pronto_para_consumo()