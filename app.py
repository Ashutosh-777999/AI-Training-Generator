import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key="AQ.Ab8RN6Iw2iydQVUGpe17BtqORp2caZrDU-r9JqONPmObszVU9g")
st.title("⚡Fast learning plan generator for any topic!")

api_key = st.sidebar.text_input("Enter Google Gemini API Key:", type="password")
st.sidebar.markdown("[👉 Get your API Key here](https://aistudio.google.com/app/apikey)")
st.sidebar.header("Language Settings 🌐")
selected_language = st.sidebar.selectbox(
    "Select Language:", 
    ["English", "हिन्दी (Hindi)", "తెలుగు (Telugu)", "ଓଡ଼ିଆ (Odia)"]
)

st.write(f"Current Language: **{selected_language}**")
st.markdown("---")


if "topic" not in st.session_state:
    st.session_state.topic = ""
if "levels_text" not in st.session_state:
    st.session_state.levels_text = ""
if "final_plan" not in st.session_state:
    st.session_state.final_plan = ""

topic_input = st.text_input("What do you want to learn?", placeholder="Type here...")


if st.button("Find Learning Levels 🔍"):
    if topic_input:
        st.session_state.topic = topic_input
        st.session_state.final_plan = "" 
        
     
        prompt = f"Provide 3 simple learning levels (Beginner, Intermediate, Advanced) for learning {topic_input}. Respond ONLY in {selected_language} language. Keep it brief."
        
        with st.spinner("Finding learning levels..."):
        
            response_stream = llm.stream(prompt)
            st.session_state.levels_text = st.write_stream(response_stream)
    else:
        st.warning("Please enter a topic to learn.")

st.markdown("---")

if st.session_state.levels_text:
    selected_level = st.selectbox(
        "What level would you like to start with?", 
        ["Beginner", "Intermediate", "Advanced"]
    )
    
    if st.button("Generate My Training Plan 🚀"):
        plan_prompt = f"Create a highly detailed, step-by-step training plan to learn {st.session_state.topic} at a {selected_level} level. Include daily tasks. You MUST respond completely in {selected_language} language."
        
        st.markdown("### 🎯 Your Training Plan:")

        response_stream = llm.stream(plan_prompt)
        st.session_state.final_plan = st.write_stream(response_stream)