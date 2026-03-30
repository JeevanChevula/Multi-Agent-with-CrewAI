# tasks/research_task.py

from crewai import Task
from agents.research_agent import create_research_agent

def create_research_task(topic: str):
    """Creates and returns the research task for a given topic."""
    return Task(
        description=f"""Research the following topic thoroughly: {topic}
        
        Your research must include:
        - Current state and recent developments
        - Key facts, statistics, and data points
        - Major players, organizations, or people involved
        - Important trends and patterns
        - Any controversies or challenges in this area
        
        Use the web search tool multiple times with different search queries 
        to gather comprehensive information from multiple sources.""",
        
        expected_output="""A comprehensive research report containing:
        - All key facts and findings organized by theme
        - Specific data points and statistics where available
        - Source references (title and URL) for major claims
        - At least 5 distinct pieces of information
        - Raw findings presented clearly for the analyst to work with""",
        
        agent=create_research_agent()
    )