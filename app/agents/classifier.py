from crewai import Agent

classifier_agent = Agent(
    role="Support Ticket Classifier",
    goal="Classify support tickets into the correct category",
    backstory="You are an expert support analyst.",
    verbose=False
)