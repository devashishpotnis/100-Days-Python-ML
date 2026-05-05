import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(page_title="Heart Disease Predictor", page_icon="")

# Custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f5f7fa;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #ff1a1a;
        }
    </style>
""", unsafe_allow_html=True)

# Load model
with open("HeartDiseasePrediction.pkl", 'rb') as f:
    model = pickle.load(f)

# Sidebar
st.sidebar.title("App Info")
st.sidebar.write("""
This app predicts the risk of heart disease based on patient health data.

### Features Used:
- Age  
- Gender  
- Chest Pain Type  
- Blood Pressure  
- Cholesterol  
- Heart Rate  

### Instructions:
1. Enter all details carefully  
2. Click on Predict  
3. View result instantly  
""")

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Developed by You Devashish Potnis")
#st.sidebar.write("👨‍⚕️ Under guidance of Dr.Abhijeet Yelale Sir")

# Title
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'> Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.write("Enter patient details below:")

# Inputs (Single Column)
age = st.number_input("Age", 1, 120)

gender = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0

cp = st.selectbox("Chest Pain Type", [0,1,2,3])

trestbps = st.number_input("Resting Blood Pressure")

chol = st.number_input("Cholesterol Level")

fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0,1])

restecg = st.selectbox("Resting ECG", [0,1,2])

thalach = st.number_input("Maximum Heart Rate Achieved")

exang = st.selectbox("Exercise Induced Angina", [0,1])

oldpeak = st.number_input("ST Depression")

slope = st.selectbox("Slope of ST Segment", [0,1,2])

ca = st.selectbox("Number of Major Vessels", [0,1,2,3])

thal = st.selectbox("Thalassemia", [0,1,2,3])

# Button
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Predict Heart Disease"):
    
    data = np.array([[age, gender, cp, trestbps, chol, fbs,
                      restecg, thalach, exang, oldpeak,
                      slope, ca, thal]])

    prediction = model.predict(data)

    st.markdown("---")

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")