from fastapi import APIRouter, Depends, Request

from app.dependencies.portfolio import get_portfolio
from app.infra.limiter import limiter
from app.v2.schemas.portfolio import PortfolioPosition
from app.v2.services import financegy_service
from app.dependencies.symbol import get_symbol

router = APIRouter(
    tags=["Portfolio V2"],
)


@router.get(
    "/securities/{symbol}/position/value",
    response_model=dict,
    summary="Calculate position market value",
    description="Returns the current market value of a position based on the latest trade price and the number of shares held.",
)
@limiter.limit("30/minute")
def calculate_position_value(
    request: Request,
    symbol: str = Depends(get_symbol),
    shares: float = 0,
):
    position_value = financegy_service.calculate_position_value(symbol, shares)
    return position_value


@router.get(
    "/securities/{symbol}/position/return",
    response_model=dict,
    summary="Calculate unrealized gain or loss",
    description="Returns the unrealized profit or loss for a position based on the latest trade price, shares held, and purchase price.",
)
@limiter.limit("30/minute")
def calculate_position_return(
    request: Request,
    symbol: str = Depends(get_symbol),
    shares: float = 0,
    purchase_price: float = 0,
):
    position_return = financegy_service.calculate_position_return(
        symbol, shares, purchase_price
    )
    return position_return


@router.get(
    "/securities/{symbol}/position/return/percent",
    response_model=dict,
    summary="Calculate percentage return",
    description="Returns the percentage unrealized gain or loss for a position based on the latest trade price and purchase price.",
)
@limiter.limit("30/minute")
def calculate_position_return_percent(
    request: Request,
    symbol: str = Depends(get_symbol),
    shares: float = 0,
    purchase_price: float = 0,
):
    position_return_percent = financegy_service.calculate_position_return_percent(
        symbol, shares, purchase_price
    )
    return position_return_percent


@router.post(
    "/portfolio/summary",
    response_model=dict,
    summary="Calculate portfolio summary",
    description="Returns a full portfolio summary including total value, total return, and per-position breakdown using latest trade prices.",
)
@limiter.limit("10/minute")
def calculate_portfolio_summary(
    request: Request, portfolio: list[PortfolioPosition] = Depends(get_portfolio)
):
    positions = [p.model_dump() for p in portfolio]
    portfolio_summary = financegy_service.calculate_portfolio_summary(positions)
    return portfolio_summary
