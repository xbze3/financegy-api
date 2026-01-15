from fastapi import APIRouter, Path
from app.services import financegy_service

router = APIRouter(
    tags=["sessions"],
)


@router.get(
    "/sessions/{session}/trades",
    summary="Get all trades for a trading session",
    description=(
        "Returns all trades associated with a specific trading session.\n\n"
        "This endpoint is useful for session-level analysis, reconciliation, or reporting."
    ),
)
def get_session_trades(
    session: str = Path(
        ...,
        description="Trading session ID.",
        examples=["1140", "1150", "1155"],
    )
):
    return financegy_service.get_session_trades(session)
