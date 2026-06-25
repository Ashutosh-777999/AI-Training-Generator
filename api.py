from fastapi import FastAPI
from ai_engine import generate_learning_package

app = FastAPI()

# Part C: Simple Session Tracking (In-memory)
user_progress = {}

@app.post("/get-custom-practice")
async def get_journey(user_id: str, topic: str, level: str):
    # Fetch content
    data = generate_learning_package(topic, level)
    
    # Update progress
    if user_id not in user_progress:
        user_progress[user_id] = []
    user_progress[user_id].append({"topic": topic, "status": "completed"})
    
    return {
        "status": "success",
        "journey_step": len(user_progress[user_id]),
        "learning_content": data
    }