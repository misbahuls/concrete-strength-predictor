import streamlit as st
import pandas as pd
import pickle

# Load the trained model
@st.cache_resource
def load_model():
    with open('concrete_model.pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

# Web App UI Design
st.title("Concrete Compressive Strength Predictor")
st.markdown("Predict the 28-day compressive strength of concrete based on mix proportions using Machine Learning.")

st.sidebar.header("Enter Mix Proportions (kg/m³)")

cement = st.sidebar.number_input("Cement", min_value=100.0, max_value=600.0, value=350.0)
slag = st.sidebar.number_input("Blast Furnace Slag", min_value=0.0, max_value=360.0, value=0.0)
fly_ash = st.sidebar.number_input("Fly Ash", min_value=0.0, max_value=200.0, value=0.0)
water = st.sidebar.number_input("Water", min_value=120.0, max_value=250.0, value=175.0)
superplasticizer = st.sidebar.number_input("Superplasticizer", min_value=0.0, max_value=35.0, value=0.0)
coarse_agg = st.sidebar.number_input("Coarse Aggregate", min_value=800.0, max_value=1200.0, value=1020.0)
fine_agg = st.sidebar.number_input("Fine Aggregate", min_value=500.0, max_value=1000.0, value=760.0)
age = st.sidebar.slider("Curing Age (Days)", min_value=1, max_value=365, value=28)

# Prediction Button
if st.button("Predict Strength"):
    input_data = pd.DataFrame([[cement, slag, fly_ash, water, superplasticizer, coarse_agg, fine_agg, age]],
                              columns=['Cement', 'Slag', 'FlyAsh', 'Water', 'Superplasticizer', 
                                       'CoarseAggregate', 'FineAggregate', 'Age_Days'])
    
    prediction = model.predict(input_data)
    
    st.subheader(f"Estimated Strength: {prediction[0]:.2f} MPa")
    
    if prediction[0] >= 30:
        st.success("Status: High-Strength Structural Concrete Mix")
    else:
        st.info("Status: Standard Structural Concrete Mix")