from fastapi import APIRouter, Depends, Request

from app.infra.limiter import limiter
from app.v2.services import financegy_service
from app.dependencies.symbol import get_symbol

router = APIRouter(
    tags=["Market V2"],
)


@router.get(
    "/market/snapshot",
    response_model=list,
    summary="Get a market snapshot",
    description="Get overall market snapshot (Symbol | Name | LTP | Prev Close | Price Change | PC% | YTD High | YTD Low)",
)
@limiter.limit("15/minute")
def get_market_snapshot(request: Request):
    return financegy_service.get_market_snapshot()


@router.get(
    "/market/movers",
    response_model=dict,
    summary="Get top market gainers and losers (based on % price change)",
    description="Returns top market gainers, losers, and unchanged securities (%change).",
)
@limiter.limit("15/minute")
def get_movers(request: Request):
    return financegy_service.get_movers()
