from crewai import Task

from app.agents.classifier import classifier_agent
from app.agents.priority import priority_agent
from app.agents.resolver import resolver_agent
from app.agents.escalation import escalation_agent

from app.database.retriever import get_solution_by_category


def run_support_crew(ticket: str):

    # Classification

    classify_task = Task(
        description=f"""
        Classify this support ticket:

        {ticket}

        Categories:
        - Authentication
        - Payment
        - Claims
        - Technical
        - Account Management

        Return ONLY the category name.
        """,
        expected_output="Category",
        agent=classifier_agent
    )

    category = str(classify_task.execute_sync()).strip()

    # Priority

    priority_task = Task(
        description=f"""
        Determine priority.

        Ticket:
        {ticket}

        Category:
        {category}

        Return only:
        Low / Medium / High / Critical
        """,
        expected_output="Priority",
        agent=priority_agent
    )

    priority = str(priority_task.execute_sync()).strip()

    # Retrieve from SQLite

    db_result = get_solution_by_category(category)

    if db_result:
        stored_solution = db_result[0]
        team = db_result[1]
    else:
        stored_solution = "No predefined solution found."
        team = "General Support"

    # Resolution

    resolution_task = Task(
        description=f"""
        Ticket:
        {ticket}

        Category:
        {category}

        Priority:
        {priority}

        Internal Solution:
        {stored_solution}

        Generate a customer-friendly solution.

        Rules:
        - Maximum 5 bullet points
        - Short and concise
        """,
        expected_output="Solution",
        agent=resolver_agent
    )

    solution = str(
        resolution_task.execute_sync()
    ).strip()

    # Escalation

    escalation_task = Task(
        description=f"""
        Ticket:
        {ticket}

        Category:
        {category}

        Priority:
        {priority}

        Rules:
        - Critical -> Yes
        - High -> Usually Yes
        - Medium -> Usually No
        - Low -> No

        Return:

        Escalate: Yes/No
        """,
        expected_output="Escalation Decision",
        agent=escalation_agent
    )

    escalation_result = str(
        escalation_task.execute_sync()
    ).strip()

    escalate = "yes" in escalation_result.lower()

    return {
        "category": category,
        "priority": priority,
        "solution": solution,
        "escalate": escalate,
        "assigned_team": team
    }