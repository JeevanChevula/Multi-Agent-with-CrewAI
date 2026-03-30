# agents/research_agent.py

from crewai import Agent
from config.llm_config import get_llm
from tools.tavily_tool import web_search_tool

def create_research_agent():
    """Creates and returns the Researcher agent."""
    return Agent(
        role="Senior Research Specialist",
        goal="Find accurate, comprehensive, and up-to-date information on the given topic from reliable web sources",
        backstory="""You are an experienced research specialist with years of expertise 
        in gathering information from across the web. You have a keen eye for credible 
        sources and know how to find the most relevant and current information quickly. 
        You always provide thorough, well-sourced research that others can build upon.""",
        tools=[web_search_tool],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False
    )