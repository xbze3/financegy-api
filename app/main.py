from fastapi import FastAPI
from .routes import securities
from .routes import sessions

app = FastAPI(
    title="FinanceGY Market Data API",
    description="Unofficial API for accessing financial data from the Guyana Stock Exchange (GSE).",
    version="1.0.0",
    root_path="/v1",
)


@app.get("/")
def root():
    return {"status": "ok", "message": "Welcome to FinanceGY-API", "version": "v1"}


app.include_router(securities.router)
app.include_router(sessions.router)
