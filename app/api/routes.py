from fastapi import APIRouter
from pydantic import BaseModel

from app.crew.support_crew import run_support_crew

router = APIRouter()


class TicketRequest(BaseModel):
    ticket: str


@router.post("/ticket")
def analyze_ticket(data: TicketRequest):

    result = run_support_crew(data.ticket)

    return result