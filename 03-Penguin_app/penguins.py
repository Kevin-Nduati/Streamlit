import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')

st.title("Palmer's Penguins")

# import data
penguins_df = pd.read_csv('penguins.csv')
st.write(penguins_df.head(10))
"""
The final goal of this mini-app is going to be to ask the user
to specify oen of the species f penguins and to then also choose 
two other variables to choose in the scatterplot. We will start by
learning how to take thse inputs, and create a dynamic visualization"""

selected_species = st.selectbox(
    'What species would you like to visualize',
    ['Adelie', 'Gentoo', 'Chinstrap'])

df = penguins_df[penguins_df['species'] == selected_species]
selected_x_var = st.selectbox(
    'What species would you want the x variable to be',
    ['bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox(
    'What species would you want the y variable to be',
    ['bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g'])
# title = st.text_input(label = 'Insert the title')
fig, axs = plt.subplots()
markers = {'Adelie':'X', 'Gentoo':'s', 'Chinstrap':'o'}
axs = sns.scatterplot(
    x=selected_x_var,
    y = selected_y_var,
    data=df, 
    hue = 'species',
    markers = markers,
    style='species'
)
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title(f'Scatterplot of {selected_species}')
st.pyplot(fig)