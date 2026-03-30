# main.py

from dotenv import load_dotenv
load_dotenv()

from crew.crew_builder import build_crew

def main():
    print("\n=== AI Research Assistant - Layer 3 ===\n")
    
    topic = input("Enter a research topic: ").strip()
    
    if not topic:
        print("No topic entered. Exiting.")
        return
    
    print(f"\nStarting research on: {topic}")
    print("This may take a few minutes...\n")
    
    crew = build_crew(topic)
    result = crew.kickoff()
    
    print("\n=== FINAL RESEARCH REPORT ===\n")
    print(result)

if __name__ == "__main__":
    main()