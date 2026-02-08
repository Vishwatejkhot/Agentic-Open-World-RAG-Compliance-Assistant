def evidence_agent(local_docs, web_results, arxiv_results):
    """
    Merges all evidence sources into one object.
    """
    return {
        "local": local_docs,
        "web": web_results,
        "arxiv": arxiv_results
    }
