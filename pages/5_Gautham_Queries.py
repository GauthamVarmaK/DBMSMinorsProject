import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="electronics_store"
)

cursor = db.cursor()

st.set_page_config(
    page_title="Gautham Queries",
    layout="wide",
    page_icon="🤵"
)

st.title("Gautham Queries - [PES1UG21EC102]")

st.markdown('''
    This is the Queries page by Gautham Varma K [PES1UG21EC102].
''')

st.markdown('''
## Query 1
### Display the top 20 orders today sorted by price.
```sql
SELECT * FROM orders ORDER BY price DESC LIMIT 20;
```
''')

cursor.execute("SELECT * FROM orders ORDER BY price DESC LIMIT 20")
orders = cursor.fetchall()

orders_df = pd.DataFrame(orders, columns=["order_id", "user_id", "comp_id", "quantity", "price", "order_date"])
st.dataframe(orders_df)

st.markdown('''
## Query 2
### Find all resistors that are of 220 Ohms that are in Production
```sql
SELECT * FROM components WHERE (comp_id IN (SELECT * from description WHERE param="resistance")) AND lifecycle = 'Production';
```
''')

cursor.execute("SELECT * FROM components WHERE (comp_id IN (SELECT * from description WHERE param='resistance')) AND lifecycle = 'Production'")
components = cursor.fetchall()

components_df = pd.DataFrame(components, columns=["comp_id", "description", "part_no", "mf_id", "name", "lifecycle", "category", "datasheet", "rohs", "mount_type"])
st.dataframe(components_df)
