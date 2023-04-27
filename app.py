import mysql.connector
import streamlit as st
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="electronics_store"
)

cursor = db.cursor()

st.set_page_config(
    page_title="Overview",
    layout="wide",
    page_icon="👋",
)

st.write("# Electronic Components Marketplace 👋")

st.markdown(
"""
    Project made by:
    | SRN | Name |
    | --- | --- |
    | PES1UG21EC102 | Gautham Varma K |
    | PES1UG21EC169 | Nishchal A V |
    | PES1UG21EC164 | Nikhil  R |
    | PES1UG21EC152 | Mrinal Pradeep |
"""
)