import streamlit as st
import pandas as pd
import mysql.connector
from config import db_config

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

st.set_page_config(page_title="Procedures", layout="wide", page_icon="⚙️")

st.title("Procedures")

st.markdown(
    """
```sql
DELIMITER $$
CREATE PROCEDURE restore_payment(IN payment_id1 INT)
BEGIN
   INSERT INTO payments(payment_id, order_id, trnx_no, amount, method)
   SELECT payment_id, order_id, trnx_no, amount, method
   FROM payments_backup
   WHERE payment_id = payment_id1;

   DELETE FROM payments_backup
   WHERE payment_id = payment_id1;
END $$
DELIMITER ;
```
""")

st.markdown("""
# Restoring the Payment 🤯
## Payments Table
""")
cursor.execute("SELECT * FROM payments;")
payments = cursor.fetchall()
payments = pd.DataFrame(payments, columns=["payment_id", "order_id", "trnx_no", "amount", "method"])
st.dataframe(payments)

st.markdown("""
## Payments Backup Table
""")
cursor.execute("SELECT * FROM payments_backup;")
payments_backup = cursor.fetchall()
payments_backup = pd.DataFrame(payments_backup, columns=["payment_id", "order_id", "trnx_no", "amount", "method", "deleted_at"])
st.dataframe(payments_backup)

payment_id = st.number_input("Enter payment_id to restore", min_value=1, max_value=1000, value=1, step=1)
if st.button("Restore"):
    cursor.execute(f"CALL restore_payment('{payment_id}');")
    db.commit()
    st.success("Restored payment_id: " + str(payment_id))
    st.info(f"**Executed:** `CALL restore_payment('{payment_id}');`")
