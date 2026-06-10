import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.title("⚡ Fast Learning plan Generator with google gemini AI")

st.sidebar.header("🔑 Settings")
api_key = st.sidebar.text_input("Enter Google Gemini API Key:", type="password")
st.sidebar.markdown("[👉 Get your API Key here](https://aistudio.google.com/app/apikey)")

st.sidebar.markdown("---")
selected_language = st.sidebar.selectbox(
    "Select Language:", 
    ["English", "हिन्दी (Hindi)", "తెలుగు (Telugu)", "ଓଡ଼ିଆ (Odia)"]
)

if "topic" not in st.session_state:
    st.session_state.topic = ""
if "levels_text" not in st.session_state:
    st.session_state.levels_text = ""
if "final_plan" not in st.session_state:
    st.session_state.final_plan = ""

topic_input = st.text_input("What do you want to learn? (e.g., LangGraph, AI)", placeholder="Type here...")

if st.button("Find Training Levels 🔍"):
    if not api_key:
        st.error("Please enter your API Key in the sidebar first!")
    elif topic_input:
        st.session_state.topic = topic_input
        st.session_state.final_plan = ""
      
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
        prompt = f"Provide 3 simple learning levels (Beginner, Intermediate, Advanced) for learning {topic_input}. Respond ONLY in {selected_language} language. Keep it brief."
        
        with st.spinner("Finding training levels... Please wait..."):
            response_stream = llm.stream(prompt)
            st.session_state.levels_text = st.write_stream(response_stream)
    else:
        st.warning("Please enter a topic to learn.")
st.markdown("---")

if st.session_state.levels_text:
    selected_level = st.selectbox("Which level would you like to start with?", ["Beginner", "Intermediate", "Advanced"])
    
    if st.button("Create My Training Plan 🚀"):
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
        plan_prompt = f"Create a highly detailed, step-by-step training plan to learn {st.session_state.topic} at a {selected_level} level. Include daily tasks. You MUST respond completely in {selected_language} language."
        
        st.markdown("### 🎯 Your Complete Training Plan:")
        response_stream = llm.stream(plan_prompt)
        st.session_state.final_plan = st.write_stream(response_stream)