from fastapi import APIRouter, Depends, Request

from app.infra.limiter import limiter
from app.v2.services import financegy_service
from app.v2.schemas.sessions import SessionOut
from app.v2.schemas.trades import TradeOut
from app.dependencies.symbol import get_symbol
from app.dependencies.session import get_session_id

router = APIRouter(
    tags=["Sessions V2"],
)


@router.get(
    "/sessions/recent",
    summary="Get most recent session",
    description="Returns the most recent trading session number available on the Guyana Stock Exchange.",
    response_model=str,
)
@limiter.limit("60/minute")
def get_recent_session(request: Request):
    recent_session = financegy_service.get_recent_session()
    return recent_session


@router.get(
    "/sessions/{session}/trades",
    summary="Get session trades",
    description="Returns all trade records for all securities during the specified trading session.",
    response_model=list[SessionOut],
)
@limiter.limit("60/minute")
def get_session_trades(request: Request, session: str = Depends(get_session_id)):
    session_trades = financegy_service.get_session_trades(session)
    return session_trades


@router.get(
    "/securities/{symbol}/sessions/{session}/trades",
    summary="Get security session trade",
    description="Returns the trade record for a specific security during the specified trading session.",
    response_model=SessionOut,
)
@limiter.limit("60/minute")
def get_security_session_trade(
    request: Request,
    symbol: str = Depends(get_symbol),
    session: str = Depends(get_session_id),
):
    security_session_trade = financegy_service.get_security_session_trade(
        symbol, session
    )
    return security_session_trade


@router.get(
    "/securities/{symbol}/sessions/latest",
    summary="Get latest session for symbol",
    description="Returns the most recent trade record available for the specified security.",
    response_model=TradeOut,
)
@limiter.limit("60/minute")
def get_latest_session_for_symbol(request: Request, symbol: str = Depends(get_symbol)):
    latest_session = financegy_service.get_latest_session_for_symbol(symbol)
    return latest_session
