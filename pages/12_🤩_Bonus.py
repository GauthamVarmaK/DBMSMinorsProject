import streamlit as st
import pandas as pd
import mysql.connector
from config import db_config

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

st.set_page_config(page_title="Bonus", layout="wide", page_icon="🤩")

st.title("Bonus")

cursor.execute("DELETE FROM order_comp WHERE order_id=300;")
cursor.execute("DELETE FROM order_comp WHERE order_id=300;")
cursor.execute("DELETE FROM orders WHERE order_id=300;")

st.write("Ever wondered how an order can be placed and processed??")

st.markdown("""
## 1 ) Orders Table
Insert the order into the orders table.
```sql
INSERT INTO orders VALUES('300','a1','2023-05-03', 'Regular', 'PaymentPending');
SELECT * FROM orders WHERE order_id=300;
```
""")

cursor.execute("INSERT INTO orders VALUES('300','a1','2023-05-03', 'Regular', 'PaymentPending');")
cursor.execute("SELECT * FROM orders WHERE order_id=300;")
orders = cursor.fetchall()
orders = pd.DataFrame(orders, columns=["order_id", "customer_id", "order_date", "order_status", "order_total"])
st.dataframe(orders)

st.markdown("""
## 2 ) Order Components Table
Insert the components into the order_comp table.
```sql
INSERT INTO order_comp VALUES('300', '16014451', '450');
INSERT INTO order_comp VALUES('300', '16014453', '600');
INSERT INTO order_comp VALUES('300', '16014452', '550');
INSERT INTO order_comp VALUES('300', '16014457', '650');
SELECT * FROM order_comp WHERE order_id=300;
```
""")

cursor.execute("INSERT INTO order_comp VALUES('300', '16014451', '450');")
cursor.execute("INSERT INTO order_comp VALUES('300', '16014453', '600');")
cursor.execute("INSERT INTO order_comp VALUES('300', '16014452', '550');")
cursor.execute("INSERT INTO order_comp VALUES('300', '16014457', '650');")
cursor.execute("SELECT * FROM order_comp WHERE order_id=300;")
order_comp = cursor.fetchall()
order_comp = pd.DataFrame(order_comp, columns=["order_id", "comp_id", "quantity"])
st.dataframe(order_comp)

st.markdown("""
## 3 ) Get a bill of the order
```sql
SELECT comp_id, comp_name, qty, price, amount
FROM bill_view 
WHERE order_id = 300;
```
""")
cursor.execute("SELECT comp_id, comp_name, qty, price, amount FROM bill_view WHERE order_id = 300;")
bill = cursor.fetchall()
bill = pd.DataFrame(bill, columns=["comp_id", "comp_name", "qty", "price", "amount"])
st.dataframe(bill)

st.markdown("""
## 4 ) Get the total amount of the order
```sql
SELECT SUM(amount) FROM bill_view WHERE order_id = 300;
```
""")
cursor.execute("SELECT SUM(amount) FROM bill_view WHERE order_id = 300;")
total = cursor.fetchall()
total = pd.DataFrame(total, columns=["total"])
st.dataframe(total)

st.markdown("""
## 5 ) Payments Table
Insert the payment into the payments table.
```sql
INSERT INTO payments VALUES('300', '300', '123456789', '8020', 'COD');
UPDATE orders SET order_status='ToBeShipped' WHERE order_id=300;
SELECT * FROM orders WHERE order_id=300;
SELECT * FROM payments WHERE payment_id=300;
```
""")

cursor.execute("INSERT INTO payments VALUES('300', '300', '123456789', '2250', 'COD');")
cursor.execute("UPDATE orders SET status='ToBeShipped' WHERE order_id=300;")
cursor.execute("SELECT * FROM orders WHERE order_id=300;")
orders = cursor.fetchall()
orders = pd.DataFrame(orders, columns=["order_id", "customer_id", "order_date", "order_status", "order_total"])
st.dataframe(orders)

cursor.execute("SELECT * FROM payments WHERE payment_id=300;")
payments = cursor.fetchall()
payments = pd.DataFrame(payments, columns=["payment_id", "order_id", "trnx_no", "amount", "method"])
st.dataframe(payments)

st.divider()

st.markdown("""
# Now, how did we get the bill view?
```sql
CREATE VIEW bill_view AS
SELECT
   order_id,
   comp_id,
   NAME AS comp_name,
   qty,
   best_price(comp_id, qty) AS price,
   qty * best_price(comp_id, qty) AS amount
FROM order_comp
NATURAL JOIN components;
```
""")

st.divider()

st.markdown("""
# Now, how did we get the best price?
```sql
DELIMITER $$
CREATE FUNCTION best_price(comp_id INT, qty INT) RETURNS DECIMAL(6,2)
BEGIN
   DECLARE price DECIMAL(6,2);
   SELECT price_slabs.price INTO price
   FROM price_slabs 
   WHERE price_slabs.comp_id=comp_id AND price_slabs.min_qty<qty 
   ORDER BY price_slabs.min_qty DESC
   LIMIT 1;

   RETURN price;
END $$
DELIMITER ;
```
""")

st.divider()

thanks = st.text("""

         _____ _                 _     __   __          
        |_   _| |               | |    \ \ / /          
          | | | |__   __ _ _ __ | | __  \ V /___  _   _ 
          | | | '_ \ / _` | '_ \| |/ /   \ // _ \| | | |
          | | | | | | (_| | | | |   <    | | (_) | |_| |
          \_/ |_| |_|\__,_|_| |_|_|\_\   \_/\___/ \__,_|
                                                        
                                                        
                 ___  ___      _                                 
                 |  \/  |     ( )                                
                 | .  . | __ _|/  __ _ _ __ ___                  
                 | |\/| |/ _` |  / _` | '_ ` _ \                 
                 | |  | | (_| | | (_| | | | | | |                
                 \_|  |_/\__,_|  \__,_|_| |_| |_|                
                                                        
                                                        
""")