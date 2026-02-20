from typing import List
from fastapi import Body, HTTPException

from app.v2.schemas.portfolio import PortfolioPosition


def get_portfolio(
    portfolio: List[PortfolioPosition] = Body(
        ...,
        description="List of portfolio positions",
        example=[
            {"symbol": "DTC", "shares": 100, "purchase_price": 300},
            {"symbol": "DDL", "shares": 50, "purchase_price": 250},
        ],
    )
) -> List[PortfolioPosition]:
    if not portfolio:
        raise HTTPException(status_code=400, detail="Portfolio cannot be empty")

    return portfolio
