import streamlit as st
import joblib
import numpy as np

scaler=joblib.load("scaler.pkl")

model=joblib.load("model.pkl")

st.title("Customer Car Price Estimator App")

st.divider()

st.write("""This app is for getting a price estimation for the customer so a car with the price range given can be adviced to the customer""")

age=st.number_input("Enter the age", min_value=18, max_value=90, value=40, step=1)

salary=st.number_input("Enter the salary",min_value=1000, max_value=999999999, value=30000,step=5000)

networth=st.number_input("Enter the net worth",min_value=0, max_value=999999999,value=10000,step=20000)

x=[age, salary, networth]
calculatebutton=st.button("Calculate")
st.divider()

if calculatebutton:
    
    x_2=np.array(x)
    x_array=scaler.transform([x_2])
    
    prediction=model.predict(x_array)
    st.write("Prediction is:", prediction[0])
    st.write("Advice cars in the similar values")

    
else:
    st.write("Please enter the values and press the calculate button")

