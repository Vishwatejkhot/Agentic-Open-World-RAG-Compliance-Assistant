import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
assert os.getenv("GROQ_API_KEY") is not None, "GROQ_API_KEY not loaded"

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)
