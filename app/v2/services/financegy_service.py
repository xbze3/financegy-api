import financegy
from datetime import date


def get_securities():
    securities = financegy.get_securities()
    return securities


def get_active_securities():
    active_securities = financegy.get_active_securities()
    return active_securities


def get_recent_session():
    recent_session = financegy.get_recent_session()
    return recent_session


def get_security_by_symbol(symbol: str):
    security_name = financegy.get_security_by_symbol(symbol)
    return security_name


def get_recent_trade(symbol: str):
    recent_trade = financegy.get_recent_trade(symbol)
    return recent_trade


def get_previous_close(symbol: str):
    previous_close = financegy.get_previous_close(symbol)
    return previous_close


def get_price_change(symbol: str):
    price_change = financegy.get_price_change(symbol)
    return price_change


def get_price_change_percent(symbol: str):
    price_change_percent = financegy.get_price_change_percent(symbol)
    return price_change_percent


def get_security_recent_year(symbol: str):
    recent_year = financegy.get_security_recent_year(symbol)
    return recent_year


def get_security_earliest_year(symbol: str):
    earliest_year = financegy.get_security_earliest_year(symbol)
    return earliest_year


def get_security_latest_year(symbol: str):
    latest_year = financegy.get_security_latest_year(symbol)
    return latest_year


def get_security_full_history(symbol: str):
    full_history = financegy.get_security_full_history(symbol)
    return full_history


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


def get_historical_trades(symbol: str, start_date, end_date):

    start_date_str = start_date.strftime("%d/%m/%Y")
    end_date_str = end_date.strftime("%d/%m/%Y")

    historical_trades = financegy.get_historical_trades(
        symbol=symbol,
        start_date=start_date_str,
        end_date=end_date_str,
    )
    return historical_trades


def get_latest_session_for_symbol(symbol: str):
    latest_session = financegy.get_latest_session_for_symbol(symbol)
    return latest_session


def get_sessions_average_price(symbol: str, start_session: str, end_session: str):
    avg_price_range = financegy.get_sessions_average_price(
        symbol, start_session, end_session
    )
    return avg_price_range


def get_average_price(symbol: str, n_sessions: int):
    avg_price_latest = financegy.get_average_price(symbol, n_sessions)
    return avg_price_latest


def get_sessions_volatility(symbol: str, n_sessions: int):
    volatility = financegy.get_sessions_volatility(symbol, n_sessions)
    return volatility


def get_ytd_high_low(symbol: str):
    ytd_high_low = financegy.get_ytd_high_low(symbol)
    return ytd_high_low


def calculate_position_value(symbol: str, shares):
    position_value = financegy.calculate_position_value(symbol, shares=shares)
    return position_value


def calculate_position_return(symbol: str, shares, purchase_price):
    position_return = financegy.calculate_position_return(
        symbol=symbol,
        shares=shares,
        purchase_price=purchase_price,
    )
    return position_return


def calculate_position_return_percent(symbol: str, shares, purchase_price):
    position_return_percent = financegy.calculate_position_return_percent(
        symbol=symbol,
        shares=shares,
        purchase_price=purchase_price,
    )
    return position_return_percent


def calculate_portfolio_summary(portfolio):
    portfolio_summary = financegy.calculate_portfolio_summary(portfolio)
    return portfolio_summary
