def planner_agent(context: dict):
    """
    Decides which external sources to query.
    """
    return {
        "web_queries": [
            "UK unfair dismissal procedure SME",
            "HR termination legal process UK"
        ],
        "arxiv_queries": [
            "compliance risk assessment framework",
            "AI assisted legal decision support systems"
        ]
    }
