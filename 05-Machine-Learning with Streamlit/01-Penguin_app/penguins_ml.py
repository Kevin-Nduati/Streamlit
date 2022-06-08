import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
penguins_df = pd.read_csv('penguins.csv')
print(penguins_df.head())

# We will create a model that oredicts the species of the penguin 
penguins_df.dropna(inplace=True)
output = penguins_df['species']
features = penguins_df[['island', 'bill_length_mm', 'bill_depth_mm',
                        'flipper_length_mm', 'body_mass_g', 'sex']]
features = pd.get_dummies(features)

# Split our data into test and train
X_train, X_test, y_train, y_test = train_test_split(features, output, 
                                                        test_size=0.2)
rfc = RandomForestClassifier(random_state=42)
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
score = accuracy_score(y_pred, y_test)
print(f'Accuracy: {score}')

# We will save two parts of our model: the model itself and the uniques 
# variable, which maps the factorized output variable to the species we
#  recognize. We will save these ojects as pickle files
output, uniques = pd.factorize(output)
rf_pickle = open('random_forest_penguin.pickle', 'wb')
pickle.dump(rfc, rf_pickle)
rf_pickle.close()
output_pickle = open('output_penguin.pickle', 'wb')
pickle.dump(uniques, output_pickle)
output_pickle.close()

# We now have two more files in our folder, a file called 
# *random_forest_penguin.pickle*, which contains our model, and 
# *output_penguin.pickle* which has the mapping between penguin species 
# and the output of our model. Let us move to our streamlit app

