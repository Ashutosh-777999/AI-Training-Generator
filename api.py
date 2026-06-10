from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI

app = FastAPI()
llm = ChatGoogleGenerativeAI(model="gemini-pro")

@app.get("/chat")
def get_bot_response(message: str):
    response = llm.invoke(message)
    return {"reply": response}