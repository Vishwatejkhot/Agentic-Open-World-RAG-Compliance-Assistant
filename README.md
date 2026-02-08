# Agentic-Open-World-RAG-Compliance-Assistant
AI-powered decision support for UK compliance and operational risk.

## Overview

This project is an **agent-based, open-world AI decision-support
system** designed to help UK companies assess **compliance and
operational risk** around high-impact business decisions before they
act.

Rather than relying on a single chatbot response, the system uses a
**multi-agent architecture** that retrieves evidence from multiple
sources, validates its own reasoning, and retries automatically when
information is insufficient.

The goal is **not legal advice**, but early risk awareness and clearer
decision-making for founders and teams.

------------------------------------------------------------------------

## Key Features

-   Agentic architecture with clearly separated responsibilities\
-   Retrieval-Augmented Generation (RAG) over local UK policy and
    regulatory documents\
-   Live web search using Tavily for up-to-date guidance\
-   Academic research grounding via arXiv\
-   Validation and self-checking layer to reduce hallucinations\
-   Auto-retry mechanism when evidence is weak or incomplete\
-   LLM reasoning constrained by retrieved evidence

------------------------------------------------------------------------

## Why UK-Focused?

Employment law, data protection (GDPR), and compliance requirements vary
significantly by jurisdiction.\
Generic AI advice can easily be misleading or incorrect.

By grounding the system in **UK-specific documents and guidance**, the
output is more realistic, relevant, and useful for UK-based founders and
operators.

------------------------------------------------------------------------

## High-Level Architecture

User Input\
↓\
Context Agent\
↓\
Query Planner Agent\
↓\
Local RAG Agent (Policies & Regulations)\
↓\
Web Agent (Live UK Guidance via Tavily)\
↓\
Research Agent (arXiv Papers)\
↓\
Evidence Merger\
↓\
Validation & Retry Layer\
↓\
LLM-Based Risk Analysis\
↓\
LLM-Based Mitigation Suggestions\
↓\
Final Structured Report

------------------------------------------------------------------------

## Tech Stack

-   Python\
-   Groq LLM (LLaMA-3)\
-   LangChain\
-   FAISS\
-   Tavily API\
-   arXiv API\
-   Streamlit

------------------------------------------------------------------------

## Example Use Cases

-   Assessing HR actions such as employee termination\
-   Evaluating employee or customer data handling decisions\
-   Surfacing compliance risks early in startup operations\
-   Exploring research-backed decision-support frameworks

------------------------------------------------------------------------

## Disclaimer

This system is **not a legal advisor** and does not replace professional
legal or compliance advice.\
It is intended purely as a **decision-support and risk awareness tool**.

------------------------------------------------------------------------

## Project Status

This project is an active exploration of:

-   Agentic AI system design\
-   Trustworthy and responsible LLM usage\
-   Validation-driven workflows\
-   Open-world RAG architectures

Feedback and collaboration are welcome.

------------------------------------------------------------------------

## One-Line Summary

An agentic, open-world AI system that helps UK companies surface
compliance and operational risks by combining local document retrieval,
live web search, academic research, and validation-driven LLM reasoning.
