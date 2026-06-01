from crewai import Agent

resolver_agent = Agent(
    role="Support Resolution Specialist",
    goal="Provide troubleshooting solutions",
    backstory="You are a senior support engineer.",
    verbose=False
)