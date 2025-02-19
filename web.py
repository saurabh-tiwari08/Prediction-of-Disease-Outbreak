import os 
import pickle
import streamlit as st
import streamlit_option_menu 
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of disease Outbreaks", 
                   page_icon="doctor", 
                   layout="wide")

diabetes_model = pickle.load(open('E:\\Edunet AI Phase 3\\training_models\\diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('E:\\Edunet AI Phase 3\\training_models\\heart_model.sav', 'rb'))
parkinson_model = pickle.load(open('E:\\Edunet AI Phase 3\\training_models\\parkinsons_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu("Prediction of Disease Outbreak System ", 
                           ["Diabetes Prediction", "Heart Disease Prediction", "Parkinson Disease Prediction"],
                           menu_icon = "hospital-fill", icons=['activity', 'heart', 'person'], default_index=0) 
    
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        glucose = st.text_input("Glucose Level")
    with col3:
        Blood_pressure = st.text_input("Blood Pressure Value")
    with col1:
        Skin_thickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI Value")    
    with col1:
        Diabetes_pedigree_function = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age = st.text_input("Age of the person")

    diab_diagonosis = " "
    if st.button("Diabetes test Result"):
        user_input = [Pregnancies, glucose, Blood_pressure, Skin_thickness, Insulin, BMI, Diabetes_pedigree_function, Age]
        user_input = [float(i) for i in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagonosis = "The person is Diabetic"
        else:
            diab_diagonosis = "The person is not Diabetic"
    st.write(diab_diagonosis)

if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input("Age of the person")
    with col2:
        Sex = st.text_input("Sex of the person")
    with col3:
        Cheast_Pain = st.text_input("Cheast Pain Type")
    with col1:
        Blood_pressure = st.text_input("Blood Pressure Value")
    with col2:
        Serum = st.text_input("Serum Cholestrol Value")
    with col3:
        Fasting_Blood_sugar = st.text_input("Fasting Blood Sugar Value > 120 mg/dl")    
    with col1:
        Electrocardiographic = st.text_input(" Electrocardiographic Result")
    with col2:
        Heart_rate = st.text_input("Maximum Heart Rate Achieved")
    with col3:
        Exercise_induced_angina = st.text_input("Exercise Induced Angina")
    with col1:
        ST_depression = st.text_input("ST Depression Value induced by exercise")
    with col2:
        Slope = st.text_input("Slope of the peak exercise ST segment")
    with col3:
        Major_vessels = st.text_input("Major Vessels Colored by Flourosopy")
    with col1:
        Thalassemia = st.text_input("Thal: 0=normal, 1=fixed defect, 2=reversable defect")
    

    heart_diagonosis = " "

    if st.button("Heart disease test Result"):
        user_input = [Age, Sex, Cheast_Pain, Blood_pressure, Serum, Fasting_Blood_sugar, Electrocardiographic, Heart_rate, Exercise_induced_angina, ST_depression, Slope, Major_vessels, Thalassemia]
        user_input = [float(i) for i in user_input]
        Heart_Disease_prediction = heart_model.predict([user_input])
        if Heart_Disease_prediction[0] == 1:
            heart_diagonosis = "The person has Heart Disease"
        else:
            heart_diagonosis = "The person is not Heart Disease"
    st.write(heart_diagonosis)

if selected == "Parkinson Disease Prediction":
    st.title("Parkinson Disease Prediction using Ml")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        MDVP_Fo = st.text_input("MDVP:Fo(Hz)")
    with col2:
        MDVP_Fhi = st.text_input("MDVP:Fhi(Hz)")
    with col3:
        MDVP_Jitter = st.text_input("MDVP:Jitter(%)")
    with col4:
        MDVP_Jiter_Abs = st.text_input("MDVP:Jitter(Abs)")
    with col5:
        MDVP_RAP = st.text_input("MDVP:RAP")
    with col1:
        MDVP_PPQ = st.text_input("MDVP:PPQ")
    with col2:
        Jitter_DDP = st.text_input("Jitter:DDP")
    with col3:
        MDVP_Shimmer = st.text_input("MDVP:Shimmer")
    with col4:
        MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
    with col5:  
        Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
    with col1:
        Shimmer_APQ5 = st.text_input("Shimmer:APQ5")
    with col2:
        MDVP_APQ = st.text_input("MDVP:APQ")
    with col3: 
        Shimmer_DDA = st.text_input("Shimmer:DDA")
    with col4:
        NHR = st.text_input("NHR")
    with col5:
        HNR = st.text_input("HNR")
    with col1:  
        RPDE = st.text_input("RPDE")
    with col2:
        DFA = st.text_input("DFA")
    with col3:            
        Spread1 = st.text_input("Spread1")
    with col4:
        Spread2 = st.text_input("Spread2")
    with col5:
        D2 = st.text_input("D2")
    with col1:
        PPE = st.text_input("PPE")

    parkinson_diagonosis = " "
    if st.button("Parkinson Disease test Result"):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Jitter, MDVP_Jiter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, Spread1, Spread2, D2, PPE]
        user_input = [float(i) for i in user_input]
        parkinson_prediction = parkinson_model.predict([user_input])
        if parkinson_prediction[0] == 1:
            parkinson_diagonosis = "The person has Parkinson Disease"
        else:
            parkinson_diagonosis = "The person is not Parkinson Disease"
    st.write(parkinson_diagonosis)

    














