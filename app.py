import streamlit as st
import requests

# Page Title
st.set_page_config(page_title="Educator Work Companion", layout="wide")
st.title("🎓 Educator Work Companion Agent")

# Sidebar for API Key (Secure Input)
st.sidebar.markdown("---")
st.sidebar.info("Don't have an API Key? [Get one here](https://aistudio.google.com/app/apikey)")
api_key = st.sidebar.text_input("Enter your Google Gemini API Key", type="password")

language = st.selectbox("Select Language:", 
                        ["English", "Hindi", "Odia", "Kannada", "Telugu"])

# Topic & Level Inputs
topic = st.text_input("Enter the topic you want to learn:")
level = st.selectbox("Select your skill level:", ["Beginner", "Intermediate", "Advanced"])

# app.py mein ye badlav karein
if st.button("Generate Learning Plan"):
    if not api_key:
        st.error("Please enter your API Key.")
    else:
        headers = {"user-id": "ashutosh_123", "language": language}
        try:
            # Server ko request tabhi jayegi jab button dabaya jayega
            response = requests.post(
                "http://localhost:8000/get-custom-practice",
                params={"topic": topic, "level": level},
                headers=headers
            )
            if response.status_code == 200:
                st.write(response.json())
            else:
                st.error(f"Error: Server responded with {response.status_code}")
        except Exception as e:
            st.error("Backend server is not running. Please start api.py first.")


headers = {
    "user-id": "ashutosh_123", # Ye string zaroor honi chahiye
    "language": language
}

# Request call karte waqt:
response = requests.post(
    "http://localhost:8000/get-custom-practice", 
    params={"topic": topic, "level": level},
    headers=headers # Ye headers pass karna compulsory hai
)