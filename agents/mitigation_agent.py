from llm.groq_llm import llm

def mitigation_agent(risks: dict):
    """
    Uses Groq to suggest mitigations.
    """

    prompt = f"""
You are a compliance advisor.

Identified risks:
{risks}

Rules:
- Suggest practical mitigation steps
- Align with UK SME practices
- No legal advice language

Return a bullet list.
"""

    response = llm.invoke(prompt)

    return {
        "actions": response.content
    }

