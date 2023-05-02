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
    page_title="Nishchal Queries",
    layout="wide",
    page_icon="🤵"
)

st.title("Nishchal Queries - [PES1UG21EC169]")

st.markdown('''
    This is the Queries page by Nishchal A V [PES1UG21EC169].
''')

st.markdown('''
## Query 1
###  List the components that are limited in stock.
```sql
SELECT stock.comp_id,components.part_no,stock.normally_stocking,stock.in_stock FROM stock JOIN components ON components.comp_id=stock.comp_id AND stock.in_stock < 100000 AND (SELECT(stock.normally_stocking = 'no'));"
```
''')

cursor.execute("SELECT stock.comp_id,components.part_no,stock.normally_stocking,stock.in_stock FROM stock JOIN components ON components.comp_id=stock.comp_id AND stock.in_stock < 100000 AND (SELECT(stock.normally_stocking = 'no'));")
stock = cursor.fetchall()

stock_df = pd.DataFrame(stock, columns=["comp_id", "part_no", "normally_stocking","in_stock"])
st.dataframe(stock_df)

st.markdown('''
## Query 2
### Tabulate orders with respect to user
```sql
SELECT users.user_id,orders.order_id,orders.date_time,orders.order_type FROM users,orders WHERE orders.user_id = users.user_id AND orders.date_time < '2022-07-01 00:00:00' AND order_type='Prime';
```
''')

cursor.execute("SELECT users.user_id,orders.order_id,orders.date_time,orders.order_type FROM users,orders WHERE orders.user_id = users.user_id AND orders.date_time < '2022-07-01 00:00:00' AND order_type='Prime';")
users = cursor.fetchall()

users_df = pd.DataFrame(users, columns=["user_id", "order_id", "date_time","order_type"])
st.dataframe(users_df)

st.markdown('''
## Query 3
### Give the best price slabs with respect to component ID
```sql
SELECT price_slabs.price,price_slabs.min_qty,components.comp_id FROM price_slabs,components WHERE price < '100' AND price_slabs.min_qty < '50' AND price_slabs.comp_id=components.comp_id;
```
''')

cursor.execute("SELECT price_slabs.price,price_slabs.min_qty,components.comp_id FROM price_slabs,components WHERE price < '100' AND price_slabs.min_qty < '50' AND price_slabs.comp_id=components.comp_id;")
price_slabs = cursor.fetchall()

price_slabs_df = pd.DataFrame(price_slabs, columns=["price", "min_qty", "comp_id"])
st.dataframe(price_slabs_df)


st.markdown('''
## Query 4
### Check how many manufacturers are selling surface mount components with lifecyle of NFNPD and the components is resistor.
```sql
SELECT components.mf_id,manufacturer.name,manufacturer.location,components.lifecycle,components.category FROM manufacturer JOIN components ON components.mf_id = manufacturer.mf_id AND (SELECT(mount_type='Surface Mount')) AND (SELECT(lifecycle='InProduction')) AND components.category='Resistors';
```
''')

cursor.execute("SELECT components.mf_id,manufacturer.name,manufacturer.location,components.lifecycle,components.category FROM manufacturer JOIN components ON components.mf_id = manufacturer.mf_id AND (SELECT(mount_type='Surface Mount')) AND (SELECT(lifecycle='InProduction')) AND components.category='Resistors';")
components = cursor.fetchall()

components_df = pd.DataFrame(components, columns=["mf_id", "name", "location","lifecycle","category"])
st.dataframe(components_df)


st.markdown('''
## Query 5
### Track users who are paying through cash 
```sql
SELECT payments.method,orders.order_id,orders.user_id,payments.trnx_no,payments.amount FROM payments,orders,users WHERE orders.user_id=users.user_id AND orders.order_id=payments.order_id AND payments.method = 'cash';
```
''')

cursor.execute("SELECT payments.method,orders.order_id,orders.user_id,payments.trnx_no,payments.amount FROM payments,orders,users WHERE orders.user_id=users.user_id AND orders.order_id=payments.order_id AND payments.method = 'cash';")
payments = cursor.fetchall()

payments_df = pd.DataFrame(payments, columns=["method", "order_id", "user_id","trnx_no","amount"])
st.dataframe(payments_df)




