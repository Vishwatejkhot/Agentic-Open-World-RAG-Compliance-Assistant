import arxiv

def arxiv_agent(query: str):
    """
    Fetches academic research from arXiv.
    """
    search = arxiv.Search(
        query=query,
        max_results=3,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []
    for r in search.results():
        papers.append({
            "title": r.title,
            "summary": r.summary[:500],
            "authors": [a.name for a in r.authors],
            "pdf": r.pdf_url
        })

    return papers
