from __future__ import annotations

import re
import calendar
from dataclasses import dataclass
from datetime import date
from fastapi import Query
from app.errors import DomainError


@dataclass(frozen=True)
class FlexibleDate:
    value: date
    granularity: str


def _parse_flexible_date(raw: str, *, is_end: bool) -> FlexibleDate:
    s = " ".join(raw.strip().split())

    if not s:
        raise DomainError(
            code="EMPTY_DATE",
            message="Date value cannot be blank",
            status=400,
            details={"value": raw},
        )

    # dd/mm/yyyy
    m = re.fullmatch(r"(\d{2})/(\d{2})/(\d{4})", s)
    if m:
        dd, mm, yyyy = map(int, m.groups())
        try:
            return FlexibleDate(date(yyyy, mm, dd), "day")
        except ValueError:
            raise DomainError(
                code="INVALID_DATE",
                message="Invalid day/month/year in date",
                status=400,
                details={"value": s},
            )

    # mm/yyyy
    m = re.fullmatch(r"(\d{2})/(\d{4})", s)
    if m:
        mm, yyyy = map(int, m.groups())
        if not (1 <= mm <= 12):
            raise DomainError(
                code="INVALID_DATE",
                message="Month must be between 01 and 12",
                status=400,
                details={"value": s},
            )
        if is_end:
            last_day = calendar.monthrange(yyyy, mm)[1]
            return FlexibleDate(date(yyyy, mm, last_day), "month")
        return FlexibleDate(date(yyyy, mm, 1), "month")

    # yyyy
    m = re.fullmatch(r"(\d{4})", s)
    if m:
        yyyy = int(m.group(1))
        if is_end:
            return FlexibleDate(date(yyyy, 12, 31), "year")
        return FlexibleDate(date(yyyy, 1, 1), "year")

    # No match
    raise DomainError(
        code="INVALID_DATE_FORMAT",
        message="Date must be `dd/mm/yyyy`, `mm/yyyy`, or `yyyy`",
        status=400,
        details={"value": s},
    )


@dataclass(frozen=True)
class DateRange:
    start: date
    end: date
    start_granularity: str
    end_granularity: str


def get_date_range(
    start: str = Query(
        ...,
        description="Start date (`dd/mm/yyyy` or `mm/yyyy` or `yyyy`).",
        examples=["01/06/2020", "01/2022", "2020"],
    ),
    end: str = Query(
        ...,
        description="End date (`dd/mm/yyyy` or `mm/yyyy` or `yyyy`).",
        examples=["01/06/2024", "12/2024", "2024"],
    ),
) -> DateRange:
    s = _parse_flexible_date(start, is_end=False)
    e = _parse_flexible_date(end, is_end=True)

    if s.value > e.value:
        raise DomainError(
            code="INVALID_DATE_RANGE",
            message="start must be before or equal to end",
            status=400,
            details={"start": str(s.value), "end": str(e.value)},
        )

    return DateRange(
        start=s.value,
        end=e.value,
        start_granularity=s.granularity,
        end_granularity=e.granularity,
    )
