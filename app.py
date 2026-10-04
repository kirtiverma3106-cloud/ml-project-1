import streamlit as st
import joblib
import pandas as pd

model = joblib.load("decision_tree_loan_model.pkl")
features = joblib.load("feature_columns.pkl")

st.title("🌳 Loan Prediction using Decision Tree")

age = st.number_input("Age", 18, 80, 25)
income = st.number_input("Income", 0, 1000000, 50000)
loan = st.number_input("Loan Amount", 0, 1000000, 10000)
credit = st.number_input("Credit Score", 300, 850, 650)

if st.button("Predict"):

    data = pd.DataFrame({
        "person_age": [age],
        "person_income": [income],
        "loan_amnt": [loan],
        "credit_score": [credit]
    })

    data = data.reindex(columns=features, fill_value=0)

    result = model.predict(data)[0]

    if result == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")
