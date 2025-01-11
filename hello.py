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
    page_title="Gemini-Powered App",
    page_icon="✨",
    layout="wide",
)

# App title
st.title("✨ Gemini-Powered Streamlit App")

# Authenticate the API key
def authenticate_api_key(api_key):
    genai.configure(api_key=api_key)

# User input section
st.subheader("Input Section")
user_input = st.text_area("Enter your prompt:", "")

if st.button("Submit"):
    if not api_key:
        st.error("Please enter your API key in the sidebar.")
    elif not user_input:
        st.warning("Please enter a prompt to submit.")
    else:
        # Call the Gemini API (Google Generative AI)
        with st.spinner("Generating response..."):
            try:
                authenticate_api_key(api_key)
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(user_input)
                st.success("Response generated successfully!")
                st.text_area("Model Response:", response.text, height=200)
            except Exception as e:
                st.error(f"Error: {e}")

# Additional sections for data analysis or visualization
st.subheader("Additional Features")
st.markdown(
    "You can extend this app by adding data visualization, file upload, or other Streamlit features."
)
