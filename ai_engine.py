from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

# ୧. ଆପଣଙ୍କ ମଡେଲ୍ ସେଟଅପ୍ କରନ୍ତୁ (ଯଦି ଆପଣ ଲାମା-୩ ବ୍ୟବହାର କରୁଛନ୍ତି)
llm = ChatOllama(model="llama3") 


# ==========================================
# ୧. STRICT TOPIC EXTRACTOR (ସାର୍ଟିଫିକେଟ୍ ପାଇଁ)
# ==========================================
topic_extractor_template = """
You are a strict text parser. Extract ONLY the core subject from the text.
Text: "{user_input}"

RULES:
1. Remove filler words like "I want to learn", "today", "teach me", etc.
2. Output absolutely NOTHING ELSE except the subject name (e.g. "Frontend Development", "Python").
3. Format in Title Case.

Subject:
"""

topic_prompt = PromptTemplate(
    input_variables=["user_input"],
    template=topic_extractor_template
)

def get_clean_topic(user_input: str):
    """ୟୁଜର୍ ର ବାକ୍ୟରୁ କେବଳ ଟପିକ୍ ବାହାର କରିବ ସାର୍ଟିଫିକେଟ୍ ପାଇଁ"""
    chain = topic_prompt | llm
    response = chain.invoke({"user_input": user_input})
    # ସ୍ପେସ୍ ଏବଂ ଏକ୍ସଟ୍ରା ଲାଇନ୍ କାଟିବା ପାଇଁ strip() ବ୍ୟବହାର ହେଉଛି
    return response.content.strip()


# ==========================================
# ୨. STRICT EXPLANATION ENGINE (ଲେଭେଲ୍ ଅନୁସାରେ ଡିଟେଲ୍ ଏକ୍ସପ୍ଲାନେସନ୍)
# ==========================================
explanation_template = """
You are a highly advanced technical expert teaching a student. 

Course Level Selected: {selected_level}
Current Topic to Explain: {current_topic}

CRITICAL INSTRUCTIONS:
1. STRICT LEVEL ADHERENCE: You MUST explain this topic matching the '{selected_level}' level. 
   - If the level is 'Advanced' or 'Intermediate', DO NOT write beginner stuff. Explain deep, complex concepts directly related to '{current_topic}'.
2. FOCUS ONLY ON THIS TOPIC: Do not explain the next topics in the syllabus. Only explain '{current_topic}'.
3. VAST EXPLANATION: Write a comprehensive, textbook-style explanation. Use deep theory, real-world architecture, and advanced code snippets where applicable. Do NOT use short summaries.

Explain the topic deeply now:
"""

explanation_prompt = PromptTemplate(
    input_variables=["selected_level", "current_topic"],
    template=explanation_template
)

def generate_topic_explanation(level: str, topic: str):
    """ଦିଆଯାଇଥିବା ଟପିକ୍ ଏବଂ ଲେଭେଲ୍ ଅନୁସାରେ ବିସ୍ତୃତ ବର୍ଣ୍ଣନା କରିବ"""
    chain = explanation_prompt | llm
    response = chain.invoke({
        "selected_level": level,
        "current_topic": topic
    })
    return response.content


# ==========================================
# ୩. SYSTEM TEMPLATE (ଭାଷ୍ଟ୍ ଷ୍ଟଡି ମ୍ୟାଟେରିଆଲ୍)
# ==========================================
system_template = """
You are a highly advanced and expert technical tutor. 
The user wants to learn a specific subject at a specific difficulty level.

Subject: {subject}
Selected Level: {level}

STRICT INSTRUCTIONS YOU MUST FOLLOW:
1. STRICT LEVEL ADHERENCE: You MUST ONLY provide topics that strictly match the '{level}' level. 
   - If the level is 'Intermediate' or 'Advanced', DO NOT include basic topics like Introduction, basic syntax, variables, or simple loops. Start directly with complex concepts appropriate for that level.
   
2. VAST AND COMPREHENSIVE EXPLANATION: Do NOT give short notes, bullet points, or simple tables. 
   - Explain each topic like a comprehensive textbook. 
   - Provide in-depth paragraphs, deep theoretical explanations, and real-world use cases.
   - Include multiple detailed code examples for each concept to make it crystal clear.
   
3. MORE TOPICS: Provide a wide and exhaustive list of topics (at least 6-8 deep topics) relevant to the {level} level. 

Generate the highly detailed, book-like study material now:
"""

prompt = PromptTemplate(
    input_variables=["subject", "level"],
    template=system_template
)

chain = prompt | llm

def generate_study_material(subject: str, level: str):
    """
    ଏହି ଫଙ୍କସନ୍ ୟୁଜର୍ ର ସବଜେକ୍ଟ ଏବଂ ଲେଭେଲ୍ ନେଇ ଡିଟେଲ୍ କଣ୍ଟେଣ୍ଟ ଦେବ।
    """
    print(f"Generating vast {level} level content for {subject}...")
    response = chain.invoke({
        "subject": subject,
        "level": level
    })
    return response.content


# ==========================================
# ୪. SCHEDULE EXPLANATION TEMPLATE (ଟାଇମ୍ ଟେବୁଲ୍ ପାଇଁ)
# ==========================================
schedule_explanation_template = """
You are an expert technical tutor. You have already provided the following study schedule to the user:
{syllabus_schedule}

The user has now started their learning journey. 

Current Progress: {current_week_and_day}
Topic to teach now: {current_topic}

STRICT INSTRUCTIONS:
1. ONLY explain the topic mentioned above ({current_topic}) for the current day. DO NOT explain the next days or the rest of the syllabus yet.
2. VAST & IN-DEPTH EXPLANATION: Explain this specific topic like a comprehensive textbook chapter. Do not use short bullet points. Write deep theoretical concepts, practical use-cases, and provide multiple code examples.
3. CONTEXT: Connect this topic slightly to what they are supposed to learn in this schedule, but keep the focus 100% on teaching today's topic.
4. ENDING: At the end of your explanation, explicitly ask the user: "Type 'Next' to move to the next topic in your schedule."

Generate the detailed lesson for today:
"""

schedule_explanation_prompt = PromptTemplate(
    input_variables=["syllabus_schedule", "current_week_and_day", "current_topic"],
    template=schedule_explanation_template
)

# ଉଦାହରଣ ସ୍ୱରୂପ:
# response = (schedule_explanation_prompt | llm).invoke({
#     "syllabus_schedule": saved_syllabus_text,
#     "current_week_and_day": "Week 1, Monday",
#     "current_topic": "Introduction to Backend Development"
# })


# ଟେଷ୍ଟିଂ ପାଇଁ ଉଦାହରଣ (ଏହାକୁ ଡିଲିଟ୍ କରିପାରିବେ ଆପଣଙ୍କ ମେନ୍ କୋଡରେ ବ୍ୟବହାର କଲା ବେଳେ)
if __name__ == "__main__":
    # user_subject = "Python"
    # user_level = "Intermediate"
    # result = generate_study_material(user_subject, user_level)
    # print(result)
    pass
