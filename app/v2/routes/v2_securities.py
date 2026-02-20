from fastapi import APIRouter, Depends, Request

from app.infra.limiter import limiter
from app.v2.services import financegy_service
from app.v2.schemas.securities import SecurityOut
from app.dependencies.search import get_search_query
from app.dependencies.symbol import get_symbol

router = APIRouter(
    tags=["Securities V2"],
)


@router.get(
    "/securities",
    summary="List all securities",
    description="Returns all currently traded securities listed on the Guyana Stock Exchange, including their ticker symbols and company names.",
    response_model=list[SecurityOut],
)
@limiter.limit("30/minute")
def get_securities(request: Request):
    securities = financegy_service.get_securities()
    return securities


@router.get(
    "/securities/active",
    summary="List active securities",
    description="Returns securities that were active in the most recent trading session on the Guyana Stock Exchange.",
    response_model=list[SecurityOut],
)
@limiter.limit("60/minute")
def get_active_securities(request: Request):
    active_securities = financegy_service.get_active_securities()
    return active_securities


@router.get(
    "/securities/search",
    summary="Search securities",
    description="Searches for securities whose symbol or company name matches the provided query.",
    response_model=list[SecurityOut],
)
@limiter.limit("60/minute")
def search_securities(request: Request, q: str = Depends(get_search_query)):
    search_results = financegy_service.search_securities(q)
    return search_results


@router.get(
    "/securities/{symbol}",
    summary="Get security by symbol",
    description="Returns the company name and details for the specified ticker symbol.",
    response_model=SecurityOut,
)
@limiter.limit("30/minute")
def get_security_by_symbol(request: Request, symbol: str = Depends(get_symbol)):
    security_name = financegy_service.get_security_by_symbol(symbol)
    return SecurityOut(symbol=symbol, name=security_name)
