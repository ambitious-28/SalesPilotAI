from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from data.companies import COMPANIES

from tools.search_tool import enrich_company
from tools.scoring_tool import calculate_lead_score

from prompts.email_prompt import EMAIL_PROMPT
from prompts.scoring_prompt import SCORING_PROMPT

from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

parser = StrOutputParser()


def run_prospecting_agent(industry):
    industry = industry.lower().strip()
    if industry not in COMPANIES:
        return []

    companies = COMPANIES[industry]
    final_output = []

    for company in companies:
        company_name = company["name"]
        contact_person = company["contact_person"]
        company_email = company["email"]

        print(f"\nEnriching company: {company_name}")

        company_content = enrich_company(company_name)

        lead_score_data = calculate_lead_score(
            company_content
        )

        lead_score = lead_score_data["score"]

        scoring_factors = lead_score_data["factors"]

        scoring_prompt = PromptTemplate(
            template=SCORING_PROMPT,
            input_variables=["company_data"]
        )

        scoring_chain = scoring_prompt | llm | parser

        analysis_result = scoring_chain.invoke({
            "company_data": company_content
        })

        email_prompt = PromptTemplate(
            template=EMAIL_PROMPT,
            input_variables=[
                "contact_person",
                "company_name",
                "company_description",
                "pain_points"
            ]
        )

        email_chain = email_prompt | llm | parser

        email_result = email_chain.invoke({
            "contact_person": contact_person,
            "company_name": company_name,
            "company_description": company_content,
            "analysis": analysis_result
        })

        final_output.append({
            "company_name": company_name,
            "contact_person": contact_person,
            "company_email": company_email,
            "company_info": company_content,
            "lead_score": lead_score,
            "scoring_factors": scoring_factors,
            "analysis": analysis_result,
            "email": email_result
        })

    return final_output