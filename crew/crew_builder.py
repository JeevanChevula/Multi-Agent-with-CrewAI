# crew/crew_builder.py

from crewai import Crew, Process
from tasks.research_task import create_research_task
from tasks.analysis_task import create_analysis_task
from tasks.writing_task import create_writing_task
from agents.research_agent import create_research_agent
from agents.analyst_agent import create_analyst_agent
from agents.writer_agent import create_writer_agent

def build_crew(topic: str):
    """Assembles and returns the research crew for a given topic."""
    
    # Create agents
    researcher = create_research_agent()
    analyst = create_analyst_agent()
    writer = create_writer_agent()
    
    # Create tasks — passing the same agent instances
    research_task = create_research_task(topic)
    analysis_task = create_analysis_task(topic)
    writing_task = create_writing_task(topic)
    
    # Assemble the crew
    return Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, writing_task],
        process=Process.sequential,
        verbose=True
    )