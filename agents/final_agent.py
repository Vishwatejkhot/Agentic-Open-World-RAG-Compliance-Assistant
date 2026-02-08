import json
from llm.groq_llm import llm

def final_agent(context: dict, risks: dict, mitigations: dict):
    prompt = f"""
You are generating a final compliance report.

Context:
{context}

Risks:
{risks}

Mitigations:
{mitigations}

Rules:
- Return ONLY valid JSON
- Do NOT include markdown
- Do NOT include explanations

Required JSON schema:
{{
  "summary": string,
  "confidence_score": number,
  "risks_identified": array,
  "recommended_actions": array,
  "disclaimer": string
}}
"""

    response = llm.invoke(prompt)

    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {
            "summary": response.content,
            "confidence_score": 0.5,
            "risks_identified": [],
            "recommended_actions": [],
            "disclaimer": "LLM returned unstructured output"
        }
