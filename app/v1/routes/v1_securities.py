from fastapi import APIRouter, Depends, Request

from app.infra.limiter import limiter
from app.v1.services import financegy_service
from app.v1.schemas.securities import SecurityOut
from app.dependencies.search import get_search_query
from app.dependencies.symbol import get_symbol

router = APIRouter(
    tags=["Securities V1"],
)


@router.get(
    "/securities",
    summary="List all securities",
    description=(
        "Returns a list of all available securities."
        "Use this endpoint to populate dropdowns, autocomplete lists, or cached reference data."
    ),
    response_model=list[SecurityOut],
)
@limiter.limit("30/minute")
def get_securities(request: Request):
    return financegy_service.get_securities()


@router.get(
    "/securities/search",
    summary="Search securities by keyword",
    description=(
        "Search for securities using a free-text keyword."
        "Typical use-cases: autocomplete, symbol/name search, filtering lists."
    ),
    response_model=list[SecurityOut],
)
@limiter.limit("60/minute")
def search_securities(request: Request, q: str = Depends(get_search_query)):
    return financegy_service.search_securities(q)


@router.get(
    "/securities/{symbol}",
    summary="Get security details by symbol",
    description="Returns security metadata/details for the provided symbol (ticker).",
    response_model=SecurityOut,
)
@limiter.limit("30/minute")
def get_security_by_symbol(request: Request, symbol: str = Depends(get_symbol)):
    name = financegy_service.get_security_by_symbol(symbol)
    return SecurityOut(symbol=symbol, name=name)
