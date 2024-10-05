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

class VerificarDados:

    def __init__(
        self, 
        df: pd.DataFrame | None = None, 
        lista_colunas_padrao: list | None = None,
        lista_colunas_raw: list |None = None,
        lista_colunas_processadas: list | None = None,
        tipo_de_dados_padrao: dict | None = None,
        tipo_de_dados_raw: dict |None = None,
        tipo_de_dados_processados: dict | None = None,
        ):
        
        """
        Documentação
        """
        
        self.df = df
        
        self.lista_colunas_padrao = lista_colunas_padrao
        self.lista_colunas_raw = lista_colunas_raw
        self.lista_colunas_processadas = lista_colunas_processadas
        
        self.tipo_de_dados_padrao = tipo_de_dados_padrao
        self.tipo_de_dados_raw = tipo_de_dados_raw
        self.tipo_de_dados_processados = tipo_de_dados_processados

    def valaidar_nomes_colunas(self, df: pd.DataFrame) -> bool:
        
        colunas_corretas = False
        # Verifica se todas as colunas estão corretas
        
        if set(self.lista_colunas_padrao) == set(df.columns):
            colunas_corretas = True
        
        return colunas_corretas

    def valaidar_tamanho_colunas(self, df: pd.DataFrame)-> bool:

        tamanho_colunas = False

        # Verifica colunas faltando ou extras
        len_colunas = len(set(self.lista_colunas_padrao)) - len(set(df.columns))

        # Verifica se não há colunas faltando nem extras
        if len_colunas == 0:
            tamanho_colunas = True
        return tamanho_colunas
    
    def verificar_tipo_dados(self, dicionario_tipo: dict)-> bool:
        
        lista_padrao = list(self.tipo_de_dados_padrao.keys())
        lista_raw = list(dicionario_tipo.keys())
        
        for i in range(len(self.tipo_de_dados_padrao)):
            tipo = self.tipo_de_dados_padrao[lista_padrao[i]] == self.tipo_de_dados_raw[lista_raw[i]]
            
            if tipo == False:
                mensagem = "Esse tipo de dado não é igual\n"\
                    f"Nome coluna: {lista_padrao[i]}, Tipo de dado: {self.tipo_de_dados_padrao[lista_padrao[i]]}\n"\
                    f"Nome coluna: {lista_raw[i]}, Tipo de dado: {self.tipo_de_dados_raw[lista_raw[i]]}\n"
                return mensagem
        return True
