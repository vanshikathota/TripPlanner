import os
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Clude AI LLM
try:
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

    if not ANTHROPIC_API_KEY:
        print("❌ Error: ANTHROPIC_API_KEY not found in environment!")
        exit(1)
    
    print("🔄 Testing Clude AI API connection...")

    Claude = LLM(
        api_key=os.getenv("ANTHROPIC_API_KEY"),
        model="anthropic/claude-3-7-sonnet-20250219",
        max_tokens=5000,
        temperature=0
    )

    print("✅ Clude AI LLM initialized successfully.")

except Exception as e:
    print(f"❌ Error initializing Clude AI: {e}")
    exit(1)

# Initialize Claude LLM (for Global Route Strategist only)
try:
    claude_llm = LLM(
        provider="anthropic",
        model="claude-3-7-sonnet-20250219",
        config={
            "api_key": os.getenv("ANTHROPIC_API_KEY"),
            "max_tokens": 5000,
            "temperature": 0
        }
    )
    print("✅ Claude LLM initialized successfully.")
except Exception as e:
    print(f"❌ Error initializing Claude LLM: {e}")
    exit(1)

# Agents
global_route_strategist = Agent(
    role="Global Route Strategist",
    goal="Plan optimal international travel routes",
    backstory="An experienced strategist specializing in global travel logistics and route optimization.",
    llm=Claude,
    verbose=True,
)

travel_logistics_coordinator = Agent(
    role="Travel Logistics Coordinator",
    goal="Provide detailed travel logistics including transport options and connections",
    backstory="A professional in managing complex travel itineraries and transport schedules.",
    llm=Claude,
    verbose=True,
)

destination_intelligence_specialist = Agent(
    role="Destination Intelligence Specialist",
    goal="Provide insights about destinations such as culture, history, and activities",
    backstory="A cultural expert with deep knowledge of global destinations and local customs.",
    llm=Claude,
    verbose=True,
)

strategic_itinerary_architect = Agent(
    role="Strategic Itinerary Architect",
    goal="Create a personalized and feasible day-by-day itinerary",
    backstory="A travel consultant known for crafting detailed travel itineraries.",
    llm=Claude,
    verbose=True,
)

experience_personalization_maestro = Agent(
    role="Experience Personalization Maestro",
    goal="Customize travel recommendations based on user preferences and style",
    backstory="A creative expert skilled in personalizing travel experiences.",
    llm=Claude,
    verbose=True,
)

# User Input
print("🌟 Welcome to AI Travel Planner!")
print("-" * 40)

starting_location = input("📍 Enter your starting location: ")
destination = input("🎯 Enter your destination: ")
start_date = input("📅 Enter your trip start date (YYYY-MM-DD): ")
end_date = input("📅 Enter your trip end date (YYYY-MM-DD): ")
budget_inr = input("💰 Enter your budget (in INR): ")
interests = input("🎨 Enter your travel interests (e.g., history, adventure, relaxation): ")
style = input("✈️ Enter your travel style (e.g., luxury, budget, backpacking): ")

print("\n🚀 Starting trip planning process...")
print("-" * 50)

# Tasks
task1 = Task(
    description=f"""
    As a Global Route Strategist, analyze and provide the best travel routes from {starting_location} to {destination}.
    Provide at least 3 different route options.
    Output in JSON: {{'routes': ['route 1 details', 'route 2 details', 'route 3 details']}}
    """,
    expected_output="{'routes': ['route 1', 'route 2', 'route 3']}",
    agent=global_route_strategist
)

task2 = Task(
    description=f"""
    As a Travel Logistics Coordinator, provide comprehensive transport logistics between {starting_location} and {destination}.
    Include flights, ground transport, transfers, and booking tips.
    Output in JSON: {{'logistics': ['option 1', 'option 2', 'option 3']}}
    """,
    expected_output="{'logistics': ['option 1', 'option 2', 'option 3']}",
    agent=travel_logistics_coordinator
)

task3 = Task(
    description=f"""
    As a Destination Intelligence Specialist, provide rich insights about {destination} including culture, cuisine, weather, and safety.
    Output in JSON: {{'insights': ['detail 1', 'detail 2', 'detail 3']}}
    """,
    expected_output="{'insights': ['detail 1', 'detail 2', 'detail 3']}",
    agent=destination_intelligence_specialist
)

task4 = Task(
    description=f"""
    As a Strategic Itinerary Architect, design a detailed itinerary for a trip from {start_date} to {end_date} in {destination} considering:
    Budget: ₹{budget_inr}, Interests: {interests}, Style: {style}.
    Output in JSON: {{'itinerary': ['Day 1: plan', 'Day 2: plan', '...']}}
    """,
    expected_output="{'itinerary': ['day 1 plan', 'day 2 plan', 'day 3 plan']}",
    agent=strategic_itinerary_architect
)

task5 = Task(
    description=f"""
    As an Experience Personalization Maestro, give tailored tips for {destination} matching {style} style and {interests}.
    Output in JSON: {{'personalized_tips': ['tip 1', 'tip 2', 'tip 3']}}
    """,
    expected_output="{'personalized_tips': ['tip 1', 'tip 2', 'tip 3']}",
    agent=experience_personalization_maestro
)

# Crew
crew = Crew(
    agents=[
        global_route_strategist,
        travel_logistics_coordinator,
        destination_intelligence_specialist,
        strategic_itinerary_architect,
        experience_personalization_maestro
    ],
    tasks=[task1, task2, task3, task4, task5],
    verbose=True
)

# Execute
try:
    print("🔄 Processing your travel plan...")
    final_output = crew.kickoff()

    # Save to text file
    with open("trip_plan.txt", "w", encoding="utf-8") as f:
        f.write("🌟 AI Travel Planner - Final Trip Plan 🌟\n")
        f.write("="*60 + "\n")
        f.write(f"Start Location: {starting_location}\n")
        f.write(f"Destination: {destination}\n")
        f.write(f"Start Date: {start_date}\n")
        f.write(f"End Date: {end_date}\n")
        f.write(f"Budget (INR): ₹{budget_inr}\n")
        f.write(f"Interests: {interests}\n")
        f.write(f"Style: {style}\n")
        f.write("="*60 + "\n\n")
        f.write(str(final_output))

    print("\n🎉 FINAL TRIP PLAN OUTPUT saved to 'trip_plan.txt'.")

except Exception as e:
    print(f"❌ Error during execution: {e}")
