from fastapi import Depends
from fastapi import APIRouter, Query, Path
from app.services import financegy_service
from app.schemas.securities import SecurityOut
from app.schemas.trades import TradeOut
from app.schemas.sessions import SessionOut
from app.dependencies.search import get_search_query
from app.dependencies.symbol import get_symbol
from app.dependencies.year import get_year
from app.dependencies.session import get_session_id
from app.dependencies.date_range_flexible import get_date_range
from app.dependencies.date_range_flexible import DateRange


router = APIRouter(
    tags=["securities"],
)


@router.get(
    "/securities",
    summary="List all securities",
    description=(
        "Returns a list of all available securities.\n\n"
        "Use this endpoint to populate dropdowns, autocomplete lists, or cached reference data."
    ),
    response_model=list[SecurityOut],
)
def get_securities():
    return financegy_service.get_securities()


@router.get(
    "/securities/search",
    summary="Search securities by keyword",
    description=(
        "Search for securities using a free-text keyword.\n\n"
        "Typical use-cases: autocomplete, symbol/name search, filtering lists."
    ),
    response_model=list[SecurityOut],
)
def search_securities(q: str = Depends(get_search_query)):
    return financegy_service.search_securities(q)


@router.get(
    "/securities/{symbol}/trades/latest",
    summary="Get the latest trade for a security",
    description="Returns the most recent trade record available for the provided security symbol.",
    response_model=TradeOut,
)
def get_recent_trade(symbol: str = Depends(get_symbol)):
    return financegy_service.get_recent_trade(symbol)


@router.get(
    "/securities/{symbol}/trades",
    summary="Get trades for a security in a specific year",
    description=(
        "Returns all trades for the provided security symbol for a given year.\n\n"
        "Use this endpoint to build yearly trade tables or compute yearly summaries."
    ),
    response_model=list[TradeOut],
)
def get_trades_for_year(
    symbol: str = Depends(get_symbol),
    y: str = Depends(get_year),
):
    return financegy_service.get_trades_for_year(symbol, y)


@router.get(
    "/securities/{symbol}/trades/recent-year",
    summary="Get trades for the most recent available year",
    description=(
        "Returns trades for the latest year available for the provided security symbol.\n\n"
        "Useful when the client does not know which year is the most recent in the dataset."
    ),
    response_model=list[TradeOut],
)
def get_security_recent_year(symbol: str = Depends(get_symbol)):
    return financegy_service.get_security_recent_year(symbol)


@router.get(
    "/securities/{symbol}/sessions/{session}/trades",
    summary="Get trades for a security in a given trading session",
    description=("Returns trades for a security filtered by a session ID."),
    response_model=SessionOut,
)
def get_security_session_trade(
    symbol: str = Depends(get_symbol),
    session: str = Depends(get_session_id),
):
    return financegy_service.get_security_session_trade(symbol, session)


@router.get(
    "/securities/{symbol}/trades/history",
    summary="Get historical trades within a date range",
    description=(
        "Returns historical trades for a security between a start and end date.\n\n"
        "Accepted date formats:\n"
        "- `yyyy` (e.g., `2022`)\n"
        "- `mm/yyyy` (e.g., `01/2022`)\n"
        "- `dd/mm/yyyy` (e.g., `01/06/2020`)\n\n"
        "Tip: Use query parameters so slashes in dates are handled safely."
    ),
    response_model=list[TradeOut],
)
def get_historical_trades(
    symbol: str = Depends(get_symbol),
    dr: DateRange = Depends(get_date_range),
):
    return financegy_service.get_historical_trades(symbol, dr.start, dr.end)


@router.get(
    "/securities/{symbol}",
    summary="Get security details by symbol",
    description="Returns security metadata/details for the provided symbol (ticker).",
    response_model=SecurityOut,
)
def get_security_by_symbol(symbol: str = Depends(get_symbol)):
    name = financegy_service.get_security_by_symbol(symbol)
    return SecurityOut(symbol=symbol, name=name)
