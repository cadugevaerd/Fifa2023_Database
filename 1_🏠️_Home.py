import streamlit as st
#import webbrowser
import urllib
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Fifa23 Database",
    layout = "wide",
)

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv")
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] != 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state['data'] = df_data

#st.dataframe(df_data.columns)


st.markdown("# Fifa23 Official Database")


link = '[Acesse os dados no Kaggle!](https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data)'
st.markdown(link, unsafe_allow_html=True)
    #webbrowser.open("https://www.kaggle.com/datasets/andrewsosanya/fifa-23-dataset?select=CLEAN_FIFA23_official_data.csv")
    
    
st.markdown("""
            O Conjunto de Dados de Jogadores de Futebol de 2017 a 2023
            fornece informações abrangentes sobre jogadores de futebol profissional.
            O conjunto de dados contém uma ampla gama de atributos,
            incluindo dados demográficos dos jogadores, características físicas,
            estatísticas de jogo, detalhes de contratos e afiliações a clubes.
            Com mais de 17.000 registros,
            este conjunto de dados oferece um recurso valioso para analistas
            de futebol, pesquisadores e entusiastas interessados em explorar
            vários aspectos do mundo do futebol, pois permite estudar atributos
            de jogadores, métricas de desempenho, valoração de mercado,
            análise de clubes, posicionamento de jogadores e desenvolvimento
            de jogadores ao longo do tempo.
            """)