import os
import sys
from fastapi import FastAPI

# Force Python to find files in the same directory
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

# Import the module as a whole to avoid naming conflicts
import ai_engine 

app = FastAPI(title="AI Training Agent API")

@app.get("/get-plan")
async def get_plan(topic: str, level: str):
    # Dynamically calling whatever generation logic you have inside ai_engine
    try:
        plan = ai_engine.generate_training_plan(topic, level)
    except AttributeError:
        # Fallback if the function is named differently inside your file
        plan = "Function generate_training_plan not found in ai_engine.py"
    return {"plan": plan}

if __name__ == "__main__":
    # Point directly to the absolute path of app.py so Streamlit doesn't throw a file error
    app_path = os.path.join(current_dir, "app.py")
    print(f"Launching Streamlit pointing to: {app_path}")
    os.system(f"streamlit run \"{app_path}\"")