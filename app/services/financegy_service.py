import financegy
from datetime import date


def get_securities():
    securities = financegy.get_securities()
    return securities


def get_security_by_symbol(symbol: str):
    security_name = financegy.get_security_by_symbol(symbol)
    return security_name


def get_recent_trade(symbol: str):
    recent_trade = financegy.get_recent_trade(symbol)
    return recent_trade


def get_security_recent_year(symbol: str):
    recent_year = financegy.get_security_recent_year(symbol)
    return recent_year


def get_session_trades(session: str):
    session_trades = financegy.get_session_trades(session)
    return session_trades


def get_security_session_trade(symbol: str, session: str):
    security_session_trade = financegy.get_security_session_trade(symbol, session)
    return security_session_trade


def search_securities(symbol: str):
    search_results = financegy.search_securities(symbol)
    return search_results


def get_trades_for_year(symbol: str, year: str):
    year_trades = financegy.get_trades_for_year(symbol, year)
    return year_trades


from datetime import date


def get_historical_trades(symbol: str, start_date: date, end_date: date):
    start_date_str = start_date.strftime("%d/%m/%Y")
    end_date_str = end_date.strftime("%d/%m/%Y")

    historical_trades = financegy.get_historical_trades(
        symbol,
        start_date_str,
        end_date_str,
    )
    return historical_trades
