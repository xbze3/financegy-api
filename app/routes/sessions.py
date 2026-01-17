from fastapi import Depends
from fastapi import APIRouter, Path
from app.services import financegy_service
from app.schemas.sessions import SessionOut
from app.dependencies.session import get_session_id

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
    response_model=list[SessionOut],
)
def get_session_trades(session: str = Depends(get_session_id)):
    return financegy_service.get_session_trades(session)
