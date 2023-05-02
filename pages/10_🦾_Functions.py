import streamlit as st
import pandas as pd
import mysql.connector
from config import db_config

db = mysql.connector.connect(**db_config)
cursor = db.cursor()

st.set_page_config(page_title="Functions", layout="wide", page_icon="🦾")

st.title("Functions")

st.markdown(
    """
```sql
DELIMITER $$
CREATE FUNCTION is_prime_user(user_id VARCHAR(50)) RETURNS VARCHAR(5)
BEGIN
   DECLARE user_since DATE;
   DECLARE is_prime VARCHAR(5);

   SELECT user_since INTO user_since
   FROM users
   WHERE user_id = user_id;

   IF TIMESTAMPDIFF(YEAR, user_since, CURDATE()) > 4 THEN
      SET is_prime = 'True';
   ELSE
      SET is_prime = 'False';
   END IF;

   RETURN is_prime;
END;$$
DELIMITER ;
```
""")

st.markdown("""
# Is Prime User? 👑
## Users Table
""")

cursor.execute("SELECT * FROM users;")
users = cursor.fetchall()
users = pd.DataFrame(users, columns=["user_id","name","email_id","phone_number","dob","user_since","address","city","state","pincode"])
st.dataframe(users)

user_id = st.text_input("Enter user_id to check", value="a1")
if st.button("Check"):
    cursor.execute(f"SELECT is_prime_user('{user_id}');")
    is_prime = cursor.fetchone()
    if is_prime[0] == 'TRUE':
        st.success("Is Prime User: " + str(is_prime[0]))
    else:
        st.error("Is Prime User: " + str(is_prime[0]))
    st.info(f"**Executed:** `SELECT is_prime_user('{user_id}');`")
