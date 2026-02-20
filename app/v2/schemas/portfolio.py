from pydantic import BaseModel, Field


class PortfolioPosition(BaseModel):
    symbol: str = Field(..., description="Security ticker symbol", example="DTC")
    shares: float = Field(..., gt=0, description="Number of shares held", example=100)
    purchase_price: float = Field(
        ..., gt=0, description="Purchase price per share", example=300
    )
