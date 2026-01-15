from fastapi import APIRouter
import financegy

router = APIRouter(tags=["securities"])


@router.get("/securities")
def get_securities():
    return financegy.get_securities()


@router.get("/securities/{symbol}")
def get_security_by_symbol(symbol: str):
    return financegy.get_security_by_symbol(symbol)
