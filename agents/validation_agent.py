def validation_agent(evidence: dict):
    """
    Validates grounding and trustworthiness.
    """
    issues = []

    # Local RAG grounding
    if not evidence["local"]:
        issues.append("Missing internal/legal documents")

    # Web grounding
    if len(evidence["web"]) < 2:
        issues.append("Insufficient independent web sources")

    for w in evidence["web"]:
        if not w.get("url"):
            issues.append("Web evidence missing citation URL")

    # Research grounding
    if not evidence["arxiv"]:
        issues.append("No academic research (arXiv) evidence")

    if issues:
        return {
            "valid": False,
            "issues": issues
        }

    return {"valid": True}
