import uuid
import logging

from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.extension import _rate_limit_exceeded_handler

from app.infra.limiter import limiter
from .v1.routes import v1_securities, v1_sessions, v1_trades
from .v2.routes import v2_securities, v2_sessions, v2_trades, v2_analytics, v2_portfolio
from .errors import DomainError, error_payload

app = FastAPI(
    title="FinanceGY Market Data API",
    description="Unofficial API for accessing financial data from the Guyana Stock Exchange (GSE).",
    version="2.0",
)

logger = logging.getLogger("financegy")

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return _rate_limit_exceeded_handler(request, exc)


@app.middleware("http")
async def request_id_middleware(request: Request, call_next):
    request.state.request_id = request.headers.get("X-Request-Id", str(uuid.uuid4()))
    response = await call_next(request)
    response.headers["X-Request-Id"] = request.state.request_id
    return response


@app.exception_handler(DomainError)
async def domain_error_handler(request: Request, exc: DomainError):
    rid = getattr(request.state, "request_id", "unknown")
    return JSONResponse(
        status_code=exc.status,
        content=error_payload(
            code=exc.code,
            message=exc.message,
            request_id=rid,
            details=exc.details,
        ),
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    rid = getattr(request.state, "request_id", "unknown")
    return JSONResponse(
        status_code=422,
        content=error_payload(
            code="VALIDATION_ERROR",
            message="Input validation failed",
            request_id=rid,
            details={"errors": exc.errors()},
        ),
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    rid = getattr(request.state, "request_id", "unknown")
    logger.exception("Unhandled error request_id=%s", rid)
    return JSONResponse(
        status_code=500,
        content=error_payload(
            code="INTERNAL_ERROR",
            message="An unexpected error occurred",
            request_id=rid,
        ),
    )


@app.get("/", tags=["default"])
def root_index():
    return {
        "name": "FinanceGY Market Data API",
        "status": "ok",
        "docs": "/docs",
        "redoc": "/redoc",
        "versions": {
            "v1": {"status": "deprecated", "base": "/v1"},
            "v2": {"status": "current", "base": "/v2"},
        },
    }


@app.get("/health", include_in_schema=False)
def health():
    return {"status": "ok"}


# /v1 routes

v1 = APIRouter(prefix="/v1")


@v1.get("/", include_in_schema=False)
def v1_root():
    return {"status": "ok", "message": "Welcome to FinanceGY-API", "version": "v1"}


v1.include_router(v1_securities.router)
v1.include_router(v1_sessions.router)
v1.include_router(v1_trades.router)

app.include_router(v1)

# /v2 routes

v2 = APIRouter(prefix="/v2")


@v2.get("/", include_in_schema=False)
def v2_root():
    return {"status": "ok", "message": "Welcome to FinanceGY-API", "version": "v2"}


v2.include_router(v2_securities.router)
v2.include_router(v2_sessions.router)
v2.include_router(v2_trades.router)
v2.include_router(v2_analytics.router)
v2.include_router(v2_portfolio.router)

app.include_router(v2)
