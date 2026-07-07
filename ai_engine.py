from langchain_ollama import ChatOllama

# Ollama କୁ ଇନିସିଆଲାଇଜ୍ କରାଗଲା 
llm = ChatOllama(model="llama3")

# (ବାକି ତଳ କୋଡ୍ ସବୁ ସମାନ ରହିବ...)
def generate_learning_package(topic: str, level: str):
    prompt = f"Create a complete learning package with examples for {topic} at a {level} level. Respond ENTIRELY in Odia (ଓଡ଼ିଆ) language."
    response = llm.invoke(prompt)
    return response.content

def generate_training_plan(topic: str, level: str):
    prompt = f"Create a detailed training plan for {topic} at a {level} level. Respond ENTIRELY in Odia (ଓଡ଼ିଆ) language."
    response = llm.invoke(prompt)
    return response.content