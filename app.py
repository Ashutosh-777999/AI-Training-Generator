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

if st.button("Generate Learning Plan"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar!")
    elif not topic:
        st.warning("Please enter a topic.")
    else:
        # API ko call karna (FastAPI backend ko)
        # Note: Aapko apne backend mein API Key pass karne ka mechanism rakhna hoga
        try:
            with st.spinner('Generating content...'):
                # Yahan hum API endpoint ko call kar rahe hain
                response = requests.post(
                    "http://localhost:8000/get-custom-practice", 
                    params={"topic": topic, "level": level}
                )
                
                if response.status_code == 200:
                    data = response.json()['data']
                    
                    # UI Display (Part A & C implementation)
                    st.subheader(f"Learning Plan for: {topic}")
                    st.write(data['explanation'])
                    
                    st.subheader("Practice Websites")
                    for link in data['practice_websites']:
                        st.markdown(f"- [{link}]({link})")
                    
                    st.subheader("Quiz (Test your knowledge)")
                    for i, q in enumerate(data['quiz']):
                        st.write(f"**Q{i+1}:** {q['q']}")
                        st.radio(f"Select answer for Q{i+1}:", q['options'], key=f"q{i}")
                        st.success(f"Correct Answer: {q['answer']}")
                else:
                    st.error("Error connecting to the backend.")
        except Exception as e:
            st.error(f"Error: {e}")