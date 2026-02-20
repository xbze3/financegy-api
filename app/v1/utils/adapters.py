from app.v1.schemas.trades import TradeOut
from app.v1.schemas.sessions import SessionOut


def adapt_trade_v1(new: dict):
    """Convert FinanceGY 4.1.0 trade payload (v2 shape) into legacy v1 shape."""
    return TradeOut(
        session=new["session"],
        date=new["session_date"],
        ltp=new.get("last_trade_price"),
        best_bid=new.get("eps"),
        vol_bid=new.get("pe_ratio"),
        best_offer=new.get("dividends_paid_last_12_months"),
        vol_offer=new.get("dividend_yield"),
        opening_price=new.get("notes"),
    )


def adapt_trade_list_v1(new_list: list[dict]):
    return [adapt_trade_v1(trade) for trade in new_list]


def adapt_session_v1(new: dict):
    """Convert FinanceGY 4.1.0 session payload (v2 shape) into legacy v1 shape."""
    return SessionOut(
        symbol=new["symbol"],
        ltp=new.get("last_trade_price"),
        best_bid=new.get("eps"),
        vol_bid=new.get("pe_ratio"),
        best_offer=new.get("dividends_paid_last_12_months"),
        vol_offer=new.get("dividend_yield"),
        opening_price=new.get("notes"),
    )


def adapt_session_list_v1(new_list: list[dict]):
    return [adapt_session_v1(session) for session in new_list]
