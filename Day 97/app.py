import streamlit as st
import numpy as np
import pandas as pd
import pickle 


with open("diabetes_dataset.pkl",'rb') as f:
    model=pickle.load(f)


st.title("Diabetes Prediction By Devashish Mayur Potnis and Varad Wavare")
st.write("Enter the details to check whether a person has Diabetes or not")

pregnancies = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose Level", 50, 300, 100)
blood_pressure = st.number_input("Blood Pressure", 30, 150, 70)
skin_thickness = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin Level", 0, 900, 80)
bmi = st.number_input("BMI", 10.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree", 0.0, 3.0, 0.3)
age = st.number_input("Age", 10, 100, 30)

if st.button("Predict Diabetes"):
    
    data = np.array([[pregnancies, glucose, blood_pressure,
                      skin_thickness, insulin, bmi, dpf, age]])
    
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Person is Diabetic")
    else:
        st.success("Person is Not Diabetic")


