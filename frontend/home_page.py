import streamlit as st
from custom_food_recommendation import main as custom_recommendation
from symptom_diagnoser import medichat_app
from mental_health import peacepal_app
from profile_page import profile_page
from nearby_places import nearby_places_app

def home():
    st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
    )
    st.markdown("<h1 style='color:#8E7AB5'>Optimize Your Well-being</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#B784B7'>Personal Healthcare & Self-care Regimen</h2>", unsafe_allow_html=True)

    
    option = st.sidebar.selectbox("Choose a service", ["Profile", "Medi-Chat", "PeacePal", "Meal-Maker", "Near-Me"])

    if option == "Profile":
        profile_page()
    elif option == "Medi-Chat":
        medichat_app()
    elif option == "PeacePal":
        peacepal_app()
    elif option == "Meal-Maker":
        custom_recommendation()
    elif option == "Near-Me":
        nearby_places_app()

if __name__ == "__main__":
    home()
