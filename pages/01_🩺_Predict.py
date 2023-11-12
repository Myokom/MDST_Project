import streamlit as st
from joblib import load
import numpy as np

st.set_page_config(
    page_title = "Predict", 
    page_icon = "🩺",
    layout = "centered"
)

def load_model_and_scaler():
    """Loads the logistic regression model and scaler from joblib files."""
    logreg = load('logreg_model.joblib')
    scaler = load('scaler.joblib')
    
    return logreg, scaler

def predict_diabetes(logreg, scaler, user_input):
    """Predicts diabetes based on user input using the given model and scaler."""
    X_scaled = scaler.transform(user_input)
    prediction = logreg.predict(X_scaled)
    return prediction

def show_predict_page():
    st.title("Do you have diabetes or not?  :mending_heart: :hospital:")

    st.write("""### We need some information to make a prediction""")
    
    # User input fields
    # Define a dictionary for gender mapping
    gender_mapping = {
        "Male": 1,
        "Female": 2
    }

    # Let user select using the human-readable options
    selected_gender = st.selectbox(
        label = "What gender were you assigned at birth?", 
        options = list(gender_mapping.keys()),
        index = None,
        placeholder = "Choose a response...")

    # Convert the selected option to its numerical value
    gender = gender_mapping.get(selected_gender)

    hip_circumference = st.number_input(
        label = "Hip Circumference (cm)", 
        value = None,
        step = 1,
        placeholder = "Type a number...")
    
    moderate_work_activity_mapping = {
        "Yes": 1, 
        "No": 2,
    }

    # Let user select using the human-readable options
    selected_moderate_work_activity = st.selectbox(
        label = "Does your work involve moderate-intensity activity that causes small increases in breathing or heart rate such as brisk walking or carrying light loads for at least 10 minutes continuously?", 
        options = list(moderate_work_activity_mapping.keys()),
        index = None,
        placeholder = "Choose a response...")
    
    moderate_work_activity = moderate_work_activity_mapping.get(selected_moderate_work_activity)

    # Button to predict
    ok = st.button("Predict")

    if ok:
        if gender is None or moderate_work_activity is None or hip_circumference is None:
            st.warning("Please make valid selections and provide hip circumference before predicting.")
        else:
            # Create a numpy array from the user input
            user_input = np.array([[gender, hip_circumference, moderate_work_activity]])
            user_input = user_input.astype(float)

            # Load model and scaler
            logreg, scaler = load_model_and_scaler()
            
            # Make prediction
            prediction = predict_diabetes(logreg, scaler, user_input)
            
            # Mapping of model outputs to desired strings
            output_mapping = {
                0: ":smiley: Our predictions suggests you may not have diabetes",
                1: ":pensive: Our prediction says you may have diabetes. You can read more about diabetes on [CDC's website](https://www.cdc.gov/diabetes/basics/symptoms.html)"
            }
            
            # Get the corresponding string for the prediction
            predicted_string = output_mapping.get(prediction[0], "Unknown")

            # Display the mapped prediction string using appropriate streamlit function
            if prediction[0] == 1:
                st.error(predicted_string)
            elif prediction[0] == 0:
                st.success(predicted_string)
            else:
                st.subheader(predicted_string)  # Default for any other unexpected values

show_predict_page()
 



    

    

