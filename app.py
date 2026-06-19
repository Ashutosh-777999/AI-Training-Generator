import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Page configuration for a better web app UI
st.set_page_config(page_title="Fast AI Training Generator", page_icon="⚡", layout="centered")

st.title("⚡ Fast AI Training Plan Generator")

# 2. Sidebar Settings
st.sidebar.header("🔑 Settings")
api_key = st.sidebar.text_input("Enter Google Gemini API Key:", type="password")
st.sidebar.markdown("[👉 Get your Free API Key Here](https://aistudio.google.com/app/apikey)")

st.sidebar.markdown("---")
selected_language = st.sidebar.selectbox(
    "Select Output Language:", 
    ["English", "Hindi", "Telugu", "Odia", "Spanish", "French"]
)

# 3. Session State Initialization (so data doesn't disappear on web reload)
if "topic" not in st.session_state:
    st.session_state.topic = ""
if "levels_text" not in st.session_state:
    st.session_state.levels_text = ""
if "final_plan" not in st.session_state:
    st.session_state.final_plan = ""

# 4. Main Input Area
topic_input = st.text_input(
    "What do you want to learn? (e.g., Agentic AI, LangChain, Python)", 
    placeholder="Type a technology or subject here..."
)

# 5. Search Levels Button
if st.button("Search Training Levels 🔍"):
    if not api_key:
        st.error("Please enter your Google Gemini API Key in the sidebar first!")
    elif topic_input:
        st.session_state.topic = topic_input
        st.session_state.final_plan = ""
        
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
        prompt = f"Provide 3 simple learning levels (Beginner, Intermediate, Advanced) for learning {topic_input}. Respond ONLY in {selected_language} language. Keep it brief and to the point."
        
        with st.spinner("Fetching latest data... Please wait..."):
            # Streaming ensures the user sees the reply immediately without waiting
            response_stream = llm.stream(prompt)
            st.session_state.levels_text = st.write_stream(response_stream)
    else:
        st.warning("Please enter a topic/technology name to proceed.")

st.markdown("---")

# 6. Generate Final Plan Section
if st.session_state.levels_text:
    selected_level = st.selectbox("Which level do you want to start from?", ["Beginner", "Intermediate", "Advanced"])
    
    if st.button("Generate My Training Plan 🚀"):
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
        
        # Upgraded prompt to fetch modern, up-to-date, real-world tasks
        plan_prompt = f"""Act as an expert technical trainer. Create a highly detailed, up-to-date, step-by-step training plan to learn {st.session_state.topic} at a {selected_level} level. 
        Include:
        - Daily tasks and timelines
        - Modern tools and current industry standards
        - Real-world project ideas
        You MUST respond completely in {selected_language} language. Use clean Markdown formatting."""
        
        st.markdown(f"### 🎯 Your Comprehensive {selected_level} Training Plan for {st.session_state.topic}:")
        
        with st.spinner("Generating your fast and updated plan..."):
            response_stream = llm.stream(plan_prompt)
            st.session_state.final_plan = st.write_stream(response_stream)