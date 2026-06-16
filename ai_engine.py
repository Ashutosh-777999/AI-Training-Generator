from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("AQ.Ab8RN6InLjCTHLdS9UOMh0g87eBToDhLKb5aq61oUqo43hoqhg"))

def generate_training_plan(topic, level):
    prompt = f"Create a detailed training plan for {topic} at {level} level."
    response = llm.invoke(prompt)
    return response.content