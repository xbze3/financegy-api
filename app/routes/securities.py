from fastapi import APIRouter
import financegy

router = APIRouter(tags=["securities"])


@router.get("/securities")
def get_securities():
    return financegy.get_securities()
