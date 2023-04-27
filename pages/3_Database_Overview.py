# create a stream lit page to describe the database

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Database Overview', page_icon="📊",layout='wide')

st.title('Database Overview')

st.markdown('''
    This is the overview of the database.
''')

st.markdown('''
```sql
CREATE DATABASE electronics_store;

USE electronics_store;

-- Create tables
CREATE TABLE users(
   user_id VARCHAR(50) PRIMARY KEY,
   NAME VARCHAR(50),
   email_id VARCHAR(50) CHECK (email_id LIKE '%@%.%'),
   phone_number VARCHAR(50) CHECK (LENGTH(phone_number) = 10),
   dob DATE,
   age INT CHECK (age >= 18),
   user_since DATE,
   address VARCHAR(100),
   city VARCHAR(50),
   state VARCHAR(50),
   pincode INT
);

CREATE TABLE manufacturer(
   mf_id VARCHAR(50) PRIMARY KEY,
   NAME VARCHAR(50) NOT NULL,
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
   price INT NOT NULL,
   FOREIGN KEY(comp_id) REFERENCES components(comp_id),
   PRIMARY KEY(comp_id, min_qty)
);

CREATE TABLE orders(
   order_id INT PRIMARY KEY,
   user_id VARCHAR(50),
   DATETIME DATETIME,
   order_type VARCHAR(50),
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
```
''');