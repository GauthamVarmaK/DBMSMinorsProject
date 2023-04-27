# create a streamlit page in a multipage app to display the relational schema image

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Relational Schema', page_icon="🔗",layout='wide')

st.title('Relational Schema')
st.markdown('''
    This is the Relational Schema of the database. 
''')
st.image('images/RelationalSchema.jpg', use_column_width=True)