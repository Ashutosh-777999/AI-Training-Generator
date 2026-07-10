import sqlite3
import uuid
from datetime import datetime

DB_NAME = "chat_history.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            session_id TEXT PRIMARY KEY,
            topic TEXT,
            created_at TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            role TEXT,
            content TEXT,
            timestamp TIMESTAMP,
            FOREIGN KEY(session_id) REFERENCES sessions(session_id)
        )
    ''')
    conn.commit()
    conn.close()

def create_new_session(topic="New Learning Path"):
    session_id = str(uuid.uuid4())
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO sessions (session_id, topic, created_at) VALUES (?, ?, ?)", 
                   (session_id, topic, datetime.now()))
    conn.commit()
    conn.close()
    return session_id

def save_message(session_id, role, content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (session_id, role, content, timestamp) VALUES (?, ?, ?, ?)",
                   (session_id, role, content, datetime.now()))
    conn.commit()
    conn.close()

def get_all_sessions():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT session_id, topic, created_at FROM sessions ORDER BY created_at DESC")
    sessions = cursor.fetchall()
    conn.close()
    return [{"session_id": row[0], "topic": row[1], "created_at": row[2]} for row in sessions]

def get_messages_for_session(session_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT role, content FROM messages WHERE session_id = ? ORDER BY timestamp ASC", (session_id,))
    messages = cursor.fetchall()
    conn.close()
    return [{"role": row[0], "content": row[1]} for row in messages]

def delete_session(session_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM messages WHERE session_id = ?", (session_id,))
    cursor.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))
    conn.commit()
    conn.close()

def setup_training_db():
    conn = sqlite3.connect('tm_bot_database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS training_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            contact_details TEXT,
            training_topic TEXT,
            agreed_date_time TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_training_agreement(user_name, details, topic):
    conn = sqlite3.connect('tm_bot_database.db')
    cursor = conn.cursor()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO training_records (user_name, contact_details, training_topic, agreed_date_time, status)
        VALUES (?, ?, ?, ?, 'Training Allocated')
    ''', (user_name, details, topic, current_time))
    
    conn.commit()
    conn.close()