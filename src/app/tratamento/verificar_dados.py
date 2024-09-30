# Autor: Gabriel Nobre
# Data: 30 de Setembro de 2024
# Descrição: Este arquivo é responsável por fazer os tratamentos das bases de dados enviadas para
# consumo na aplicação.
# License: 

# Imports

import os
import pickle

import pandas       as pd
import streamlit    as st

class ReceberDados:

    def __init__(
        self, 
        df: pd.DataFrame, 
        lista_colunas_padrao: list,
        tipo_de_dados: dict
        ):
        
        self.df = df
        self.lista_colunas_padrao = [
            'subscription_name',
            'subscription_guid'
            'date',
            'resource_guid',
            'service_name',
            'service_type',
            'service_region',
            'service_resource',
            'quantity',
            'cost'
            ],
        self.tipo_de_dados = {}
    
    def get_lista_colunas_padrao(self) -> list:
        return self.lista_colunas_padrao
    
    def set_lista_colunas_padrao(self, lista_colunas: list):
        self.lista_colunas_padrao = lista_colunas
    
    def get_df(self) -> pd.DataFrame:
        return self.df
    
    def set_df(self, df: pd.DataFrame):
        self.df = df
    
    def valaidar_df(self, df: pd.DataFrame)-> pd.DataFrame:
        
        if isinstance(df, pd.DataFrame):
            return df
        else:
            mensagem = f"Você enviou um {type(df)}, não pode ser aceito.\n"\
                        "Escolha um arquivo CSV e siga as orientações no menu."
            return mensagem

    def valaidar_colunas_corretas(self, df: pd.DataFrame)-> bool:


        colunas_corretas = False

        # Verifica se todas as colunas estão corretas
        if set(lista_colunas_padrao) == set(df.columns):
            colunas_corretas = True

        return colunas_corretas

    def valaidar_tamanho_colunas(self, df: pd.DataFrame)-> bool:

        tamanho_colunas = False

        # Verifica colunas faltando ou extras
        len_colunas = 10 - len(set(df.columns))

        # Verifica se não há colunas faltando nem extras
        if len_colunas == 0:
            tamanho_colunas = True

        return tamanho_colunas

    def verificar_tipo_dados(self, df: pd.DataFrame)-> pd.DataFrame:
        ...
    

#todo: terminar os tipos de dados
