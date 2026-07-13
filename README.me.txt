TM Knowledge Bot (AI Master Tutor)
TM Knowledge Bot is an advanced AI-powered tutoring and chat assistant built with Python. It utilizes a FastAPI backend and a Streamlit frontend to deliver personalized learning experiences and casual conversations. The application is powered by local large language models (LLMs) via Ollama, ensuring data privacy and fast local processing. 
Features
* Dual Bot Modes: Users can select between "?? Casual Chat" for general conversations and "?? Study Masterclass" for guided learning. 
* Multi-language Support: The bot can output responses in English, Odia, Hindi, Bengali, and Spanish. 
* Structured Learning Paths: Generates custom study schedules, breaks down topics into Beginner, Intermediate, and Advanced levels, and provides deep explanations. 
* Automated Assessments: Generates 3-question Multiple Choice Quizzes (MCQs) to evaluate the user's understanding of the generated lessons. 
* Downloadable Study Materials: Compiles and allows users to download Main Study Notes (.md) and Practice Quizzes (.md). 
* Custom Certificates: Dynamically generates and downloads an HTML Certificate of Completion utilizing the local logo.png file. 
* Session Management: Automatically saves chat history and learning sessions to a local SQLite database (chat_history.db), allowing users to resume past topics. 
* Email Notifications: Includes an automated SMTP email function to notify users of their allocated training schedules. 
Technology Stack
* Frontend: Streamlit (with custom CSS for Light ?? and Dark ?? themes). 
* Backend: FastAPI and Uvicorn. 
* AI & LLM Orchestration: Langchain (Langchain Community / ChatOllama). 
* Local AI Engine: Ollama (utilizing llama3 and llama3.2:1b models). 
* Database: SQLite3 (chat_history.db and tm_bot_database.db). 
* Containerization: Docker. 
Prerequisites
* Python 3.11 or higher. 
* Ollama installed and running locally on your machine. 
* A valid image file named exactly logo.png placed in the root directory for the application's branding to load properly. 
Installation & Setup
Local Setup
1. Pull the Local LLM: Open your terminal and ensure Ollama is running the required model. 
Bash
ollama run llama3
2. Install Dependencies: Install the required Python packages. 
Bash
pip install fastapi uvicorn langchain-community streamlit pysqlite3
3. Add Branding: Ensure you have placed your logo.png file in the root folder. 
4. Run the Application: You can launch the FastAPI and Streamlit servers together via the main script. 
Bash
python main.py
Docker Setup
The project includes a Dockerfile for easy containerization. 
1. Build the Docker Image:
Bash
docker build -t tm-knowledge-bot .
2. Run the Container:
Bash
docker run -p 8000:8000 tm-knowledge-bot
Database Structure
The application automatically initializes the necessary SQLite databases on startup. 
* sessions Table: Stores unique session_id, topic, and created_at timestamps. 
* messages Table: Stores the chat context linking back to the session ID, distinguishing between user and assistant roles. 
* training_records Table: Captures user names, contact details, agreed dates, and allocation statuses. 

