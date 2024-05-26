import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
from home_page import home

# Check if Firebase Admin SDK is already initialized
if not firebase_admin._apps:
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate("assets/care-compass-1224f-dbd593f5314a.json")
    firebase_admin.initialize_app(cred)

def sign_up():
    signup_email = st.text_input("Email")
    signup_password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        try:
            user = auth.create_user(
                email=signup_email,
                password=signup_password
            )
            st.success("User created successfully!")
        except:
            st.error(f"Error creating user")
    
def login():
    login_email = st.text_input("Email")
    login_password = st.text_input("Password", type="password")
    if st.button("Login"):
        try:
            user = auth.get_user_by_email(login_email)
            st.session_state.loggedIn = True
            st.session_state.login_email = login_email
        except :
            st.error(f"Error logging in")
    


# Streamlit UI
st.sidebar.title("HealthGuard Access Portal: Your Key to Wellness")

# Initialize session state
if 'loggedIn' not in st.session_state:
    st.session_state.loggedIn = False
    st.session_state.login_email = None

if st.session_state.loggedIn == False:
    page = st.sidebar.radio("Select Page", ("Sign Up", "Login"))
    if page == "Sign Up":
        st.title("Sign Up")
        sign_up()
    
    elif page == "Login":
        st.title("Login")
        login()
else:  
    email = st.session_state.login_email
    home()
        
