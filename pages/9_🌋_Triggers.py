import streamlit as st
import pandas as pd
import mysql.connector
from config import db_config

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

st.set_page_config(page_title="Triggers", layout="wide", page_icon="🌋")

st.title("Triggers")

st.markdown("""
```sql
CREATE TABLE payments_backup(
   payment_id INT PRIMARY KEY,
   order_id INT,
   trnx_no VARCHAR(50),
   amount INT,
   method VARCHAR(50),
   deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
   FOREIGN KEY(order_id) REFERENCES orders(order_id)
);

DELIMITER $$
CREATE TRIGGER backup_payments
AFTER DELETE ON payments
FOR EACH ROW
BEGIN
    INSERT INTO payments_backup(payment_id, order_id, trnx_no, amount, method)
    VALUES (OLD.payment_id, OLD.order_id, OLD.trnx_no, OLD.amount, OLD.method);
END $$
DELIMITER ;
```
"""
)

st.markdown("""
# Triggering the Trigger 👀
## Payments Table
""")

cursor.execute("SELECT * FROM payments;")
payments = cursor.fetchall()
payments = pd.DataFrame(payments, columns=["payment_id", "order_id", "trnx_no", "amount", "method"])
st.dataframe(payments)

payment_id = st.number_input("Enter payment_id to delete", min_value=1, max_value=1000, value=1, step=1)
if st.button("Delete"):
    cursor.execute(f"DELETE FROM payments WHERE payment_id={payment_id};")
    db.commit()
    st.success("Deleted payment_id: " + str(payment_id))
    st.info(f"**Executed:** `DELETE FROM payments WHERE payment_id={payment_id};`")

st.markdown("""
## Payments Backup Table
""")

cursor.execute("SELECT * FROM payments_backup;")
payments_backup = cursor.fetchall()
payments_backup = pd.DataFrame(payments_backup, columns=["payment_id", "order_id", "trnx_no", "amount", "method", "deleted_at"])
st.dataframe(payments_backup)
