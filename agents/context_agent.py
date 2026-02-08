def context_agent(user_input: str):
    """
    Extracts high-level context from user input.
    Kept deterministic on purpose.
    """
    return {
        "decision_type": "HR / Compliance decision",
        "jurisdiction": "UK",
        "company_type": "SME",
        "risk_domains": ["employment_law", "data_protection"]
    }
