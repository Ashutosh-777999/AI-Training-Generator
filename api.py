from fastapi import FastAPI
from langchain_community.llms import Ollama

app = FastAPI()
llm = Ollama(model="llama3.2:1b")

@app.get("/chat")
def get_bot_response(message: str):
    response = llm.invoke(message)
    return {"reply": response}