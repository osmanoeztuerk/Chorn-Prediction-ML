import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('Welcome!')
st.header('Welcome to "Employee Churn Analysis Project".')

dept_options = {
    'Sales': 'sales',
    'Technical': 'technical',
    'Support': 'support',
    'IT': 'it',
    'Product Manager': 'product_mng',
    'Marketing': 'marketing',
    'RandD': 'RandD',
    'Accounting': 'accounting',
    'HR': 'hr',
    'Management': 'management'
}

# Define input fields
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        param1 = st.slider('Satisfaction Level:', min_value=0.0, max_value=1.0, step=0.01)
        param2 = st.slider('Last Evaluation:', min_value=0.0, max_value=1.0, step=0.01)
        param3 = st.slider('Number of Project:', min_value=0, max_value=8, step=1)
        param4 = st.slider('Average Monthly Hours:', min_value=95, max_value=350, step=1)
        param5 = st.slider('Time Spend Company:', min_value=2, max_value=10, step=1)
        
    with col2:
        param6 = 1 if st.radio("Work Accident", ("Yes", "No")) == "Yes" else 0
        param7 = 1 if st.radio("Promotion Last 5 Years", ("Yes", "No")) == "Yes" else 0
        param8 = st.radio('Department', ('sales', 'technical','support','IT','product_mng', 'marketing','RandD','accounting','hr','management'))
        param9 = st.radio('Salary', ("Low", "Medium", "High"))

if param9 == "Low":
    param9 = "low"
elif param9 == "Medium":
    param9 = "medium"
else:
    param9 = "high"
    

observations = {'satisfaction_level':[param1],
                'last_evaluation':[param2],
                'number_project':[param3],
                'average_montly_hours':[param4],
                'time_spend_company':[param5],
                'Work_accident':[param6],
                'promotion_last_5years':[param7],
                'Departments ':[param8],
                'salary':[param9]}
observations = pd.DataFrame(observations)
st.write(observations)


import pickle
from xgboost import XGBRegressor
model = pickle.load(open('xgb_model', 'rb'))

if st.button('Predict'):
    pred = model.predict(observations)
    #st.write(pred)
    
    if pred > 0.5:
        st.warning(f"Probably Gone! {pred}")
    else:
        st.warning(f"Probably will stay! {pred}")