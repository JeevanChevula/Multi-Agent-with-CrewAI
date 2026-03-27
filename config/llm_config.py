# config/llm_config.py

from crewai import LLM

def get_llm():
    """Returns Gemini 2.5 Flash-Lite — fast, cheap, good for worker agents."""
    return LLM(
        model="gemini/gemini-2.5-flash-lite",
        temperature=0.7
    )