from turtle import st

from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI
import uvicorn

app = FastAPI()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key="AQ.Ab8RN6InLjCTHLdS9UOMh0g87eBToDhLKb5aq61oUqo43hoqhg")

@app.post("/generate-plan")
async def get_plan(topic: str, level: str):
    response = llm.invoke(f"Create a plan for {topic} at {level} level")
    return {"plan": response.content}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)