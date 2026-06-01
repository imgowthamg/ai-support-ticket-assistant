from crewai import Agent

priority_agent = Agent(
    role="Priority Assessment Specialist",
    goal="Determine the priority level of support tickets",
    backstory="You are an experienced support manager.",
    verbose=False
)