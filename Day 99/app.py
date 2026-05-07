import streamlit as st
import numpy as np
import pickle

# Page config
st.set_page_config(page_title="Stroke Predictor", page_icon="")

# Custom CSS (SAME UI)
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
model = pickle.load(open("StrokePrediction.pkl", "rb"))

# Sidebar (SAME STYLE)
st.sidebar.title("App Info")
st.sidebar.write("""
This app predicts the risk of stroke based on patient health data.

### Instructions:
1. Enter all details carefully  
2. Click on Predict  
3. View result instantly  
""")

st.sidebar.markdown("---")
st.sidebar.write("👨‍💻 Developed by Devashish Potnis")

# Title
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>Stroke Prediction</h1>", unsafe_allow_html=True)
st.write("Enter patient details below:")

# Inputs (SAME STYLE)

gender = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0

age = st.number_input("Age", 1, 120)

hypertension = st.selectbox("Hypertension", [0,1])

heart_disease = st.selectbox("Heart Disease", [0,1])

ever_married = st.selectbox("Ever Married", ["Yes", "No"])
ever_married = 1 if ever_married == "Yes" else 0

work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children"])
work_map = {"Private":0, "Self-employed":1, "Govt_job":2, "children":3}
work_type = work_map[work_type]

residence = st.selectbox("Residence Type", ["Urban", "Rural"])
residence = 1 if residence == "Urban" else 0

avg_glucose = st.number_input("Average Glucose Level")

bmi = st.number_input("BMI")

smoking = st.selectbox("Smoking Status", ["never smoked", "formerly smoked", "smokes"])
smoke_map = {"never smoked":0, "formerly smoked":1, "smokes":2}
smoking = smoke_map[smoking]

# Button
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Predict Stroke Risk"):
    
    data = np.array([[gender, age, hypertension, heart_disease,
                      ever_married, work_type, residence,
                      avg_glucose, bmi, smoking]])

    prediction = model.predict(data)

    st.markdown("---")

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Stroke")
    else:
        st.success("✅ Low Risk of Stroke")