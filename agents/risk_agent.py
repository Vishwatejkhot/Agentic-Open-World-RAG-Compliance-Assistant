from llm.groq_llm import llm

def risk_agent(context: dict, evidence: dict):
    """
    Uses Groq LLM to identify risks based ONLY on provided evidence.
    """

    prompt = f"""
You are a compliance risk analyst.

Context:
{context}

Evidence (DO NOT invent anything):
Local documents:
{evidence["local"]}

Web sources:
{[w["content"] for w in evidence["web"]]}

Research papers:
{[a["summary"] for a in evidence["arxiv"]]}

Rules:
- Identify risks strictly from evidence
- Cite evidence explicitly
- Do not hallucinate

Return JSON with:
- risk name
- severity
- justification
"""

    response = llm.invoke(prompt)

    return {
        "risks": response.content
    }
