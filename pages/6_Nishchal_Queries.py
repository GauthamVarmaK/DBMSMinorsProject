import streamlit as st
import pandas as pd
import mysql.connector
from config import db_config

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

st.set_page_config(page_title="Nishchal Queries", layout="wide", page_icon="🐨")

st.title("Nishchal Queries - [PES1UG21EC169]")

st.markdown(
    """
    This is the Queries page by Nishchal A V [PES1UG21EC169].
"""
)

st.markdown(
    """
## Query 1
###  List the components that are limited in stock.
```sql
SELECT stock.comp_id,manufacturer.name as mf_name,components.name as comp_name,components.datasheet,components.part_no,stock.normally_stocking,stock.in_stock,price_slabs.price,min_qty 
FROM 
stock INNER JOIN components ON components.comp_id=stock.comp_id INNER JOIN manufacturer ON manufacturer.mf_id = components.mf_id JOIN price_slabs ON price_slabs.comp_id = components.comp_id AND stock.in_stock < 100000 AND (SELECT(stock.normally_stocking = 'no')) AND min_qty <= 100;
```
"""
)
cursor.execute(
    "SELECT stock.comp_id,manufacturer.name as mf_name,components.name as comp_name,components.datasheet,components.part_no,stock.normally_stocking,stock.in_stock,price_slabs.price,min_qty FROM stock INNER JOIN components ON components.comp_id=stock.comp_id INNER JOIN manufacturer ON manufacturer.mf_id = components.mf_id JOIN price_slabs ON price_slabs.comp_id = components.comp_id AND stock.in_stock < 100000 AND (SELECT(stock.normally_stocking = 'no')) AND min_qty <= 100;"
)
stock = cursor.fetchall()
stock_df = pd.DataFrame(
    stock,
    columns=[
        "comp_id",
        "mf_name",
        "comp_name",
        "datasheet",
        "part_no",
        "normally_stocking",
        "in_stock",
        "price",
        "min_qty",
    ],
)
st.dataframe(stock_df)

st.markdown(
    """
## Query 2
### Tabulate orders with respect to user order type.
```sql
SELECT users.user_id,orders.order_id,orders.date_time,orders.order_type 
FROM users,orders WHERE orders.user_id = users.user_id AND orders.date_time < '2022-07-01 00:00:00' AND order_type='Prime';
```
"""
)
cursor.execute(
    "SELECT users.user_id,orders.order_id,orders.date_time,orders.order_type FROM users,orders WHERE orders.user_id = users.user_id AND orders.date_time < '2022-07-01 00:00:00' AND order_type='Prime';"
)
users = cursor.fetchall()
users_df = pd.DataFrame(
    users, columns=["user_id", "order_id", "date_time", "order_type"]
)
st.dataframe(users_df)

st.markdown(
    """
## Query 3
### Give the best price slabs with respect to components 
```sql
SELECT components.comp_id,price_slabs.min_qty,price_slabs.price,price_slabs.price * price_slabs.min_qty total_price,components.name 
FROM price_slabs JOIN components ON price_slabs.comp_id=components.comp_id WHERE price <= 3 AND min_qty <= 100;
```
"""
)
cursor.execute(
    "SELECT components.comp_id,price_slabs.min_qty,price_slabs.price,price_slabs.price * price_slabs.min_qty total_price,components.name FROM price_slabs JOIN components ON price_slabs.comp_id=components.comp_id WHERE price <= 3 AND min_qty <= 100;"
)
price_slabs = cursor.fetchall()
price_slabs_df = pd.DataFrame(
    price_slabs, columns=["comp_id", "min_qty", "price", "total_price", "name"]
)
st.dataframe(price_slabs_df)


st.markdown(
    """
## Query 4
### Check how many manufacturers are selling surface mount components with lifecyle of NFNPD and the components is resistor.
```sql
SELECT components.mf_id,manufacturer.name,manufacturer.location,components.lifecycle,components.category 
FROM manufacturer JOIN components ON components.mf_id = manufacturer.mf_id AND (SELECT(mount_type='Surface Mount')) AND (SELECT(lifecycle='InProduction')) AND components.category='Resistors';
```
"""
)
cursor.execute(
    "SELECT components.mf_id,manufacturer.name,manufacturer.location,components.lifecycle,components.category FROM manufacturer JOIN components ON components.mf_id = manufacturer.mf_id AND (SELECT(mount_type='Surface Mount')) AND (SELECT(lifecycle='InProduction')) AND components.category='Resistors';"
)
components = cursor.fetchall()
components_df = pd.DataFrame(
    components, columns=["mf_id", "name", "location", "lifecycle", "category"]
)
st.dataframe(components_df)


st.markdown(
    """
## Query 5
### Track users who are paying through cash 
```sql
SELECT payments.method,orders.order_id,orders.user_id,users.name,phone_number,address,city,state,pincode,payments.trnx_no,payments.amount 
FROM payments,orders,users where orders.user_id=users.user_id AND orders.order_id=payments.order_id AND payments.method = 'cash';
```
"""
)
cursor.execute(
    "SELECT payments.method,orders.order_id,orders.user_id,users.name,phone_number,address,city,state,pincode,payments.trnx_no,payments.amount FROM payments,orders,users where orders.user_id=users.user_id AND orders.order_id=payments.order_id AND payments.method = 'cash';"
)
payments = cursor.fetchall()
payments_df = pd.DataFrame(
    payments,
    columns=[
        "method",
        "order_id",
        "user_id",
        "name",
        "phone_number",
        "address",
        "city",
        "state",
        "pincode",
        "trnx_no",
        "amount",
    ],
)
st.dataframe(payments_df)

cursor.close()
db.close()
