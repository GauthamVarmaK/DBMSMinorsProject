import streamlit as st
import pandas as pd
import mysql.connector
from config import db_config

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

st.set_page_config(page_title="Database Overview", page_icon="📊", layout="wide")

st.title("Database Overview")
st.markdown(
    """
This is the overview of the database.
"""
)

st.markdown(
    """
```sql
CREATE DATABASE electronics_store;

USE electronics_store;

CREATE TABLE users(
   user_id VARCHAR(50) PRIMARY KEY,
   name VARCHAR(50),
   email_id VARCHAR(50) CHECK (email_id LIKE '%@%.%'),
   phone_number VARCHAR(50) CHECK (LENGTH(phone_number) = 10),
   dob DATE,
   user_since DATE,
   address VARCHAR(100),
   city VARCHAR(50),
   state VARCHAR(50),
   pincode INT
);

CREATE TABLE manufacturer(
   mf_id VARCHAR(50) PRIMARY KEY,
   name VARCHAR(50) NOT NULL,
   description VARCHAR(100),
   location VARCHAR(50)
);

CREATE TABLE components(
   comp_id INT PRIMARY KEY,
   description VARCHAR(50),
   part_no VARCHAR(50) NOT NULL,
   mf_id VARCHAR(50),
   name VARCHAR(50) NOT NULL,
   lifecycle VARCHAR(50),
   category VARCHAR(50),
   datasheet VARCHAR(100),
   rohs VARCHAR(50),
   mount_type VARCHAR(50),
   FOREIGN KEY(mf_id) REFERENCES manufacturer(mf_id)
);

CREATE TABLE description(
   comp_id INT,
   param VARCHAR(50),
   value VARCHAR(50),
   FOREIGN KEY(comp_id) REFERENCES components(comp_id),
   PRIMARY KEY(comp_id, param)
);

CREATE TABLE stock(
   comp_id INT,
   in_stock INT,
   lead_time INT,
   normally_stocking VARCHAR(5),
   FOREIGN KEY(comp_id) REFERENCES components(comp_id),
   PRIMARY KEY(comp_id)
);

CREATE TABLE price_slabs(
   comp_id INT,
   min_qty INT,
   price DECIMAL(6,2) NOT NULL,
   FOREIGN KEY(comp_id) REFERENCES components(comp_id),
   PRIMARY KEY(comp_id, min_qty)
);

CREATE TABLE orders(
   order_id INT PRIMARY KEY,
   user_id VARCHAR(50),
   date_time DATETIME,
   order_type VARCHAR(50),
   status VARCHAR(50),
   FOREIGN KEY(user_id) REFERENCES users(user_id)
);

CREATE TABLE order_comp(
   order_id INT,
   comp_id INT,
   qty INT,
   FOREIGN KEY(order_id) REFERENCES orders(order_id),
   FOREIGN KEY(comp_id) REFERENCES components(comp_id),
   PRIMARY KEY(order_id, comp_id)
);

CREATE TABLE payments(
   payment_id INT PRIMARY KEY,
   order_id INT,
   trnx_no VARCHAR(50),
   amount INT,
   method VARCHAR(50),
   FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

CREATE VIEW user_age AS
SELECT user_id, name, email_id, phone_number, dob, TIMESTAMPDIFF(YEAR, dob, CURDATE()) AS age, user_since, address, city, state, pincode
FROM users;
```
"""
)

st.markdown(
    """
# Users
"""
)
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
users = pd.DataFrame(
    users,
    columns=[
        "user_id",
        "name",
        "email_id",
        "phone_number",
        "dob",
        "user_since",
        "address",
        "city",
        "state",
        "pincode",
    ],
)
st.dataframe(users)

st.markdown(
    """
# Manufacturer
"""
)
cursor.execute("SELECT * FROM manufacturer")
manufacturer = cursor.fetchall()
manufacturer = pd.DataFrame(
    manufacturer, columns=["mf_id", "name", "description", "location"]
)
st.dataframe(manufacturer)

st.markdown(
    """
# Components
"""
)
cursor.execute("SELECT * FROM components")
components = cursor.fetchall()
components = pd.DataFrame(
    components,
    columns=[
        "comp_id",
        "description",
        "part_no",
        "mf_id",
        "name",
        "lifecycle",
        "category",
        "datasheet",
        "rohs",
        "mount_type",
    ],
)
st.dataframe(components)

st.markdown(
    """
# Description
"""
)
cursor.execute("SELECT * FROM description")
description = cursor.fetchall()
description = pd.DataFrame(description, columns=["comp_id", "param", "value"])
st.dataframe(description)

st.markdown(
    """
# Stock
"""
)
cursor.execute("SELECT * FROM stock")
stock = cursor.fetchall()
stock = pd.DataFrame(
    stock, columns=["comp_id", "in_stock", "lead_time", "normally_stocking"]
)
st.dataframe(stock)

st.markdown(
    """
# Price Slabs
"""
)
cursor.execute("SELECT * FROM price_slabs")
price_slabs = cursor.fetchall()
price_slabs = pd.DataFrame(price_slabs, columns=["comp_id", "min_qty", "price"])
st.dataframe(price_slabs)

st.markdown(
    """
# Orders
"""
)
cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()
orders = pd.DataFrame(
    orders, columns=["order_id", "user_id", "date_time", "order_type", "status"]
)
st.dataframe(orders)

st.markdown(
    """
# Order Components
"""
)
cursor.execute("SELECT * FROM order_comp")
order_comp = cursor.fetchall()
order_comp = pd.DataFrame(order_comp, columns=["order_id", "comp_id", "qty"])
st.dataframe(order_comp)

st.markdown(
    """
# Payments
"""
)
cursor.execute("SELECT * FROM payments")
payments = cursor.fetchall()
payments = pd.DataFrame(
    payments, columns=["payment_id", "order_id", "trnx_no", "amount", "method"]
)
st.dataframe(payments)

st.markdown(
    """
# User Age [View]
"""
)
cursor.execute("SELECT * FROM user_age")
user_age = cursor.fetchall()
user_age = pd.DataFrame(
    user_age,
    columns=[
        "user_id",
        "name",
        "email_id",
        "phone_number",
        "dob",
        "age",
        "user_since",
        "address",
        "city",
        "state",
        "pincode",
    ],
)
st.dataframe(user_age)
