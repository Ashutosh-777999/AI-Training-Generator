import streamlit as st
import requests

st.title("🎓 Educator Work Companion")

# User se key mangna
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")
topic = st.text_input("Topic:")
level = st.selectbox("Level:", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate"):
    if not api_key:
        st.error("Please enter your API Key first.")
    else:
        # Key ko Header mein bhej rahe hain
        headers = {"x-api-key": api_key}
        response = requests.post(
            "http://localhost:8000/get-custom-practice", 
            params={"topic": topic, "level": level},
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()['data']
            st.write(data['explanation'])
            # ... baaki UI elements yahan add karein
        else:
            st.error("Failed to generate. Check your API Key.")