FROM python:3.11
WORKDIR /app
COPY . .
# langchain-google-genai ବଦଳରେ langchain-community ଦିଆଗଲା 
RUN pip install fastapi uvicorn langchain-community streamlit pysqlite3
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]