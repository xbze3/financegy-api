from fastapi import APIRouter
from app.services import financegy_service

router = APIRouter(tags=["securities"])


@router.get("/securities")
def get_securities():
    return financegy_service.get_securities()


@router.get("/securities/{symbol}")
def get_security_by_symbol(symbol: str):
    return financegy_service.get_security_by_symbol(symbol)
