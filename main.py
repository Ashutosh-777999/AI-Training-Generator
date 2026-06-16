import os

if __name__ == "__main__":
    os.system("streamlit run app.py")

from fastapi import FastAPI
from app.ai_engine import generate_training_plan

app = FastAPI(title="AI Training Agent API")

@app.get("/get-plan")
async def get_plan(topic: str, level: str):
    plan = generate_training_plan(topic, level)
    return {"status": "success", "data": plan}