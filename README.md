# SalesPilotAI

AI-Powered CRM Prospecting & Sales Workflow Automation System

---

## Overview

SalesPilotAI is a Generative AI-powered prospecting workflow designed to automate lead enrichment, operational analysis, lead scoring, and personalized outreach generation for sales teams.

The system simulates a CRM-integrated enterprise sales workflow where company leads are enriched using real-time web context, analyzed using LLMs, scored using explainable business rules, and converted into personalized outreach emails with human approval before execution.

This project demonstrates practical enterprise GenAI concepts such as:
- AI workflow orchestration
- Lead enrichment pipelines
- Explainable AI
- Human-in-the-loop systems
- Personalized LLM generation
- Enterprise automation workflows

---

# Problem Statement

Sales teams spend significant time:
- researching companies
- understanding business operations
- identifying operational pain points
- qualifying leads
- writing personalized outreach emails

This process is repetitive, difficult to scale, and often inconsistent.

SalesPilotAI automates large parts of this workflow using AI-assisted orchestration while still maintaining human oversight before execution.

---

# Key Features

- CRM-style structured lead management
- Tavily-powered company enrichment
- LLM-based operational analysis
- Rule-based explainable lead scoring
- Personalized AI-generated outreach emails
- Human approval before sending emails
- Streamlit-based interactive UI
- Modular LangChain workflow architecture

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| LangChain | Workflow orchestration |
| Groq + Llama 3.3 | LLM inference |
| Tavily API | Retrieval & enrichment |
| Streamlit | Frontend/UI |
| Resend API | Email delivery |
| dotenv | Environment variable management |

---

# Architecture

```text
Mock CRM Leads
        ↓
Tavily Enrichment Layer
        ↓
LLM Operational Analysis
        ↓
Rule-Based Lead Scoring
        ↓
Personalized Email Generation
        ↓
Human Approval
        ↓
Email Sending
```

---

# How the System Works

## 1. CRM Lead Input

The system starts with seeded CRM-style lead data containing:
- company names
- contact persons
- email addresses

This simulates enterprise CRM records.

---

## 2. Company Enrichment

Tavily is used as the retrieval layer to gather contextual business information about companies from the web.

This enrichment step improves downstream reasoning and personalization quality.

Example:
- company operations
- products/services
- workflow complexity
- operational context

---

## 3. Operational Analysis

The enriched context is passed to an LLM which analyzes:
- operational inefficiencies
- workflow bottlenecks
- automation opportunities
- business relevance

---

## 4. Lead Scoring

The system uses deterministic rule-based scoring for:
- consistency
- explainability
- enterprise reliability

Scoring signals include:
- AI relevance
- workflow complexity
- enterprise scale
- SaaS fit
- operational management indicators

---

## 5. Personalized Outreach Generation

The LLM generates personalized sales outreach emails based on:
- company context
- operational analysis
- workflow challenges
- automation opportunities

---

## 6. Human-in-the-Loop Approval

Before execution:
- generated emails can be reviewed
- edited manually
- approved before sending

This aligns with enterprise AI governance and operational safety practices.

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/SalesPilotAI.git

cd SalesPilotAI
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

TAVILY_API_KEY=your_tavily_api_key

RESEND_API_KEY=your_resend_api_key
```

---

# Running the Application

```bash
streamlit run app.py
```

---

# APIs Used

## Groq API

Used for:
- fast LLM inference
- operational analysis
- email generation

Model:
- `llama-3.3-70b-versatile`

---

## Tavily API

Used for:
- retrieval
- company enrichment
- contextual business intelligence

## Resend API

Used for:
- transactional email delivery
- sending AI-generated outreach emails
- workflow execution layer
