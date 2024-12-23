# Autor: Gabriel Nobre
# Data: 20 de Setembro de 2024
# Descrição:
# License: 

# Imports
import datetime

import numpy            as np
import pandas           as pd
import streamlit        as st
import plotly.express   as px

from app.tratamento import tratar_dados

# Code

def filtro_maquina(df: pd.DataFrame)-> pd.DataFrame:
    filtro = st.multiselect('Máquina', sorted(set(df['maquina'].unique())))
    
    if filtro != []:
        df = df.loc[df['maquina'].isin(filtro)]
    else:
        df = df.copy()
    return df

def filtro_linha_data_e_service_name(df: pd.DataFrame)-> pd.DataFrame:
    
    linha_date_inicio, linha_date_fim, linha_service_name = st.columns((3))
    
    #try:
    with linha_date_inicio:
        filtro_data_inicio = st.date_input('Data Início',
                                            df['date'].min())
    
    with linha_date_fim:
        filtro_data_fim = st.date_input('Data Fim',
                                        df['date'].max())
        
    with linha_service_name:
        filtro_service_name = st.multiselect('Nome do Serviço',
                                sorted(set(df['service_name'].unique())))
        
        if filtro_service_name != []:
            df = df.loc[df['service_name'].isin(filtro_service_name)] 
        else:
            df = df.copy()
    
    filtro_data_inicio_a = pd.to_datetime((filtro_data_inicio - datetime.timedelta(days=1)))
    filtro_data_fim_a = pd.to_datetime((filtro_data_fim + datetime.timedelta(days=1)))
    
    df = df[(df['date'] > filtro_data_inicio_a) &\
            (df['date'] < filtro_data_fim_a)]
    
    #except:
    #    st.markdown("## Os gráficos darão erro. Conclua o filtro da data para evitar esse erro.")
        
    return df

def filtro_cost_e_quatity(df: pd.DataFrame)-> pd.DataFrame:
    
    cost, quantity = st.columns((2))
    
    with cost:
        
        cost_min = float(df['cost'].min())
        cost_max = float(df['cost'].max())
        
        filtro_cost = st.slider("Valores isolados de cada requisição",
                                min_value = cost_min,
                                max_value = cost_max,
                                value= (cost_min, cost_max))
    
    with quantity:
        quantity_min = float(df['quantity'].min())
        quantity_max = float(df['quantity'].max())
        
        filtro_quantity = st.slider("Quantidade de requisições de serviços dia",
                                min_value = quantity_min,
                                max_value = quantity_max,
                                value= (quantity_min, quantity_max))
    
    df = df[(df['cost'] > filtro_cost[0]) & (df['cost'] < filtro_cost[1])&\
            (df['quantity'] > filtro_quantity[0]) & (df['quantity'] < filtro_quantity[1])]
    
    return df

def tabela_estatistica(df: pd.DataFrame):
    
    df = df.loc[:,['date','cost','quantity']].groupby('date').sum().reset_index()
    
    df = df.select_dtypes( include = ['int64','float64'])
    
    # Medidas de tendência central - Mean, Median
    media = pd.DataFrame(df.apply(np.mean)).T
    mediana = pd.DataFrame(df.apply(np.median)).T
    
    # Medidas de Dispersão - Std, min, max, range, skew, kurtosis
    desvio_padrao = pd.DataFrame(df.apply(np.std)).T
    minimo = pd.DataFrame(df.apply(np.min)).T
    maximo = pd.DataFrame(df.apply(np.max)).T
    range = pd.DataFrame(df.apply(lambda x : x.max() - x.min())).T
    assimetria = pd.DataFrame(df.apply(lambda x : x.skew())).T
    curtosis = pd.DataFrame(df.apply(lambda x : x.kurtosis())).T
    
    estatistica = pd.concat([minimo, maximo, range, media, mediana, desvio_padrao, assimetria, curtosis]).T.reset_index()
    estatistica.columns = ['variaveis','minimo', 'maximo', 'range', 'media', 'mediana', 'desvio_padrao', 'assimetria', 'curtosis']
    
    st.header("Tabela com os valores Estatísticos das variáveis numéricas")
    st.dataframe(estatistica, use_container_width=True)
    
    
    hist_cost, hist_quant = st.columns((2))
    
    with hist_cost:
        
        fig = px.histogram(df,
                           x= 'cost',
                           title='Contagem de Custo por Dia',
                           labels={'cost': 'Custo (USD)'})
        fig.update_layout(yaxis_title="Contagem Dias")
        st.plotly_chart(fig, use_container_width=True)
    
    with hist_quant:
        
        fig2 = px.histogram(df,
                           x= 'quantity',
                           title='Contagem de Microserviços por Dia',
                           labels={'quantity': 'Microserviços'})
        fig2.update_layout(yaxis_title="Contagem Dias")
        st.plotly_chart(fig2, use_container_width=True)

