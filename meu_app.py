import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
# %matplotlib inline
st.set_page_config(page_title='TCC Thiago')

with st.container():
    st.subheader('ANÁLISE DESCRITIVA E EXPLORATÓRIA DOS ÍNDICES ANUAIS DE PM2,5     DISPONIBILIZADOS EM RELATÓRIO DA ORGANIZAÇÃO MUNDIAL DE SAÚDE')
    st.title('Leitura do DataFrame')
    st.write('Informações sobre o DataFrame ao longo dos anos de 2010 a 2019')
    df = pd.read_csv("44a688d7-8cd5-4c31-baa5-ec9fee468092.csv")
    df

with st.container():
    st.write('---')
    st.title('Preparação de dados')
    st.write('Dados nulos')
    st.write(df.isnull().any())

with st.container():
    st.write('---')
    st.write('Verificação de dados nulos nas linhas')
    st.write(df[df.isnull().T.any()])

with st.container():
    st.write('---')
    st.write('Contagem do número de valores ausentes em cada coluna do DataFrame')
    st.write(df.isnull().sum())

with st.container():
    st.write('---')
    st.write('Remoção das colunas com dados nulos/faltantes')
    df.dropna(axis=1, how='all', inplace=True)
    df

with st.container():
    st.write('---')
    st.write('Verificação da remoção das colunas que continham dados nulos')
    st.write(df.isnull().sum())

with st.container():
    st.write('---')
    st.title('Outliers')
    st.write('gráfico de boxplot da coluna numérica FactValueNumeric')
#     df = px.data.iris()
#     fig = px.scatter(
#     df,
#     x="FactValueNumeric",
#     y="",
#     color="sepal_length",
#     color_continuous_scale="reds",
# )
#     tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
# with tab1:
#     st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# with tab2:
#     st.plotly_chart(fig, theme=None, use_container_width=True)
    
with st.container():
    st.write('---')
    st.write('Verificação do valor mínimo de PM2,5')
    st.write(df.FactValueNumeric.min())

with st.container():
    st.write('---')
    st.write('Verificação do valor máximo de PM2,5')
    st.write(df.FactValueNumeric.max())

with st.container():
    st.write('---')
    st.title('Análise')
    st.write('Total de PM2,5 por ano no Brasil')
    x = df[(df['Dim1']=='Total') & (df['Location']=='Brazil')]['Period']
    y = df[(df['Dim1']=='Total') & (df['Location']=='Brazil')]['FactValueNumeric']
    plt.bar(x,y)
    plt.show()
    # st.bar_chart(df, x='Dim1'=='Total' & 'Location'=='Brazil'['Period'], y='Dim1'=='Total' & 'Location'=='Brazil'['FactValueNumeric'])
    # st.bar_chart(df, x='Dim1'=='Total'and 'Location'=='Brazil'['Period'], y='Dim1'=='Total'and 'Location'=='Brazil'['FactValueNumeric'])
   