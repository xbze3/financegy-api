from fastapi import FastAPI
from .routes import securities

app = FastAPI(title="FinanceGY-API", root_path="/v1")


@app.get("/")
def root():
    return {"status": "ok", "message": "Welcome to FinanceGY-API", "version": "v1"}


app.include_router(securities.router)
