# tasks/analysis_task.py

from crewai import Task
from agents.analyst_agent import create_analyst_agent

def create_analysis_task(topic: str):
    """Creates and returns the analysis task for a given topic."""
    return Task(
        description=f"""Analyze the research findings provided to you about: {topic}
        
        Your analysis must include:
        - Identify the most important and relevant findings
        - Extract key patterns and trends from the data
        - Highlight any contradictions or gaps in the research
        - Assess the significance of the findings
        - Draw meaningful conclusions that go beyond surface-level observations
        
        Work strictly from the research provided to you. 
        Do not search for new information — your job is to think deeply 
        about what the Researcher has already found.""",
        
        expected_output="""A structured analysis containing:
        - Top 3-5 key insights extracted from the research
        - Identified patterns and trends with explanation
        - Any contradictions or knowledge gaps noted
        - Significance of findings explained clearly
        - Concrete conclusions the Writer can build a report around""",
        
        agent=create_analyst_agent(),
        context_from_async_tasks_if_any=[]
    )