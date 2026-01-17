from pydantic import BaseModel


class SecurityOut(BaseModel):
    symbol: str
    name: str | None

    model_config = {
        "from_attributes": True,
        "json_schema_extra": {
            "example": {
                "symbol": "BDH",
                "name": "Banks DIH Holdings Inc.",
            }
        },
    }
