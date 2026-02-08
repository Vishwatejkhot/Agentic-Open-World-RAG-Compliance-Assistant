from agents.context_agent import context_agent
from agents.planner_agent import planner_agent
from agents.rag_agent import rag_agent
from agents.web_agent import web_agent
from agents.arxiv_agent import arxiv_agent
from agents.evidence_agent import evidence_agent
from agents.risk_agent import risk_agent
from agents.mitigation_agent import mitigation_agent
from agents.validation_agent import validation_agent
from agents.final_agent import final_agent

TOOLS = {
    "context": context_agent,
    "planner": planner_agent,
    "rag": rag_agent,
    "web": web_agent,
    "arxiv": arxiv_agent,
    "evidence": evidence_agent,
    "risk": risk_agent,
    "mitigation": mitigation_agent,
    "validation": validation_agent,
    "final": final_agent
}
