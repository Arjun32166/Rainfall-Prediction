import streamlit as st 
import joblib 
import sklearn 

st.title("Rain Fall Prediction")

a1=st.number_input("Enter Pressure")
a2=st.number_input("Enter Dew point")
a3=st.number_input("Enter humidity")
a4=st.number_input("Enter Cloud")
a5=st.number_input("Enter Sunshine")
a6=st.number_input("Enter Winddirection")
a7=st.number_input("Enter Windspeed")

def predict():
    # some code
    op = mymodel.predict([[a1, a2, a3, a4, a5, a6, a7]])
