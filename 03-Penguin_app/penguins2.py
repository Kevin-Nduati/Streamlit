import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

st.title('Data MAnipulation in Streamlit')
"""What if we wanted the user to be able to
 filter out penguins based on their gender"""
st.subheader("PAlmer's Penguins")
penguin_file = st.file_uploader(
    'Select your local penguins CSV (default provided',
)
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    penguins_df = pd.read_csv('penguins.csv')

selected_x_var = st.selectbox(
    'What do you want variable x to be',
    ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
)
selected_y_var = st.selectbox(
    'What about variable y',
    ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']
)
selected_gender = st.selectbox(
    'What gender do you want to filter for',
    ['all penguins', 'male penguins', 'female penguins']
)
if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df['sex'] == 'female']
else:
    pass

fig, axs = plt.subplots()
axs = sns.scatterplot(
    x = selected_x_var,
    y = selected_y_var,
    data = penguins_df,
    hue = 'species'
)
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title(f'Scatterplot of Palmer"s Penguins {selected_gender}')
st.pyplot(fig)

"""
We have added another selectbox plugin, with male and female, and all options
We could have done this by asking for a text input, but for data manipulation,
we want to restrict user action as much as possible"""
