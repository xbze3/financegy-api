from pydantic import BaseModel, Field


class PortfolioPosition(BaseModel):
    symbol: str = Field(
        ...,
        description="Security ticker symbol",
        json_schema_extra={"example": "DTC"},
    )

    shares: float = Field(
        ...,
        gt=0,
        description="Number of shares held",
        json_schema_extra={"example": 100},
    )

    purchase_price: float = Field(
        ...,
        gt=0,
        description="Purchase price per share",
        json_schema_extra={"example": 300},
    )
