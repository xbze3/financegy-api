from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_securities():
    response = client.get("/v1/securities")
    assert response.status_code == 200


def test_search_securities():
    response = client.get("/v1/securities/search?q=ddl")
    assert response.status_code == 200


def test_get_security_by_symbol():
    response = client.get("/v1/securities/DDL")
    assert response.status_code == 200


def test_get_session_trades():
    response = client.get("/v1/sessions/1056/trades")
    assert response.status_code == 200


def test_get_security_session_trade():
    response = client.get("/v1/securities/DDL/sessions/1056/trades")
    assert response.status_code == 200


def test_get_recent_trade():
    response = client.get("/v1/securities/DDL/trades/latest")
    assert response.status_code == 200


def test_get_trades_for_year():
    response = client.get("/v1/securities/DDL/trades?y=2024")
    assert response.status_code == 200


def test_get_recent_year_trades():
    response = client.get("/v1/securities/DDL/trades/recent-year")
    assert response.status_code == 200


def test_get_historical_trades():
    response = client.get("/v1/securities/DDL/trades/history?start=2024&end=2025")
    assert response.status_code == 200
