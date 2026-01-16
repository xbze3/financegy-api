from pydantic import BaseModel


class SecurityOut(BaseModel):
    symbol: str
    name: str

    model_config = {"from_attributes": True}
