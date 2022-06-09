import streamlit as st
import pandas as pd
st.title('SF Trees')
st.write('This app analyses trees in San Francisco')
trees_df = pd.read_csv('trees.csv')
# Streamlit allows us to format our app into dynamic columns using the 
# st.columns(). We can divide oyr streamlit ap into multiple columns 
# of variable lengths, and then treat each column as its own unique space
# in our app to include text, graphs, images, or anything else.
# The syntax for columns in streamlit uses with notation. The following
#  code imports our SF Trees dataset and creates three columns

col1, col2, col3 = st.columns((1,1,1))
with col1:
    st.write('First column')
with col2:
    st.write('Second column')
with col3:
    st.write('Third column')


# USING THE STREAMLIT SIDEBAR
