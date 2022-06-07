import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import pandas as pd
"""
The last step is to allow a user to upload their own data
Streamlit has a function called *file_uploader()* upto 200mb
Our default interactive widget-like seect box is just the first
value in our list, but it does not make sense to have a default
uploaded file before the user actually interacts with te app.
The default user uploaded file has a value of None
"""
st.title("Streamlit Flow Control")
"""
There are two solutions to this data upload default problem
We can provide the default file to use until the user interacts
with the application, or we can stop the app until a file is uploaded.
We can start with the first option. The following code uploads the
*st.file_uploader()* function from within an if statement. If the
user uploads a file, then the app uses that, if they do not, then
 we default to the file we have used before"""
st.subheader("Palmer's Penguin")
penguin_file = st.file_uploader(
    'Select your local penguins CSV (default provided)')
if penguin_file is not None:
    penguins_df = pd.read_csv(penguin_file)
else:
    # penguins_df = pd.read_csv('penguins.csv')
    # there is an option to stop the application when no file is uploaded
    st.stop()

selected_x_var = st.selectbox(
    'What do you want variable x to be',
    ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm','body_mass_g']
)
selected_y_var = st.selectbox(
    'What about the y?',
    ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm','body_mass_g']
)

fig, axs = plt.subplots()
axs = sns.scatterplot(
    x=selected_x_var,
    y = selected_y_var,
    hue = 'species',
    data = penguins_df
)
plt.xlabel(selected_x_var)
plt.ylabel(selected_y_var)
plt.title("Scatterplot of Palmer's Penguins")
st.pyplot(fig)
