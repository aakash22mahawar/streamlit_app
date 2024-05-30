import streamlit as st
conn = st.connection("snowflake")
df = conn.query("select * from house_price limit 5")
st.write(df)