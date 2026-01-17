from fastapi import Query
from app.errors import DomainError


def get_search_query(
    q: str = Query(
        ...,
        min_length=1,
        max_length=50,
        description="Search term (symbol/company name/partial match).",
        examples=["DDL", "Demerara", "Banks DIH"],
    )
) -> str:
    cleaned = " ".join(q.strip().split())

    if len(cleaned) == 0:
        raise DomainError(
            code="EMPTY_SEARCH_QUERY",
            message="Search term cannot be blank",
            status=400,
        )

    return cleaned
