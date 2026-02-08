import streamlit as st
from orchestrator import run_pipeline

st.set_page_config(page_title="Agentic Open-World RAG", layout="wide")
st.title("🧠 Agentic Compliance Auditor")

user_input = st.text_area(
    "Describe your company decision",
    placeholder="We want to terminate an employee immediately..."
)

if st.button("Run Audit"):
    result = run_pipeline(user_input)
    st.json(result)
