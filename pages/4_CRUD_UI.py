import mysql.connector
import streamlit as st
import pandas as pd

db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="winterfox@2003",  
    database="electronics_store"
)

cursor = db.cursor()

st.title("Store Details")

cursor.execute("SELECT * FROM Components")
st.dataframe(pd.DataFrame(cursor.fetchall(),columns=("Component ID","Description","Part no","Manufacurer ID","Name","Life Cycle","Category","Datasheet","ROHS","Mount Type")))

st.subheader("Add a new component")

comp_id = st.number_input("comp_id",key="comp_id_create")
desc = st.text_input("desc",key="desc_create")
part_no = st.text_input("part_no",key="part_no_create")
mf_id = st.text_input("mf_id",key="mf_id_create")
name = st.text_input("name",key="name_create")
life_cycle = st.text_input("life_cycle",key="life_cycle_create")
category = st.text_input("category",key="category_create")
datasheet = st.text_input("datasheet",key="datasheet_create")
rohs = st.text_input("rohs",key="rohs_create")
mount = st.text_input("mount",key="mount_create")

if st.button("Add Component"):
    cursor.execute("INSERT INTO Components VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (comp_id, desc, part_no, mf_id, name, life_cycle, category, datasheet, rohs, mount))
    db.commit()
    st.success("Component added successfully")
st.subheader("Update a Component")

cursor.close()
db.close()