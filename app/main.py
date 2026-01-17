import uuid
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from .routes import securities
from .routes import sessions
from .errors import DomainError, error_payload

app = FastAPI(
    title="FinanceGY Market Data API",
    description="Unofficial API for accessing financial data from the Guyana Stock Exchange (GSE).",
    version="1.0.0",
    root_path="/v1",
)


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


@app.get("/")
def root():
    return {"status": "ok", "message": "Welcome to FinanceGY-API", "version": "v1"}


app.include_router(securities.router)
app.include_router(sessions.router)
