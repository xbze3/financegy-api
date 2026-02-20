from fastapi import APIRouter, Depends, Request

from app.infra.limiter import limiter
from app.v2.services import financegy_service
from app.v2.schemas.trades import TradeOut
from app.dependencies.symbol import get_symbol
from app.dependencies.year import get_year
from app.dependencies.date_range_flexible import get_date_range, DateRange

router = APIRouter(
    tags=["Trades V2"],
)


@router.get(
    "/securities/{symbol}/trades/latest",
    summary="Get recent trade",
    description="Returns the most recent trade record available for the specified security.",
    response_model=TradeOut,
)
@limiter.limit("60/minute")
def get_recent_trade(request: Request, symbol: str = Depends(get_symbol)):
    recent_trade = financegy_service.get_recent_trade(symbol)
    return recent_trade


@router.get(
    "/securities/{symbol}/trades",
    summary="Get trades for year",
    description="Returns all trade records for the specified security during the given year.",
    response_model=list[TradeOut],
)
@limiter.limit("30/minute")
def get_trades_for_year(
    request: Request,
    symbol: str = Depends(get_symbol),
    y: str = Depends(get_year),
):
    year_trades = financegy_service.get_trades_for_year(symbol, y)
    return year_trades


@router.get(
    "/securities/{symbol}/trades/recent-year",
    summary="Get recent year trades",
    description="Returns all trade records for the most recent year available for the specified security.",
    response_model=list[TradeOut],
)
@limiter.limit("30/minute")
def get_security_recent_year(request: Request, symbol: str = Depends(get_symbol)):
    recent_year_trades = financegy_service.get_security_recent_year(symbol)
    return recent_year_trades


@router.get(
    "/securities/{symbol}/trades/history",
    summary="Get historical trades",
    description="Returns trade records for the specified security within the provided date range.",
    response_model=list[TradeOut],
)
@limiter.limit("10/minute")
def get_historical_trades(
    request: Request,
    symbol: str = Depends(get_symbol),
    dr: DateRange = Depends(get_date_range),
):
    historical_trades = financegy_service.get_historical_trades(
        symbol, dr.start, dr.end
    )
    return historical_trades


@router.get(
    "/securities/{symbol}/trades/full-history",
    summary="Get full history",
    description="Returns the complete trade history across all available years for the specified security.",
    response_model=list[TradeOut],
)
@limiter.limit("10/minute")
def get_security_full_history(request: Request, symbol: str = Depends(get_symbol)):
    full_history = financegy_service.get_security_full_history(symbol)
    return full_history
