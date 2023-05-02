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
    page_title="Mrinal Queries",
    layout="wide",
    page_icon="🫥"
)

st.title("Mrinal's Queries")

st.markdown('''
    This is the Queries page by Mrinal [PES1UG21EC152].
''')

st.markdown('''
## Query 1
### Show the number of LEDs components that are in production 
sql:
SELECT COUNT(category) as count  FROM components WHERE category='LEDS' AND lifecycle='InProduction';
''')

cursor.execute("SELECT COUNT(category) as count  FROM components WHERE category='LEDS' AND lifecycle='InProduction';")
orders = cursor.fetchall()

orders_df = pd.DataFrame(orders, columns=["Count"])
st.dataframe(orders_df)


st.markdown('''
## Query 2
### Select the cheapest component(using comp_ID)
sql:
SELECT comp_id FROM price_slabs WHERE price=(SELECT MIN(price) FROM price_slabs);
''')

cursor.execute("SELECT comp_id FROM price_slabs WHERE price=(SELECT MIN(price) FROM price_slabs);")
orders = cursor.fetchall()

orders_df = pd.DataFrame(orders, columns=["Count"])
st.dataframe(orders_df)


st.markdown('''
## Query 3
###  Find the name of a newer user, whose order has to be shipped and find their mode of payment
sql:
SELECT users.name,payments.method FROM users,orders,payments WHERE users.user_since=(SELECT max(user_since) FROM users) AND users.user_ID=orders.user_ID AND orders.order_ID=payments.order_ID AND orders.status='tobeshipped';

''')

cursor.execute("SELECT users.name,payments.method FROM users,orders,payments WHERE users.user_since=(SELECT max(user_since) FROM users) AND users.user_ID=orders.user_ID AND orders.order_ID=payments.order_ID AND orders.status='tobeshipped';")
orders = cursor.fetchall()
orders_df = pd.DataFrame(orders, columns=["Name","Method"])
st.dataframe(orders_df)

st.markdown('''
## Query 4
### Select users who has been a user for a long time and find their most use method of payments
sql:
SELECT users.user_ID,users.name,payments.method FROM users,orders,payments WHERE user_since=(SELECT MIN(user_since) FROM users) AND users.user_ID=orders.user_ID AND orders.order_ID=payments.order_ID AND payments.method=(SELECT payments.method FROM payments WHERE payments.order_ID=orders.order_ID GROUP BY payments.method LIMIT 1);

''')

cursor.execute("SELECT users.user_ID,users.name,payments.method FROM users,orders,payments WHERE user_since=(SELECT MIN(user_since) FROM users) AND users.user_ID=orders.user_ID AND orders.order_ID=payments.order_ID AND payments.method=(SELECT payments.method FROM payments WHERE payments.order_ID=orders.order_ID GROUP BY payments.method LIMIT 1);")
orders = cursor.fetchall()

orders_df = pd.DataFrame(orders, columns=["User_ID","Name","Method"])
st.dataframe(orders_df)



st.markdown('''
## Query 5
### Find the name of a user who has bought a component of mount_type=”surface mount”
sql:
SELECT users.name FROM users,components,orders,order_comp WHERE users.user_ID=orders.user_ID AND orders.order_ID=order_comp.order_ID AND order_comp.comp_ID=components.comp_ID AND components.mount_type="Surface Mount";
''')

cursor.execute("SELECT users.name FROM users,components,orders,order_comp WHERE users.user_ID=orders.user_ID AND orders.order_ID=order_comp.order_ID AND order_comp.comp_ID=components.comp_ID AND components.mount_type='Surface Mount';")
orders = cursor.fetchall()

orders_df = pd.DataFrame(orders, columns=["NAME"])
st.dataframe(orders_df)




