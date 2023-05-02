import streamlit as st

st.set_page_config(page_title="ER Diagram", page_icon="♦️", layout="wide")

st.title("ER Diagram")
st.markdown(
    """
This is the ER Diagram of the database. 
"""
)
st.image("images/ERDiagram.png", use_column_width=True)
