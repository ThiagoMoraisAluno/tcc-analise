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
    fig = plt.figure(figsize=[10,5])
    plt.boxplot(df['FactValueNumeric'])
    plt.xticks([1],['FactValueNumeric'])
    st.pyplot(fig)
    
with st.container():
    st.write('---')
    st.write('Verificação do valor mínimo de PM2,5')
    st.write(df.FactValueNumeric.min())

with st.container():
    st.write('---')
    st.write('Verificação do valor máximo de PM2,5')
    st.write(df.FactValueNumeric.max())

with st.container(): #VER COM BRUNO
    st.write('---')
    st.write('PM2.5 ao longo do tempo no Brasil')
    df_brazil = df[(df['Location'] == 'Brazil') & (df.Dim1 == 'Total')]
    x = df_brazil.Period
    y = df_brazil.FactValueNumeric
    fig = plt.figure(figsize=[10,5])
    plt.plot(x,y)
    plt.title('PM2.5 ao longo do tempo no Brasil')
    plt.xlabel('Anos')
    plt.ylabel('PM2.5')
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('índices totais de PM2.5 por região')
    x = df[(df['Dim1']=='Total') & (df['Location']=='Brazil')]['Period']
    y_total = df[(df['Dim1']=='Total') & (df['Location']=='Brazil')]['FactValueNumeric']
    y_rural = df[(df['Dim1']=='Rural') & (df['Location']=='Brazil')]['FactValueNumeric']
    y_cities = df[(df['Dim1']=='Cities') & (df['Location']=='Brazil')]['FactValueNumeric']
    y_towns = df[(df['Dim1']=='Towns') & (df['Location']=='Brazil')]['FactValueNumeric']
    y_urban = df[(df['Dim1']=='Urban') & (df['Location']=='Brazil')]['FactValueNumeric']
    fig = plt.figure(figsize=([10,5]))
    plt.plot(x,y_total, label="Total")
    plt.plot(x,y_rural, label="Rural")
    plt.plot(x,y_cities, label="Cities")
    plt.plot(x,y_towns, label="Towns")
    plt.plot(x,y_urban, label="Urban")
    plt.legend()
    plt.legend()
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Top 5 Países com Maiores Índices de PM2.5')
    
    qtd = st.selectbox("Selecione a quantidade", ["5", "10", "15"], key="selectbox_paises")
    qtd_maior_paises = int(qtd)
    if qtd_maior_paises==5:
        x = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(5).index
        y = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(5).values
        fig = plt.figure(figsize=([10,5]))
    elif qtd_maior_paises==10:
        x = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(10).index
        y = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(10).values
        fig = plt.figure(figsize=([13,5]))
    elif qtd_maior_paises==15:
        x = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(15).index
        y = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(15).values
        fig = plt.figure(figsize=([25,5]))
    
    plt.bar(x,y)
    plt.ylabel('Média de PM2,5')
    plt.xticks(rotation = 45)
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Top 5 Países com menores Índices de PM2.5')
    qtd = st.selectbox("Selecione a quantidade", ["5", "10", "15"], key="selectbox_paises2")
    qtd_maior_paises = int(qtd)
    if qtd_maior_paises==5:
        x = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(5).index
        y = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(5).values
        fig = plt.figure(figsize=([10,5]))
    elif qtd_maior_paises==10:
        x = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(10).index
        y = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(10).values
        fig = plt.figure(figsize=([13,5]))
    elif qtd_maior_paises==15:
        x = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(15).index
        y = df[df.Dim1 == 'Total'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(15).values
        fig = plt.figure(figsize=([25,5]))
    
    plt.bar(x,y)
    plt.ylabel('Média de PM2,5')
    plt.xticks(rotation = 45)
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Top 5 piores cidades de países para se viver')
    qtd = st.selectbox("Selecione a quantidade", ["5", "10", "15"], key="selectbox_paises3")
    qtd_maior_paises = int(qtd)
    if qtd_maior_paises==5:
        x = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(5).index
        y = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(5).values
        fig = plt.figure(figsize=([10,5]))
    elif qtd_maior_paises==10:
        x = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(10).index
        y = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(10).values
        fig = plt.figure(figsize=([13,5]))
    elif qtd_maior_paises==15:
        x = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(15).index
        y = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(15).values
        fig = plt.figure(figsize=([25,5]))
    
    plt.bar(x,y)
    plt.ylabel('Média de PM2,5')
    plt.xticks(rotation = 45)
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Top 5 melhores cidades de países para se viver')
    qtd = st.selectbox("Selecione a quantidade", ["5", "10", "15"], key="selectbox_paises4")
    qtd_maior_paises = int(qtd)
    if qtd_maior_paises==5:
        x = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(5).index
        y = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(5).values
        fig = plt.figure(figsize=([10,5]))
    elif qtd_maior_paises==10:
        x = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(10).index
        y = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(10).values
        fig = plt.figure(figsize=([13,5]))
    elif qtd_maior_paises==15:
        x = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(15).index
        y = df[df.Dim1 == 'Cities'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(15).values
        fig = plt.figure(figsize=([25,5]))
    
    plt.bar(x,y)
    plt.ylabel('Média de PM2,5')
    plt.xticks(rotation = 45)
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Top 5 piores regiões rurais de países para se viver')
    qtd = st.selectbox("Selecione a quantidade", ["5", "10", "15"], key="selectbox_paises5")
    qtd_maior_paises = int(qtd)
    if qtd_maior_paises==5:
        x = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(5).index
        y = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(5).values
        fig = plt.figure(figsize=([10,5]))
    elif qtd_maior_paises==10:
        x = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(10).index
        y = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(10).values
        fig = plt.figure(figsize=([13,5]))
    elif qtd_maior_paises==15:
        x = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(15).index
        y = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(15).values
        fig = plt.figure(figsize=([25,5]))
    
    plt.bar(x,y)
    plt.ylabel('Média de PM2,5')
    plt.xticks(rotation = 45)
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Top 5 melhores regiões rurais de países para se viver')
    qtd = st.selectbox("Selecione a quantidade", ["5", "10", "15"], key="selectbox_paises6")
    qtd_maior_paises = int(qtd)
    if qtd_maior_paises==5:
        x = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(5).index
        y = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(5).values
        fig = plt.figure(figsize=([10,5]))
    elif qtd_maior_paises==10:
        x = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(10).index
        y = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(10).values
        fig = plt.figure(figsize=([13,5]))
    elif qtd_maior_paises==15:
        x = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(15).index
        y = df[df.Dim1 == 'Rural'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(15).values
        fig = plt.figure(figsize=([25,5]))
    
    plt.bar(x,y)
    plt.ylabel('Média de PM2,5')
    plt.xticks(rotation = 45)
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Top 5 piores cidades pequenas de países para se viver')
    qtd = st.selectbox("Selecione a quantidade", ["5", "10", "15"], key="selectbox_paises7")
    qtd_maior_paises = int(qtd)
    if qtd_maior_paises==5:
        x = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(5).index
        y = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(5).values
        fig = plt.figure(figsize=([10,5]))
    elif qtd_maior_paises==10:
        x = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(10).index
        y = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(10).values
        fig = plt.figure(figsize=([13,5]))
    elif qtd_maior_paises==15:
        x = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(15).index
        y = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(15).values
        fig = plt.figure(figsize=([25,5]))
    
    plt.bar(x,y)
    plt.ylabel('Média de PM2,5')
    plt.xticks(rotation = 45)
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Top 5 melhores cidades pequenas de países para se viver')
    qtd = st.selectbox("Selecione a quantidade", ["5", "10", "15"], key="selectbox_paises8")
    qtd_maior_paises = int(qtd)
    if qtd_maior_paises==5:
        x = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(5).index
        y = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(5).values
        fig = plt.figure(figsize=([10,5]))
    elif qtd_maior_paises==10:
        x = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(10).index
        y = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(10).values
        fig = plt.figure(figsize=([13,5]))
    elif qtd_maior_paises==15:
        x = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(15).index
        y = df[df.Dim1 == 'Towns'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(15).values
        fig = plt.figure(figsize=([25,5]))
    
    plt.bar(x,y)
    plt.ylabel('Média de PM2,5')
    plt.xticks(rotation = 45)
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Top 5 piores regiões urbanas de países para se viver')
    qtd = st.selectbox("Selecione a quantidade", ["5", "10", "15"], key="selectbox_paises9")
    qtd_maior_paises = int(qtd)
    if qtd_maior_paises==5:
        x = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(5).index
        y = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(5).values
        fig = plt.figure(figsize=([10,5]))
    elif qtd_maior_paises==10:
        x = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(10).index
        y = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(10).values
        fig = plt.figure(figsize=([13,5]))
    elif qtd_maior_paises==15:
        x = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(15).index
        y = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=False).head(15).values
        fig = plt.figure(figsize=([25,5]))
    
    plt.bar(x,y)
    plt.ylabel('Média de PM2,5')
    plt.xticks(rotation = 45)
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Top 5 melhores regiões urbanas de países para se viver')
    qtd = st.selectbox("Selecione a quantidade", ["5", "10", "15"], key="selectbox_paises10")
    qtd_maior_paises = int(qtd)
    if qtd_maior_paises==5:
        x = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(5).index
        y = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(5).values
        fig = plt.figure(figsize=([10,5]))
    elif qtd_maior_paises==10:
        x = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(10).index
        y = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(10).values
        fig = plt.figure(figsize=([13,5]))
    elif qtd_maior_paises==15:
        x = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(15).index
        y = df[df.Dim1 == 'Urban'].groupby('Location')['FactValueNumeric'].mean().sort_values(ascending=True).head(15).values
        fig = plt.figure(figsize=([25,5]))
    
    plt.bar(x,y)
    plt.ylabel('Média de PM2,5')
    plt.xticks(rotation = 45)
    st.pyplot(fig)

with st.container():
    st.write('---')
    st.write('Média de PM2.5 do Brasil')
    st.write(df_brazil.FactValueNumeric.mean())

with st.container():
    st.write('---')
    st.write('Média Total de PM2.5 de todos os países')
    st.write(df[df.Dim1 == 'Total'].FactValueNumeric.mean())

with st.container():
    st.write('---')
    st.write('Desvio Padrão')
    st.write(df[df.Dim1 == 'Total'].FactValueNumeric.std())


    
   