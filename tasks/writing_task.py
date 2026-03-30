# tasks/writing_task.py

from crewai import Task
from agents.writer_agent import create_writer_agent

def create_writing_task(topic: str):
    """Creates and returns the writing task for a given topic."""
    return Task(
        description=f"""Write a comprehensive, professional research report on: {topic}
        
        Using the research findings and analysis provided to you, create a report that includes:
        - An executive summary (2-3 sentences capturing the essence)
        - Key findings section with clear headings
        - Analysis and insights section
        - Trends and patterns observed
        - Conclusions and implications
        
        Writing guidelines:
        - Use clear, professional language
        - Structure the report with proper headings and sections
        - Make complex information accessible without oversimplifying
        - Ensure logical flow from findings to conclusions
        - The report should stand alone — a reader with no prior context should understand it""",
        
        expected_output="""A polished, professional research report containing:
        - Executive summary at the top
        - Well-structured sections with clear headings
        - All key findings and insights incorporated
        - Proper conclusions that follow logically from the findings
        - Minimum 400 words, written in clear professional English""",
        
        agent=create_writer_agent()
    )