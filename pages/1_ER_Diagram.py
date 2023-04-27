# create a streamlit page in a multipage app to display the er diagram image

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='ER Diagram', page_icon="♦️",layout='wide')

st.title('ER Diagram')
st.markdown('''
    This is the ER Diagram of the database. 
''')
st.image('images/ERDiagram.jpg', use_column_width=True)