from fastapi import Path
from app.errors import DomainError


def get_symbol(
    symbol: str = Path(
        ...,
        min_length=3,
        max_length=3,
        description="Security symbol (ticker).",
        examples=["DDL", "DIH", "DTC"],
    )
) -> str:
    cleaned = symbol.strip().upper()

    if not cleaned:
        raise DomainError(
            code="EMPTY_SYMBOL",
            message="Symbol cannot be blank",
            status=400,
        )

    if not cleaned.isalpha():
        raise DomainError(
            code="INVALID_SYMBOL_FORMAT",
            message="Symbol must contain only letters",
            status=400,
            details={"symbol": symbol},
        )

    return cleaned
