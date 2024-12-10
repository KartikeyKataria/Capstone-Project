# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:44:57 2024

@author: user
"""

import streamlit as st
import pandas as pd
import pickle

# load model
loaded_dataset = pickle.load(open('C:/Users/user/Downloads/trainedmodel.sav','rb'))

# Save the trained model
with open('C:/Users/user/Downloads/trainedmodel.sav', 'wb') as f:
    pickle.dump(trained_models, f)

# Load the trained model
with open('C:/Users/user/Downloads/trainedmodel.sav','rb') as f:
    model = pickle.load(f)

# Create a Streamlit app
st.title("Fraud Analysis App")

# Input fields for feature values on the main screen
st.header("Enter Customer Information")
amount = st.number_input("Amount", min_value=0, max_value=10000000, value=1)
Old_balance_original = st.number_input("Old Balance Original", min_value=0, max_value=10000000, value=1)
New_balance_original = st.number_input("New Balance Original", min_value=0, max_value=10000000, value=1)
Old_balance_Desitination = st.number_input("Old Balance Destination", min_value=0, max_value=10000000, value=1)
New_balance_Desitination = st.number_input("New Balance Destination", min_value=0, max_value=10000000, value=1)

# Create a pandas DataFrame to hold the feature values
data = pd.DataFrame({'amount': [amount], 
                     'Old_balance_original': [Old_balance_original], 
                     'New_balance_original': [New_balance_original], 
                     'Old_balance_Destination': [Old_balance_Desitination], 
                     'New_balance_Destination': [New_balance_Desitination]})

# Make a prediction using the model
prediction = model.predict(data)

# Display the prediction result on the main screen
st.header("Prediction Result")
if prediction[0] == 0:
    st.success("The transaction is not fraud.")
else:
    st.error("This transaction is fraud.")
