from pydantic import BaseModel


class TradeOut(BaseModel):
    session: int
    session_date: str
    last_trade_price: str | None
    eps: str | None
    pe_ratio: str | None
    dividends_paid_last_12_months: str | None
    dividend_yield: str | None
    notes: str | None

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "session": "1004",
                "session_date": "30/01/2023",
                "last_trade_price": "340.0",
                "eps": "6.38",
                "pe_ratio": "53.3",
                "dividends_paid_last_12_months": "1.55",
                "dividend_yield": "0.5%",
                "notes": "1, 2",
            }
        },
    }
