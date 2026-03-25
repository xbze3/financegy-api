from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_price_change():
    response = client.get("/v2/securities/DDL/price-change")
    assert response.status_code == 200


def test_get_price_change_percent():
    response = client.get("/v2/securities/DDL/price-change/percent")
    assert response.status_code == 200


def test_get_average_price():
    response = client.get("/v2/securities/DDL/analytics/average-price?n=30")
    assert response.status_code == 200


def test_get_sessions_volatility():
    response = client.get("/v2/securities/DDL/analytics/volatility?n=30")
    assert response.status_code == 200


def test_get_ytd_high_low():
    response = client.get("/v2/securities/DDL/analytics/ytd-high-low")
    assert response.status_code == 200


def test_get_market_snapshot():
    response = client.get("/v2/market/snapshot")
    assert response.status_code == 200


def test_get_movers():
    response = client.get("/v2/market/movers")
    assert response.status_code == 200


def test_calculate_position_value():
    response = client.get("/v2/securities/DDL/position/value?shares=100")
    assert response.status_code == 200


def test_calculate_position_return():
    response = client.get(
        "/v2/securities/DDL/position/return?shares=100&purchase_price=300"
    )
    assert response.status_code == 200


def test_calculate_position_return_percent():
    response = client.get(
        "/v2/securities/DDL/position/return/percent?shares=100&purchase_price=300"
    )
    assert response.status_code == 200


def test_calculate_portfolio_summary():
    response = client.post(
        "/v2/portfolio/summary",
        json=[
            {
                "symbol": "DDL",
                "shares": 100,
                "purchase_price": 300,
            }
        ],
    )
    assert response.status_code == 200


def test_get_securities_v2():
    response = client.get("/v2/securities")
    assert response.status_code == 200


def test_get_active_securities():
    response = client.get("/v2/securities/active")
    assert response.status_code == 200


def test_search_securities_v2():
    response = client.get("/v2/securities/search?q=ddl")
    assert response.status_code == 200


def test_get_security_by_symbol_v2():
    response = client.get("/v2/securities/DDL")
    assert response.status_code == 200


def test_get_recent_session():
    response = client.get("/v2/sessions/recent")
    assert response.status_code == 200


def test_get_session_trades_v2():
    response = client.get("/v2/sessions/1056/trades")
    assert response.status_code == 200


def test_get_security_session_trade_v2():
    response = client.get("/v2/securities/DDL/sessions/1056/trades")
    assert response.status_code == 200


def test_get_latest_session_for_symbol():
    response = client.get("/v2/securities/DDL/sessions/latest")
    assert response.status_code == 200


def test_get_session_date():
    response = client.get("/v2/session/1056/date")
    assert response.status_code == 200


def test_get_recent_trade_v2():
    response = client.get("/v2/securities/DDL/trades/latest")
    assert response.status_code == 200


def test_get_trades_for_year_v2():
    response = client.get("/v2/securities/DDL/trades?y=2024")
    assert response.status_code == 200


def test_get_security_recent_year_v2():
    response = client.get("/v2/securities/DDL/trades/recent-year")
    assert response.status_code == 200


def test_get_historical_trades_v2():
    response = client.get("/v2/securities/DDL/trades/history?start=2024&end=2025")
    assert response.status_code == 200


def test_get_security_full_history():
    response = client.get("/v2/securities/BDH/trades/full-history")
    assert response.status_code == 200


def test_get_security_traded_years():
    response = client.get("/v2/securities/DDL/traded-years")
    assert response.status_code == 200


def test_get_year_sessions():
    response = client.get("/v2/sessions/year/2026")
    assert response.status_code == 200


def test_get_year_sessions_snapshot():
    response = client.get("/v2/sessions/year/2026/snapshot")
    assert response.status_code == 200
