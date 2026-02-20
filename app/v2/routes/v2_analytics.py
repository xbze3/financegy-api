from fastapi import APIRouter, Depends, Request

from app.infra.limiter import limiter
from app.v2.services import financegy_service
from app.dependencies.symbol import get_symbol

router = APIRouter(
    tags=["Analytics V2"],
)


@router.get(
    "/securities/{symbol}/price-change",
    response_model=dict,
    summary="Get absolute price change",
    description="Returns the absolute difference between the most recent trade price and the previous session close for the specified security.",
)
@limiter.limit("60/minute")
def get_price_change(request: Request, symbol: str = Depends(get_symbol)):
    return financegy_service.get_price_change(symbol)


@router.get(
    "/securities/{symbol}/price-change/percent",
    response_model=dict,
    summary="Get percentage price change",
    description="Returns the percentage change between the most recent trade price and the previous session close.",
)
@limiter.limit("60/minute")
def get_price_change_percent(request: Request, symbol: str = Depends(get_symbol)):
    return financegy_service.get_price_change_percent(symbol)


@router.get(
    "/securities/{symbol}/analytics/average-price",
    response_model=dict,
    summary="Get average price over recent sessions",
    description="Returns the average last traded price over the most recent N trading sessions (default: 30).",
)
@limiter.limit("30/minute")
def get_average_price(
    request: Request,
    symbol: str = Depends(get_symbol),
    n: int = 30,
):
    return financegy_service.get_average_price(symbol, n)


@router.get(
    "/securities/{symbol}/analytics/volatility",
    response_model=dict,
    summary="Get price volatility",
    description="Returns the annualized volatility based on price changes over the most recent N trading sessions.",
)
@limiter.limit("30/minute")
def get_sessions_volatility(
    request: Request,
    symbol: str = Depends(get_symbol),
    n: int = 30,
):
    return financegy_service.get_sessions_volatility(symbol, n)


@router.get(
    "/securities/{symbol}/analytics/ytd-high-low",
    response_model=dict,
    summary="Get year-to-date high and low",
    description="Returns the highest and lowest traded prices for the security during the current calendar year.",
)
@limiter.limit("60/minute")
def get_ytd_high_low(request: Request, symbol: str = Depends(get_symbol)):
    return financegy_service.get_ytd_high_low(symbol)
