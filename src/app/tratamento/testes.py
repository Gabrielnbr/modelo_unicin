import pandas as pd
import pickle
from verificar_dados import VerificarDados
import tratar_dados as td

df_raw = pd.read_csv("src\\data\\raw\\azure_usage_1mes.csv")

with open("src\\data\\processed\\2_0_eda_ceaec.pkl", "rb") as df_pkl:
    df_processed = pickle.load(df_pkl)

verificar_dados = VerificarDados(
                    df=df_raw,
                    lista_colunas_raw=df_raw.columns,
                    lista_colunas_processadas=df_processed.columns,
                    tipo_de_dados_padrao=0)

verificar_dados.valaidar_df(verificar_dados.df)

verificar_dados.lista_colunas_raw = td.renomear_colunas(verificar_dados.df)



