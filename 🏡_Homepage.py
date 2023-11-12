import streamlit as st

st.set_page_config(
    page_title = "Homepage", 
    page_icon = "👋",
    layout= "centered"
)

st.title("Welcome to our MDST Project! 👋")

def show_homepage():

    st.subheader("Discover Your Diabetes Risk with a Click! :mag:")
    st.markdown("""
    This application offers users the chance to complete a brief survey. Based on your responses, we predict the likelihood of you having diabetes. Our prediction model is trained using data sourced from NHANES.
    
    **What is NHANES?**  
    The National Health and Nutrition Examination Survey (NHANES) is an initiative designed to gauge the health and nutritional status of adults and children across the United States. Through this comprehensive survey, valuable insights into various health concerns are gathered and analyzed, making it an invaluable resource for predictive models like ours.
    """)
    
    st.header("Reference")
    st.markdown("[NHANES 2017-2020](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2017-2020)")




show_homepage()