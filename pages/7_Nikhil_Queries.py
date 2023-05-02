import streamlit as st
import pandas as pd
import mysql.connector
from config import db_config

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

st.set_page_config(page_title="Nikhil Queries", layout="wide", page_icon="🤵")

st.title("Nikhil Queries - [PES1UG21EC164]")

st.markdown(
    """
    This is the Queries page by Nikhil R [PES1UG21EC164].
"""
)

st.markdown(
    """
## Query 1
###  Select all components whose lead time is minimum from table Stock
```sql
SELECT * FROM stock WHERE lead_time<1;
```
"""
)
cursor.execute("SELECT * FROM stock WHERE lead_time<1;")
stock = cursor.fetchall()
stock_df = pd.DataFrame(
    stock, columns=["comp_id", "in_stock", "lead_time", "normally_stocking"]
)
st.dataframe(stock_df)

st.markdown(
    """
## Query 2
### Retrieve all details from the table price_slabs where the price is unusually high
```sql
SELECT * FROM price_slabs WHERE price_slabs.price > (SELECT AVG(price) FROM price_slabs);
```
"""
)
cursor.execute(
    "SELECT * FROM price_slabs WHERE price_slabs.price > (SELECT AVG(price) FROM price_slabs);"
)
price_slabs = cursor.fetchall()
price_slabs_df = pd.DataFrame(price_slabs, columns=["comp_id", "min_qty", "price"])
st.dataframe(price_slabs_df)

st.markdown(
    """
## Query 3
### Display those locations which have more than one manufacturer stationed.
```sql
SELECT location, count(*) as num FROM manufacturer GROUP BY(location) Having count(*)>1;
```
"""
)
cursor.execute(
    "SELECT location, count(*) as num FROM manufacturer GROUP BY(location) Having count(*)>1;"
)
manufacturer = cursor.fetchall()
manufacturer_df = pd.DataFrame(manufacturer, columns=["location", "num"])
st.dataframe(manufacturer_df)


st.markdown(
    """
## Query 4
### Display the user_id, name  and phone number of customers whose order status is Missing
```sql
SELECT users.user_id, users.name, users.phone_number, orders.status FROM users LEFT JOIN orders ON users.user_id=orders.user_id and orders.status='Missing';
```
"""
)
cursor.execute(
    "SELECT users.user_id, users.name, users.phone_number, orders.status FROM users LEFT JOIN orders ON users.user_id=orders.user_id and orders.status='Missing';"
)
components = cursor.fetchall()
components_df = pd.DataFrame(
    components, columns=["user)id", "name", "phone_number", "status"]
)
st.dataframe(components_df)


st.markdown(
    """
## Query 5
### Display the user id of those users who have made payments larger than 20000.
```sql
SELECT users.user_id, orders.order_id, payments.trnx_no, payments.amount FROM users INNER JOIN orders ON users.user_id=orders.user_id INNER JOIN payments ON payments.order_id=orders.order_id where payments.amount>20000;
```
"""
)
cursor.execute(
    "SELECT users.user_id, orders.order_id, payments.trnx_no, payments.amount FROM users INNER JOIN orders ON users.user_id=orders.user_id INNER JOIN payments ON payments.order_id=orders.order_id where payments.amount>20000;"
)
payments = cursor.fetchall()
payments_df = pd.DataFrame(
    payments, columns=["user_id", "order_id", "trnx_no", "amount"]
)
st.dataframe(payments_df)

cursor.close()
db.close()
