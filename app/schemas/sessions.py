from pydantic import BaseModel


class SessionsOut(BaseModel):
    symbol: str
    ltp: str
    best_bid: str
    vol_bid: str
    best_offer: str
    vol_offer: str
    opening_price: str

    model_config = {"from_attributes": True}
