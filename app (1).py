import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="Telecom Churn Prediction", layout="centered")

st.title("Telecom Customer Churn Prediction App")


model = pickle.load(open("model.pkl", "rb"))

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])

tenure = st.number_input("Tenure (months)", 0, 100, 1)
monthly = st.number_input("Monthly Charges", 0.0, 200.0, 50.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 100.0)

gender = 1 if gender == "Male" else 0
senior = 1 if senior == "Yes" else 0
partner = 1 if partner == "Yes" else 0
dependents = 1 if dependents == "Yes" else 0


if st.button("Predict"):

    input_data = np.array([[gender, senior, partner, dependents,
                            tenure, monthly, total]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Customer is likely to CHURN")
        st.write("This customer is at risk of leaving the company.")
        st.write("CHURN = YES → Customer will leave")
        st.write("CHURN = NO → Customer will stay")

    else:
        st.success("Customer is NOT likely to churn")
        st.write("This customer is likely to stay with the company.")
        st.write("CHURN = NO → Customer will stay")
        st.write("CHURN = YES → Customer will leave")
