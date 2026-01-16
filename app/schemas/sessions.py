from pydantic import BaseModel


class SessionOut(BaseModel):
    symbol: str
    ltp: float | None
    best_bid: float | None
    vol_bid: float | None
    best_offer: float | None
    vol_offer: str | None
    opening_price: str | None

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "symbol": "DDL",
                "ltp": 340.0,
                "best_bid": 6.38,
                "vol_bid": 53.3,
                "best_offer": 1.55,
                "vol_offer": "0.5%",
                "opening_price": "1, 2",
            }
        },
    }
