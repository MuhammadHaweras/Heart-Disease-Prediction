# 💓 Heart Disease Prediction App

A Machine Learning-powered web application built using Streamlit that predicts the risk of heart disease based on clinical and personal inputs. This app uses a trained Logistic Regression model and is based on the Cleveland Heart Disease dataset.

---

## 📌 Project Overview

Heart disease is one of the leading causes of death globally. Early detection can help improve treatment outcomes and reduce complications. This application enables users to input patient data and get a risk prediction instantly.

---

## 🚀 Demo

Try it live on Streamlit Cloud 👉 [(https://rsgorgsttpjdr5v3ahmxza.streamlit.app/)]

---

## 🛠️ Features

- Clean and interactive Streamlit UI
- Input validation and clear warnings
- Risk classification:
  - ✅ No Risk
  - ❗ Moderate Risk
  - 🚨 Critical Risk
- Selcted Best model among 9 hyperparameter tuned models
- Custom trained Logistic Regression model using GridSearchCV

---

## 📂 Dataset Description

The app uses the **Cleveland Heart Disease** dataset from UCI Machine Learning Repository. It includes:
- **14 attributes** (e.g., age, sex, chest pain type, blood pressure, cholesterol, etc.)
- Target column: `num` (heart disease risk on a scale 0–4)

---

## 📈 Model Training

The model was trained using the following steps:
- Data cleaning and label encoding
- Feature engineering and correlation analysis
- Multiple models compared using cross-validation and hyperparameter tuning
- Best performance from **Logistic Regression** with:
  - `C=0.1`
  - `solver='lbfgs'`
  - Accuracy ≈ 68.6%

---

## 🔧 Tech Stack

- Python
- Streamlit
- scikit-learn
- pandas, seaborn, matplotlib, plotly

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/heart-disease-prediction.git
cd heart-disease-prediction
