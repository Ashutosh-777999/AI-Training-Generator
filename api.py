from fastapi import FastAPI
from langchain_ollama import ChatOllama
import uvicorn

app = FastAPI()

# (ବାକି ତଳ କୋଡ୍ ସବୁ ସମାନ ରହିବ...)

@app.post("/generate-plan")
async def get_plan(topic: str, level: str, model_name: str = "llama3"):
    # ଏବେ LLM ଫଙ୍କସନ୍ ଭିତରେ ଇନିସିଆଲାଇଜ୍ ହେବ ଏବଂ Ollama ବ୍ୟବହାର କରିବ
    llm = ChatOllama(model=model_name)
    
    prompt = f"Create a plan for {topic} at {level} level in Odia (ଓଡ଼ିଆ) language."
    response = llm.invoke(prompt)
    return {"plan": response.content}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)