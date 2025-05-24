import streamlit as st
import joblib
from preprocess import preprocess_form_input
from churn_utils import get_churn_prevention_suggestions

st.set_page_config(page_title="Customer Churn Prediction System")
st.title("📊 Customer Churn Prediction & Prevention")

model = joblib.load('churn_model.pkl')

with st.form("churn_form"):
    st.subheader("Customer Information")
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior = st.selectbox("Senior Citizen", [0, 1])
    partner = st.selectbox("Has Partner", ["Yes", "No"])
    dependents = st.selectbox("Has Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
    monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
    total = st.number_input("Total Charges", 0.0, 10000.0, 1000.0)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    tech_support = st.selectbox("Tech Support", ["Yes", "No"])

    submitted = st.form_submit_button("Predict Churn")

if submitted:
    input_data = {
        'gender': gender,
        'SeniorCitizen': senior,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'PaperlessBilling': paperless,
        'MonthlyCharges': monthly,
        'TotalCharges': total,
        'Contract': contract,
        'InternetService': internet,
        'PaymentMethod': payment,
        'TechSupport': tech_support
    }

    processed = preprocess_form_input(input_data)
    prediction = model.predict(processed)[0]

    if prediction == 1:
        st.error("⚠️ The customer is likely to churn.")
        st.subheader("🛡️ Recommended Actions:")
        for s in get_churn_prevention_suggestions(processed.iloc[0].to_dict()):
            st.markdown(f"- {s}")
    else:
        st.success("✅ The customer is likely to stay.")
