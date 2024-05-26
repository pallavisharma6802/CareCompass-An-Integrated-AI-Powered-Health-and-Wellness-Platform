import streamlit as st
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests
import webbrowser

def get_nearby_places(location, place_type,city):    
   
    try:
        url = f'https://www.google.com/maps/search/{place_type}+in+{location}+{city}/'
        webbrowser.open_new_tab(url)
    except Exception as e:
        st.write(f"Error: {e}")


def nearby_places_app():
    st.title("Nearby Places Suggestion")

    # User input for location and place type
    location = st.text_input("Enter your location (e.g., street name):")
    city = st.text_input("Enter your city (e.g., Mumbai):")
    place_type = st.selectbox("Select the type of place:", ["Hospital", "Clinic", "Pharmacy", "Children's Hospital", "Blood Donation Centers", "Diagnostic Centers" , "Home Health Agencies", "Ayurveda Clinic", "Homeopathy", "Skin and Hair Clinic", "Other" ])
    if place_type == "Other":
        place_type = st.text_input("Enter place you wish to search nearby:")
    # Button to trigger the nearby places suggestion
    if st.button("Get Nearby Places"):
        get_nearby_places(location, place_type,city)