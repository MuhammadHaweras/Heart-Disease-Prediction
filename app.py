import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('./best_heart_disease_model.pkl')

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")
st.title("💓 Heart Disease Prediction App")

st.markdown("Enter patient details to predict heart disease risk.")

cp_options = {
    "Select a Value": None,
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-Anginal": 2,
    "Asymptomatic": 3
}

restecg_options = {
    "Select a Value": None,
    "Normal": 0,
    "Stt Abnormality": 1,
    "LV Hypertrophy": 2
}

slope_options = {
    "Select a Value": None,
    "Downsloping": 0,
    "Flat": 1,
    "Upsloping": 2
}

thal_options = {
    "Select a Value": None,
    "normal": 0,
    "fixed defect": 1,
    "reversible defect": 2
}

# Input fields
st.subheader("📝 Patient Details")
age = st.number_input("Age", min_value=1, max_value=120, value=None)
sex = st.selectbox("Sex", ["Select a Value", "Male", "Female"])
cp_label = st.selectbox("Chest Pain Type (cp)", list(cp_options.keys()))
trestbps = st.number_input("Resting Blood Pressure", min_value=10, value=None)
chol = st.number_input("Cholesterol", min_value=10, value=None)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", ["Select a Value", "Yes", "No"])
restecg_label = st.selectbox("Resting ECG (restecg)", list(restecg_options.keys()))
thalch = st.number_input("Max Heart Rate Achieved (thalch)", min_value=70, max_value=210, value=None)
exang = st.selectbox("Exercise-Induced Angina (exang)", ["Select a Value", "Yes", "No"])
oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, format="%.1f", value=None)
slope_label = st.selectbox("Slope of ST Segment", list(slope_options.keys()))
ca = st.selectbox("Number of Major Vessels Colored", ["Select a Value", 0, 1, 2, 3])
thal_label = st.selectbox("Thalassemia (thal)", list(thal_options.keys()))

# Validate input
all_filled = all([
    age, trestbps, chol, thalch, oldpeak is not None,
    sex != "Select a Value",
    cp_options[cp_label] is not None,
    fbs != "Select a Value",
    restecg_options[restecg_label] is not None,
    exang != "Select a Value",
    slope_options[slope_label] is not None,
    ca != "Select a Value",
    thal_options[thal_label] is not None
])

# Encode categorical values

sex_val = 1 if sex == "Male" else 0 if sex == "Female" else None
fbs_val = 1 if fbs == "Yes" else 0 if fbs == "No" else None
exang_val = 1 if exang == "Yes" else 0 if exang == "No" else None

# Show input data if all fields are valid
if not all_filled:
    st.warning("⚠️ Please fill in **all fields** and select **valid options** before predicting.")
else:
    input_data = pd.DataFrame([{
        'age': age,
        'sex': sex_val,
        'cp': cp_options[cp_label],
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs_val,
        'restecg': restecg_options[restecg_label],
        'thalch': thalch,
        'exang': exang_val,
        'oldpeak': oldpeak,
        'slope': slope_options[slope_label],
        'ca': int(ca),
        'thal': thal_options[thal_label],
    }])

    st.subheader("📋 Input Data")
    st.write(input_data)

    if st.button("🧠 Predict"):
        prediction = model.predict(input_data)[0]

        st.subheader("🔍 Prediction")

        if prediction == 0:
            st.success("**✅ No Heart Disease Risk Detected**")
        elif prediction == 1:
            st.warning("**⚠️ Risk of Mild Heart Disease Detected**")
        else:
            st.error("**🚨 Risk of Critical Heart Disease Detected**")
