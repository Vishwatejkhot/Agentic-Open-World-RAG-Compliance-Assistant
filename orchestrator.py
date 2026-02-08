from tools.agent_tools import TOOLS

MAX_RETRIES = 3

def run_pipeline(user_input: str):
    context = TOOLS["context"](user_input)
    plan = TOOLS["planner"](context)

    retry_count = 0
    validation_report = None

    while retry_count < MAX_RETRIES:
        # ---- RAG ----
        local_docs = TOOLS["rag"](user_input)

        # ---- WEB ----
        web_results = []
        for q in plan["web_queries"]:
            web_results.extend(
                TOOLS["web"](q)
            )

        # ---- ARXIV ----
        arxiv_results = []
        for q in plan["arxiv_queries"]:
            arxiv_results.extend(
                TOOLS["arxiv"](q)
            )

        # ---- EVIDENCE ----
        evidence = TOOLS["evidence"](
            local_docs,
            web_results,
            arxiv_results
        )

        # ---- VALIDATION ----
        validation_report = TOOLS["validation"](evidence)

        if validation_report["valid"]:
            break  # ✅ success

        # 🔁 Retry logic
        retry_count += 1

        # Adaptive tightening
        plan["web_queries"] = [
            q + " legal guidance site:gov.uk"
            for q in plan["web_queries"]
        ]

        plan["arxiv_queries"] = [
            q + " systematic review"
            for q in plan["arxiv_queries"]
        ]

    # ❌ Final failure
    if not validation_report or not validation_report["valid"]:
        return {
            "status": "FAILED",
            "reason": "Validation failed after retries",
            "validation_issues": validation_report["issues"],
            "retries_attempted": retry_count
        }

    # ---- RISK + MITIGATION ----
    risks = TOOLS["risk"](context, evidence)
    mitigations = TOOLS["mitigation"](risks)

    # ---- FINAL ----
    final_output = TOOLS["final"](context, risks, mitigations)
    final_output["retries_used"] = retry_count

    return final_output