def grafico1(df: pd.DataFrame):
    
    df = df.loc[:,['service_name','cost']]\
            .groupby('service_name')\
            .sum().sort_values(by='cost').reset_index()

    fig = px.histogram(
        data_frame= df,
        x = 'service_name',
        y = 'cost',
        title = 'Evolução do Custo por Serviço',
        labels={'service_name': 'Nome do Serviço', 'cost': 'Custo Total (USD)'},
    )
    st.plotly_chart(fig, use_container_width=True)
    ... # Relação custo por serviço
    
    st.markdown(f"### Valor do custo acumulado é de: {df['cost'].sum():.4f} USD")

def grafico2(df: pd.DataFrame):
    
    custo_agg, custo_servico = st.columns((2))
    
    with custo_agg: # Evolução do custo agregado ao longo do tempo
        df2 = df.loc[:,['cost','date']]\
                                .groupby(['date'])\
                                .sum().sort_values(by='date').reset_index()
        fig2 = px.line(
            data_frame= df2,
            x = 'date',
            y = 'cost',
            title= 'Evolução do custo agregado ao longo do tempo',
            labels={'date': 'Data', 'cost': 'Custo Total (USD)'}
        )
        st.plotly_chart(fig2, use_container_width=True)

    with custo_servico: # Evolução do custo por serviço ao longo do tempo
        df3 = df.loc[:,['cost','date','service_name']]\
                                .groupby(['date','service_name'])\
                                .sum().sort_values(by='date').reset_index()

        fig3 = px.line(
            data_frame= df3,
            x = 'date',
            y = 'cost',
            color='service_name',
            title= 'Evolução do custo por serviço ao longo do tempo',
            labels={'date': 'Data', 'cost': 'Custo Total (USD)'}
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown(f"### Valor do custo acumulado é de: {df['cost'].sum():.4f} USD")
    
def custo_mes(df: pd.DataFrame):
    
    df = df.loc[:,['cost','year_month']]\
            .groupby('year_month')\
            .sum().sort_values(by='year_month').reset_index()

    fig = px.line(
        data_frame= df,
        x = 'year_month',
        y = 'cost',
        title="Evolução do Custo por Mes",
        labels={'year_month': 'Ano Mês', 'cost': 'Custo Total (USD)'},
        markers=True,
    )
    st.plotly_chart(fig, use_container_width=True)
    ... # Relação custo por serviço
    
    st.markdown(f"### Valor do custo acumulado é de: {df['cost'].sum():.4f} USD")
    

def run():
    
    df = tratar_dados.df_pronto_para_consumo()
    
    df = filtro_maquina(df)
    df = filtro_linha_data_e_service_name(df)
    #df = filtro_cost_e_quatity(df)
    
    st.divider()
    grafico1(df)
    st.divider()
    
    grafico2(df)
    st.divider()
    
    custo_mes(df)
    st.divider()
    
    tabela_estatistica(df)

run()

if __name__ == '__main__':
    run()