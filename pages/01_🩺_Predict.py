import streamlit as st
from joblib import load
import numpy as np
import pandas as pd

st.set_page_config(
    page_title = "Predict", 
    page_icon = "🩺",
    layout = "centered"
)

def calculate_bmi_pounds_feet_inches(weight_pounds, height_feet, height_inches):
     total_inches = (height_feet * 12) + height_inches
     height_m = total_inches * 0.0254
     weight_kg = weight_pounds * 0.453592
     if height_m == 0:
         return "Invalid height"
     bmi = weight_kg / (height_m ** 2)
     return bmi
 
def calculate_bmi_metric(weight_kg, height_cm):
     height_m = height_cm / 100  # Convert cm to meters
     if height_m == 0:
         return "Invalid height"
     bmi = weight_kg / (height_m ** 2)
     return bmi

# Function to load your logistic regression model and preprocessor
def load_model_and_preprocessor():
    model = joblib.load('logreg_model.joblib')
    preprocessor = joblib.load('preprocessor.joblib')
    return model, preprocessor



def predict_diabetes(logreg, scaler, user_input):
    """Predicts diabetes based on user input using the given model and scaler."""
    X_scaled = scaler.transform(user_input)
    prediction = logreg.predict(X_scaled)
    return prediction


def show_predict_page():
    st.title("Do you have diabetes or not?  :mending_heart: :hospital:")

    st.write("""### We need some information to make a prediction""")
    
    # User input fields
    st.subheader('Demographic Information 👤')

    # Let user select gender using the human-readable options
    Gender = st.selectbox(
        label = "What gender were you assigned at birth?",
        options = ["Male", "Female"],  # Assuming these were the original categories
        index = None,
        placeholder = "Choose a response...")

    # Age
    Age_Years = st.slider('How old are you?', 0, 80, 25)

    # Race
    Race = st.selectbox(
        label = "What race/ethnicity best describes you?",
        options = ["Mexican American", "Other Hispanic", "Non-Hispanic White", 
                "Non-Hispanic Black", "Non-Hispanic Asian", 
                "Other Race - Including Multi-Racial"],  # Assuming these were the original categories
        index = None,
        placeholder = "Choose a response...")


    st.subheader('Body Measurements 📐')
 
    # User selects the unit system
    unit_system = st.radio("Select the unit system", ['Imperial (pounds, feet, inches)', 'Metric (kilograms, centimeters)'])

    if unit_system == 'Imperial (pounds, feet, inches)':
        weight_pounds = st.number_input('Enter your weight (in pounds):', min_value=1.0, max_value=600.0, step=0.1, value=1.0, placeholder="Type a number...")
        height_feet = st.number_input('Enter your height (feet):', min_value=0, max_value=7, step=1, value=1, placeholder="Type a number...")
        height_inches = st.number_input('Enter your height (additional inches):', min_value=0, max_value=11, step=1, value=1, placeholder="Type a number...")
        BMI_Value = calculate_bmi_pounds_feet_inches(weight_pounds, height_feet, height_inches)
    elif unit_system == 'Metric (kilograms, centimeters)':
        weight_kg = st.number_input('Enter your weight (in kilograms):', min_value=1.0, max_value=300.0, step=0.1, value=1.0, placeholder="Type a number...")
        height_cm = st.number_input('Enter your height (in centimeters):', min_value=50, max_value=250, step=1,  value=50, placeholder="Type a number...")
        BMI_Value = calculate_bmi_metric(weight_kg, height_cm)
    
    Hip_Circumference_cm = st.number_input(
        label = "Hip Circumference (cm)", 
        value = None,
        step = 1,
        placeholder = "Type a number...")
    
    Waist_Circumference_cm = st.number_input(
        label = "Waist Circumference (cm)", 
        value = None,
        step = 1,
        placeholder = "Type a number...")

    st.subheader('Lifestyle 🏄‍♂️🍽️')
    
    # Let user select using the human-readable options    
    Vigorous_work_activity = st.selectbox(
        label = "Does your work involve moderate-intensity activity that causes small increases in breathing or heart rate such as brisk walking or carrying light loads for at least 10 minutes continuously?",
        options = ["Yes", "No"],
        index = None,
        placeholder = "Choose a response...")
    
    Walk_or_bicycle = st.selectbox(
        label="In a typical week, do you walk or use a bicycle for at least 10 minutes continuously to get to and from places?",
        options=["Yes", "No"],  # Assuming these were the original categories
        index = None,
        placeholder="Choose a response...")
    
    Vigorous_recreational_activities = st.selectbox(
        label = "Do you engage in any vigorous sports, fitness, or recreational activities like running or basketball that significantly elevate your breathing or heart rate for at least 10 minutes continuously in a typical week?",
        options = ["Yes", "No"],
        index = None,
        placeholder = "Choose a response...")
    
    Meals_Outside = st.number_input(
        label = "In the past 7 days, how many meals did you get that were prepared away from home in places such as restaurants, fast food places, food stands, grocery stores, or from vending machines?",
        min_value = 0,
        value = None,
        step = 1,
        placeholder = "Type a number...")

    FastFood_Meals = st.number_input(
        label = "Continuation of last question: How many of those meals did you get from a fast-food or pizza place?",
        min_value = 0,
        value = None,
        step = 1,
        placeholder = "Type a number...")
    
    Ready_Eat_Foods_30D = st.number_input(
        label = "How often in the past 30 days did you eat \"ready to eat\" foods like salads, soups, or sandwiches from a grocery store's salad bar or deli counter?",
        min_value = 0,
        value = None,
        step = 1,
        placeholder = "Type a number...")
    
    Frozen_Meals_30D = st.number_input(
        label = "In the past 30 days, how often did you eat frozen meals or frozen pizzas?",
        min_value = 0,
        value = None,
        step = 1,
        placeholder = "Type a number...")
    
    Past_12_Mo_Alco = st.select_slider(
        label="How frequently have you drunk alcoholic beverages in the past 12 months",
        options=[
            "Every day", 
            "Nearly every day", "3 to 4 times a week", 
            "2 times a week",
            "Once a week", 
            "2 to 3 times a month", "Once a month",
            "7 to 11 times in the last year", 
            "3 to 6 times in the last year",
            "1 to 2 times in the last year", 
            "Never in the last year"])

    # Button to predict
    ok = st.button("Predict")

    if ok:
        if (Past_12_Mo_Alco is None or FastFood_Meals is None or Meals_Outside is None or Vigorous_recreational_activities is None 
            or Walk_or_bicycle is None or Vigorous_work_activity is None or Waist_Circumference_cm is None 
            or Hip_Circumference_cm is None or Race is None or Gender is None):


            st.warning("Please make valid selections and provide hip circumference before predicting.")
        else:
                # Create a DataFrame from the user input
            user_input_df = pd.DataFrame([[Meals_Outside, FastFood_Meals, Ready_Eat_Foods_30D, 
                                           Frozen_Meals_30D, Gender, Age_Years, 
                                           Race, Vigorous_work_activity, Walk_or_bicycle, Vigorous_recreational_activities, 
                                           BMI_Value, Waist_Circumference_cm, Hip_Circumference_cm, Past_12_Mo_Alco]], 
                                           
                                           columns=['Meals_Outside', 'FastFood_Meals', 'Ready_Eat_Foods_30D', 
                                                    'Frozen_Meals_30D', 'Gender', 'Age_Years', 
                                                    'Race', 'Vigorous_work_activity', 'Walk_or_bicycle', 'Vigorous_recreational_activities', 
                                                    'BMI_Value', 'Waist_Circumference_cm', 'Hip_Circumference_cm', 'Past_12_Mo_Alco'])
            
            # Load the logistic regression model
            logreg = load('logistic_regression_model.joblib')

            # Load the preprocessor
            preprocessor = load('preprocessor.joblib')

            # Preprocess the user input
            user_input_preprocessed = preprocessor.transform(user_input_df)

            # Make prediction
            prediction = logreg.predict(user_input_preprocessed)

            
            # Display the prediction
            if prediction[0] == 1:
                st.error(":pensive: Our prediction says you may have diabetes. You can read more about diabetes on [CDC's website](https://www.cdc.gov/diabetes/basics/symptoms.html)")
            else:
                st.success(":smiley: Our predictions suggest you may not have diabetes")


show_predict_page()
 



    

    

