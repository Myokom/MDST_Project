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
    
    st.markdown("""
    ***Disclaimer***
                
    Our prediction model is based on a relatively small amount of predictor variables. We understand diabetes is a serious medical condition that can be caused by any number of genetic, health and lifestyle factors therefore we cannot predict whether or not an individual has or will develop diabetes with a high level of certainty. Additionally, the information entered into this application should remain private and will not be stored. This model is simply an interactive way of displaying what we have learned and the knowledge we have gained this semester as members of MDTS :slightly_smiling_face: If you are curious you can check out the code on [Github](https://github.com/Myokom/MDST_Project)""")

    

    st.subheader("Project Made By:")
    st.markdown("[Tobias Madsen](https://www.linkedin.com/in/tob1asmadsen/), [Anthony Hernandez](https://www.linkedin.com/in/a-i-hernandez/), Elle Chen, Jaegun Song, and [Kiley Price](https://www.linkedin.com/in/kiley-price/)")
    st.markdown("*Proud members of [Michigan Data Science Team](https://mdst.club) 🚀*")







show_homepage()