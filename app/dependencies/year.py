from fastapi import Query, Path
from datetime import date
from app.errors import DomainError


def get_year(
    y: str = Query(
        ...,
        min_length=4,
        max_length=4,
        description="Year (YYYY).",
        examples=["2024", "2023"],
    )
) -> int:
    if not y.isdigit():
        raise DomainError(
            code="INVALID_YEAR_FORMAT",
            message="Year must be a 4-digit number",
            status=400,
            details={"year": y},
        )

    year = int(y)

    current_year = date.today().year
    earliest_year = 2018

    if year < earliest_year:
        raise DomainError(
            code="YEAR_OUT_OF_RANGE",
            message=f"Year cannot be earlier than {earliest_year}",
            status=400,
            details={"year": year},
        )

    if year > current_year:
        raise DomainError(
            code="YEAR_IN_FUTURE",
            message="Year cannot be in the future",
            status=400,
            details={"year": year},
        )

    return year


def get_year_path(
    year: str = Path(
        ...,
        min_length=4,
        max_length=4,
        description="Year (YYYY).",
        examples=["2024", "2023"],
    )
) -> int:
    if not year.isdigit():
        raise DomainError(
            code="INVALID_YEAR_FORMAT",
            message="Year must be a 4-digit number",
            status=400,
            details={"year": year},
        )

    year = int(year)

    current_year = date.today().year
    earliest_year = 2018

    if year < earliest_year:
        raise DomainError(
            code="YEAR_OUT_OF_RANGE",
            message=f"Year cannot be earlier than {earliest_year}",
            status=400,
            details={"year": year},
        )

    if year > current_year:
        raise DomainError(
            code="YEAR_IN_FUTURE",
            message="Year cannot be in the future",
            status=400,
            details={"year": year},
        )

    return year
