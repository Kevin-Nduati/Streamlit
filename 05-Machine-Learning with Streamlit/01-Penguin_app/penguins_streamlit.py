# Now that we have our model, we want to load it along with our mapping function
# into streamlit.
import streamlit as st
import pickle
import pandas as pd

rf_pickle = open('random_forest_penguin.pickle', 'rb')
map_pickle = open('output_penguin.pickle', 'rb')
rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
rf_pickle.close()
map_pickle.close()
# st.write(rfc)
# st.write(unique_penguin_mapping)
# df = pd.read_csv('penguins.csv')
# st.write(df['island'].unique())

# We should now add streamlit functions to get the user input.
island = st.selectbox(
    'Penguin Island',
    options=['Biscoe', 'Dream', 'Torgerson']
)
sex = st.selectbox(
    'Sex',
    options=['Female', 'Male']
)
bill_length = st.number_input('Bill Length (mm)', min_value=0.0)
bill_depth = st.number_input('Bill Depth (mm)', min_value=0.0)
flipper_length = st.number_input('Flipper Length (mm)', min_value=0.0)
body_mass = st.number_input('Body Mass (g)', min_value=0.0)
st.write(f'the user inputs are {[island, bill_length, bill_depth, flipper_length, body_mass]}')

# Now that we have all our inputs, the next step is to format
#  the data in the same format as our preprocessed data, for example, 
# our model does not have one variable called sex, but instead have
# two variables called sex_female and sex_male. Once our data is in
#  the same shape, we can call predict function and map the prediction to our 
# original species list an see how our model functions
island_biscoe, island_dream, island_torgerson = 0,0,0
if island == 'Biscoe':
    island_biscoe = 1
elif island == 'Dream':
    island_dream = 1
elif island == 'Torgerson':
    island_torgerson = 1

sex_female, sex_male = 0,0
if sex == 'Female':
    sex_female = 1
elif sex == 'Male':
    sex_male = 1

# All of our data is in the correct format, we the use the predict()
#  function on our model with new data
new_prediction = pd.DataFrame(rfc.predict([[
    bill_length, bill_depth, flipper_length,
    body_mass, island_biscoe, island_dream,
    island_torgerson, sex_female, sex_male ]])).iloc[0][0]

unique_penguin_mapping = pd.DataFrame(unique_penguin_mapping)

# st.write(pd.DataFrame(unique_penguin_mapping).iloc[0][0])

# prediction_species = unique_penguin_mapping.iloc[new_prediction][0]

st.write(f'We predict your penguin is of the **{new_prediction}** species')
