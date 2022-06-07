import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

"""
This app analyses trees in San Fransisco """
trees_df = pd.read_csv('trees.csv')
st.write(trees_df.head())
