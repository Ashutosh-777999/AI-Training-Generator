import os
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv() # .env file se key load karega

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def generate_learning_package(topic, level):
    # Part A: Learning Outputs ke liye structure
    prompt = f"""
    Create a learning resource for '{topic}' at '{level}' level.
    Return ONLY valid JSON with these keys:
    - "notes": Detailed explanation (string)
    - "quiz": List of 3 questions with answers (list of strings)
    - "links": List of helpful resources (list of strings)
    """
    response = llm.invoke(prompt)
    
    # JSON clean-up
    content = response.content.replace("```json", "").replace("```", "")
    return json.loads(content)

def generate_full_learning_module(topic, level):
    # Prompt ko 'Educator Agent' jaisa banaya gaya hai
    prompt = f"""
    You are an expert Educator Agent. Create a learning module for '{topic}' at '{level}' level.
    Return ONLY valid JSON format:
    {{
        "notes": "Brief explanation of the topic.",
        "Practice_websites": ["https://gemini.google.com/app?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all", "https://www.coursera.org/courseraplus?utm_medium=sem&utm_source=gg&utm_campaign=b2c_india_x_coursera_ftcof_courseraplus_cx_dr_bau_gg_sem_bd-ex_in_all_m_hyb_24-05_x&campaignid=21327429274&adgroupid=162815312357&device=c&keyword=coursera&matchtype=e&network=g&devicemodel=&creativeid=700607287634&assetgroupid=&targetid=kwd-36262515261&extensionid=&placement=&gad_source=1&gad_campaignid=21327429274&gbraid=0AAAAADdKX6b55mt75WI8VaFuOY-8jGw_r&gclid=CjwKCAjw6MPRBhBTEiwAd-7Mr_tfSM1L_oH0vWQYvvE_E8_tzVR1ErHSRlOZmOUQ5sawF-LAAOfmbRoC-owQAvD_BwE","https://www.youtube.com/"],
        "quiz": [
            {{"question": "Q1", "options": ["A", "B", "C", "D"], "answer": "A"}},
            {{"question": "Q2", "options": ["A", "B", "C", "D"], "answer": "B"}}
        ]
    }}
    """
    response = llm.invoke(prompt)
    content = response.content.replace("```json", "").replace("```", "")
    return json.loads(content)