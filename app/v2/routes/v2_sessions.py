from fastapi import APIRouter, Depends, Request

from app.infra.limiter import limiter
from app.v2.services import financegy_service
from app.v2.schemas.sessions import SessionOut
from app.v2.schemas.trades import TradeOut
from app.dependencies.symbol import get_symbol
from app.dependencies.session import get_session_id
from app.dependencies.year import get_year_path

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


@router.get(
    "/session/{session}/date",
    response_model=str,
    summary="Get specified session date.",
    description="Returns the date for a specified trading session.",
)
@limiter.limit("60/minute")
def get_session_date(request: Request, session: str = Depends(get_session_id)):
    return financegy_service.get_session_date(session)


@router.get(
    "/sessions/year/{year}",
    summary="Get trading sessions for a specific year",
    description="Returns all trading sessions that occurred within the specified year along with their session dates.",
    response_model=dict,
)
@limiter.limit("20/minute")
def get_year_sessions(request: Request, year: int = Depends(get_year_path)):
    return financegy_service.get_year_sessions(year)


@router.get(
    "/sessions/year/{year}/snapshot",
    summary="Get yearly trading sessions snapshot",
    description=(
        "Returns an aggregated snapshot of all trading sessions for a given year. "
        "This includes consolidated market data such as session summaries, price movements, "
        "and activity across all listed securities for each session in the selected year."
    ),
    response_model=dict,
)
@limiter.limit("15/minute")
def get_year_sessions_snapshot(request: Request, year: int = Depends(get_year_path)):
    return financegy_service.get_year_sessions_snapshot(year)
