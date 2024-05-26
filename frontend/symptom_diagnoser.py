import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import streamlit as st

# Load environment variables
load_dotenv()


GOOGLE_API_KEY = "AIzaSyBJXKvhgHCL36qcmydRHkyZ_ls3tLNsMCQ"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

if "chat_session" not in st.session_state:
    st.session_state.chat_session = None
# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])



def medichat_app():
    # Display the chatbot's title on the page
    st.header("‍⚕️ MediChat - Your Medical Assistant")

    # Ensure chat_session is initialized in session_state
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = None

    # Initialize chat session if not already present
    if st.session_state.chat_session is None:
        # Configure model here if needed (assuming model setup happens elsewhere)
        model = gen_ai.GenerativeModel('gemini-pro')
        st.session_state.chat_session = model.start_chat(history=[])

    # Display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input fields for user's symptoms, number of days, prior medications, and allergies
    symptoms = st.text_input("Symptoms (comma-separated)", "")
    days_suffering = st.number_input("Number of days facing symptoms", value=0)
    prior_medications = st.text_input("Prior medications", "")
    allergies = st.text_input("Allergies", "")

    # Concatenate inputs into a prompt
    prompt = f"I have {symptoms} for the past {days_suffering} days and am taking {prior_medications} medication. I also have allergies to {allergies}."

    if st.button("Consult MediChat"):
        # Display user's prompt
        #st.chat_message("user").markdown(prompt)

        # Send user's prompt to Gemini-Pro and get the response
        gemini_response = st.session_state.chat_session.send_message(prompt)

        # Display Gemini-Pro's response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)