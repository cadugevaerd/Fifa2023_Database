import streamlit as st

st.set_page_config(
    page_title="Players Fifa 2023",
    layout = "wide",
)

df_data = st.session_state['data']

clubes = df_data["Club"].unique()
clube = st.sidebar.selectbox("Clube:", clubes)
df_players = df_data[df_data["Club"] == clube]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador:", players)
stats = df_players[df_players["Name"] == player]
st.image(stats["Photo"].values[0])
st.title(stats["Name"].values[0])

st.markdown(f"**Clube:** {stats['Club'].values[0]}")
st.markdown(f"**Posição:** {stats['Position'].values[0]}")
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {stats['Age'].values[0]}")
col2.markdown(f"**Altura:** {stats['Height(cm.)'].values[0] / 100}")
col3.markdown(f"**Peso:** {stats['Weight(lbs.)'].values[0]* 0.453:.2f}")
st.divider()

st.subheader(f"Overall: {stats['Overall'].values[0]}")
st.progress(int(stats['Overall'].values[0]))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="**Valor de Mercado:**",value= f"£ {stats['Value(£)'].values[0]:,}")
col2.metric(label="**Remuneração Salarial:**",value= f"£ {stats['Wage(£)'].values[0]:,}")
col3.metric(label="**Clausula de Rescisão:**",value= f"£ {stats['Release Clause(£)'].values[0]:,}")
#st.write(clube)