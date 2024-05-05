import streamlit as st
st.set_page_config(
    page_title="Teams Fifa 2023",
    layout = "wide",
)

df_data = st.session_state['data']

clubes = df_data["Club"].unique()
clube = st.sidebar.selectbox("Clube:", clubes)

df_club = df_data[df_data["Club"] == clube]
df_club.set_index("Name", inplace = True)
st.image(df_club["Club Logo"].values[0])
st.markdown(f"## {clube}")
columns = ["Age","Photo","Flag","Overall","Value(£)",'Wage(£)','Joined','Height(cm.)','Weight(lbs.)'
           ,'Contract Valid Until','Release Clause(£)']
df_filtered = df_club[columns]
st.dataframe(df_filtered,
             column_config={
                 'Overall': st.column_config.ProgressColumn(
                     "Overall",format="%d",min_value=0, max_value=100),
                 'Wage(£)': st.column_config.ProgressColumn(
                     format="£%f",min_value=0, max_value=df_filtered['Wage(£)'].max()),
                 'Photo': st.column_config.ImageColumn(),
                 'Flag' : st.column_config.ImageColumn("Country")
                 
                 
             })