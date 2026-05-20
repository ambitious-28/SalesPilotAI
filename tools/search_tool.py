from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def enrich_company(company_name):

    query = f"""
    What does {company_name} do?
    What products or services does it offer?
    What business problems does it solve?
    """

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=2
    )

    context = ""

    for result in response["results"]:

        context += result["content"] + "\n"

    return context