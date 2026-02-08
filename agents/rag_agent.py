from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

_embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

_db = FAISS.load_local("vectorstore", _embeddings, allow_dangerous_deserialization=True)

def rag_agent(query: str):
    """
    Retrieves internal company + law documents.
    """
    docs = _db.similarity_search(query, k=4)
    return [d.page_content for d in docs]
