from fastapi import APIRouter, Depends, Request

from app.infra.limiter import limiter
from app.v1.services import financegy_service
from app.v1.schemas.sessions import SessionOut
from app.v1.utils.adapters import adapt_session_v1
from app.dependencies.symbol import get_symbol
from app.dependencies.session import get_session_id

router = APIRouter(
    tags=["Sessions V1"],
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
@limiter.limit("30/minute")
def get_session_trades(request: Request, session: str = Depends(get_session_id)):
    return financegy_service.get_session_trades(session)


@router.get(
    "/securities/{symbol}/sessions/{session}/trades",
    summary="Get trades for a security in a given trading session",
    description="Returns trades for a security filtered by a session ID.",
    response_model=SessionOut,
)
@limiter.limit("60/minute")
def get_security_session_trade(
    request: Request,
    symbol: str = Depends(get_symbol),
    session: str = Depends(get_session_id),
):
    payload = adapt_session_v1(
        financegy_service.get_security_session_trade(symbol, session)
    )
    return payload
