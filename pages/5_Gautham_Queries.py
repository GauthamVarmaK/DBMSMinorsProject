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

st.title("Gautham's Queries")

st.markdown('''
    This is the Queries page by Gautham Varma K [PES1UG21EC102].
''')

st.markdown('''
## Query 1
### Display the top 20 orders today sorted by price.
```sql
SELECT orders.order_id,user_id,date_time,order_type,pm.amount FROM orders,payments as pm WHERE order_id=pm.order_id ORDER BY pm.amount DESC LIMIT 20;
```
''')

cursor.execute("SELECT orders.order_id,user_id,date_time,order_type,pm.amount FROM orders,payments as pm WHERE orders.order_id=pm.order_id ORDER BY pm.amount DESC LIMIT 20;")
orders = cursor.fetchall()

orders_df = pd.DataFrame(orders, columns=["order_id", "user_id", "datetime","order_type", "price"])
st.dataframe(orders_df)

st.markdown('''
## Query 2
### Find all resistors that are of 220 Ohms that are in Production
```sql
SELECT * FROM components WHERE (comp_id IN (SELECT comp_id from description WHERE param='Resistance' AND value='220 Ohms')) AND lifecycle = 'InProduction';
```
''')

cursor.execute("SELECT * FROM components WHERE (comp_id IN (SELECT comp_id from description WHERE param='Resistance' AND value='220 Ohms')) AND lifecycle = 'InProduction';")
components = cursor.fetchall()

components_df = pd.DataFrame(components, columns=["comp_id", "description", "part_no", "mf_id", "name", "lifecycle", "category", "datasheet", "rohs", "mount_type"])
st.dataframe(components_df)

st.markdown('''
## Query 3
### List up to 50 components that have less than 50 pieces in stock but have a lead time of greater than 8 weeks.
```sql
SELECT components.comp_id,components.name,components.part_no,components.mf_id,components.lifecycle,components.category,components.datasheet,components.rohs,components.mount_type,stock.in_stock,stock.location,stock.lead_time 
FROM components,stock 
WHERE components.comp_id=stock.comp_id AND stock.in_stock<50 AND stock.lead_time>8 LIMIT 50;
```
''')

cursor.execute("SELECT components.comp_id,components.name,components.part_no,components.mf_id,components.lifecycle,components.category,components.datasheet,components.rohs,components.mount_type,stock.in_stock,stock.lead_time,stock.normally_stocking FROM components,stock WHERE components.comp_id=stock.comp_id AND stock.in_stock<50 AND stock.lead_time>8 LIMIT 50;")
components = cursor.fetchall()

components_df = pd.DataFrame(components, columns=["comp_id", "name", "part_no", "mf_id", "lifecycle", "category", "datasheet", "rohs", "mount_type", "quantity", "lead_time", "normally_stocking"])
st.dataframe(components_df)

st.markdown('''
## Query 4
### List the top 10 products sold by any manufacturer based on the total number of pieces sold.
```sql
-- TODO
```
''')

cursor.execute("SELECT 'Hello World!';")
components = cursor.fetchall()

components_df = pd.DataFrame(components, columns=["TODO"])
st.dataframe(components_df)

st.markdown('''
## Query 5
### Only list components that are RoHS compliant sold by a certain manufacturer
```sql
SELECT components.comp_id,components.name,components.part_no,components.mf_id,components.lifecycle,components.category,components.datasheet,components.rohs,components.mount_type FROM components WHERE components.rohs='Compliant' AND components.mf_id='1';
```
''')

cursor.execute("SELECT components.comp_id,components.name,components.part_no,components.mf_id,components.lifecycle,components.category,components.datasheet,components.rohs,components.mount_type FROM components WHERE components.rohs='Compliant' AND components.mf_id='1';")
components = cursor.fetchall()

components_df = pd.DataFrame(components, columns=["comp_id", "name", "part_no", "mf_id", "lifecycle", "category", "datasheet", "rohs", "mount_type"])
st.dataframe(components_df)

st.markdown('''
## Query 6
### List orders whose status is Not shipped if placed before a week
```sql
SELECT * FROM orders WHERE status='ToBeShipped' AND date_time < DATE(DATE_SUB(NOW(), INTERVAL 1 WEEK));
```
''')

cursor.execute("SELECT * FROM orders WHERE status='ToBeShipped' AND date_time < DATE(DATE_SUB(NOW(), INTERVAL 1 WEEK));")
orders = cursor.fetchall()

orders_df = pd.DataFrame(orders, columns=["order_id", "user_id", "date_time", "order_type","status"])
st.dataframe(orders_df)

st.markdown('''
## Query 7
### Find the Most commonly used mode of payment
```sql
SELECT method as payment_mode,COUNT(method) FROM payments GROUP BY payment_mode ORDER BY COUNT(payment_mode) DESC LIMIT 1;
```
''')

cursor.execute("SELECT method as payment_mode,COUNT(method) FROM payments GROUP BY payment_mode ORDER BY COUNT(payment_mode) DESC LIMIT 1;")
payments = cursor.fetchall()

payments_df = pd.DataFrame(payments, columns=["payment_mode", "count"])
st.dataframe(payments_df)

st.markdown('''
## Query 8
### Select resistors of 45 Ohms components that are 'InProduction' and have in_stock of greater than 400
```sql
SELECT components.comp_id,components.name,components.part_no,components.mf_id,components.lifecycle,components.category,components.datasheet,components.rohs,components.mount_type,stock.in_stock,stock.lead_time
FROM components,stock,description
WHERE components.comp_id=stock.comp_id AND components.comp_id=description.comp_id AND description.param='Resistance' AND description.value='45 Ohms' AND components.lifecycle='InProduction' AND stock.in_Stock>400;
```
''')

cursor.execute("SELECT components.comp_id,components.name,components.part_no,components.mf_id,components.lifecycle,components.category,components.datasheet,components.rohs,components.mount_type,stock.in_stock,stock.lead_time FROM components,stock,description WHERE components.comp_id=stock.comp_id AND components.comp_id=description.comp_id AND description.param='Resistance' AND description.value='45 Ohms' AND components.lifecycle='InProduction' AND stock.in_stock>400;")
components = cursor.fetchall()

components_df = pd.DataFrame(components, columns=["comp_id", "name", "part_no", "mf_id", "lifecycle", "category", "datasheet", "rohs", "mount_type", "quantity", "lead_time"])
st.dataframe(components_df)
