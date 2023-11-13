import streamlit as st

st.set_page_config(
    page_title = "Homepage", 
    page_icon = "👋",
    layout= "centered"
)

st.title("Welcome to our MDST Project! 👋")

def show_homepage():

    st.subheader("Assess Your Diabetes Risk by Taking Our Survey! 📝")
    st.markdown("""
    This application offers users the chance to complete a brief survey. Based on your responses, we predict the likelihood of you having diabetes - check it out in the sidebar. Our prediction model is trained using data sourced from NHANES.
    
    **What is NHANES?**  
                The National Health and Nutrition Examination Survey (NHANES) is an initiative designed to gauge the health and nutritional status of adults and children across the United States. Through this comprehensive survey, valuable insights into various health concerns are gathered and analyzed, making it an invaluable resource for predictive models like ours.
    
    For more information about NHANES please visit the [NHANES 2017-2020 Website](https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?Cycle=2017-2020)""")
    


    st.subheader("Project Made By:")
    st.markdown("[Tobias Madsen](https://www.linkedin.com/in/tob1asmadsen/), Anthony Hernandez, Elle Chen, Jaegun Song, and Kiley Price")
    st.markdown("*Proud members of [Michigan Data Science Team](https://mdst.club) 🚀*")







show_homepage()