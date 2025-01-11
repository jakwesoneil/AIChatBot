import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the variables
api_key = os.getenv("API_KEY")

# Set up the page configuration
st.set_page_config(
    page_title="Internet Helper - Gemini AI",
    page_icon="🌐",
    layout="wide",
)

# App title
st.title("🌐 Internet Connection Helper - Powered by Gemini AI")

# Authenticate the API key
def authenticate_api_key(api_key):
    genai.configure(api_key=api_key)

# Generate response as an internet connection helper
def generate_response(api_key, user_input):
    authenticate_api_key(api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    # Prefix the user input with the purpose for better alignment
    prompt = (
        "You are an AI chatbot. Your purpose is to help users with their internet connection concerns."
        "Provide clear, concise, and helpful responses in a friendly tone with empathy.\n\n"
        f"User's concern: {user_input}"
    )
    return model.generate_content(prompt)

# User input section
st.subheader("Describe Your Internet Issue")
user_input = st.text_area("Enter your concern about your internet connection:", "")

if st.button("Get Help"):
    if not api_key:
        st.error("Please set your API key in the .env file.")
    elif not user_input:
        st.warning("Please describe your internet issue before submitting.")
    else:
        # Call the Gemini API
        with st.spinner("Generating helpful advice..."):
            try:
                response = generate_response(api_key, user_input)
                st.success("Here's some advice for your issue!")
                with st.container(border=True):
                    st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
