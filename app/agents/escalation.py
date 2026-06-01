from crewai import Agent

escalation_agent = Agent(
    role="Escalation Specialist",
    goal="Determine whether a support ticket should be escalated",
    backstory="""
    You are a support operations lead responsible
    for routing tickets to the correct teams.
    """,
    verbose=False
)