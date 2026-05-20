import streamlit as st

from agents.prospect_agent import run_prospecting_agent
from tools.email_tool import send_email

st.set_page_config(
    page_title="AI Prospecting Agent",
    layout="wide"
)

st.title("AI Prospecting Agent")

industry = st.selectbox(
    "Select Industry",
    [
        "saas",
        "healthcare ai",
        "fintech",
        "cybersecurity",
        "edtech"
    ]
)

if st.button("Run Agent"):
    with st.spinner("Running AI Prospecting Workflow..."):
        results = run_prospecting_agent(industry)
        for result in results:
            st.divider()
            st.subheader(result["company_name"])
            st.write(
                f"Contact Person: {result['contact_person']}"
            )
            st.write(
                f"CRM Email: {result['company_email']}"
            )
            with st.expander(
                "Company Enrichment Data"
            ):
                st.write(result["company_info"])


            st.markdown("## Lead Score")

            st.success(
                f"{result['lead_score']}/100"
            )

            st.markdown(
                "### Scoring Factors"
            )

            for factor in result["scoring_factors"]:

                st.write(f"✅ {factor}")


            st.markdown(
                "## Pain Point Analysis"
            )

            st.code(result["analysis"])

            st.markdown(
                "## Generated Outreach"
            )

            edited_email = st.text_area(

                f"Edit Email for {result['company_name']}",

                result["email"],

                height=260
            )

            if st.button(

                f"Approve & Send to {result['company_name']}"
            ):

                email_status = send_email(

                    "yourgmail@gmail.com",

                    f"Opportunity for {result['company_name']}",

                    edited_email
                )

                st.success(email_status)