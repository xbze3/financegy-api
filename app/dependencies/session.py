from fastapi import Path
from app.errors import DomainError


def get_session_id(
    session: str = Path(
        ...,
        min_length=3,
        max_length=6,
        description="Trading session ID.",
        examples=["1140", "1150", "1155"],
    )
) -> int:

    earlist_session = 754

    if int(session) < earlist_session:
        raise DomainError(
            code="SESSION_OUT_OF_RANGE",
            message=f"Session cannot be earlier than session {earlist_session}",
            status=400,
            details={"session": session},
        )

    if not session.isdigit():
        raise DomainError(
            code="INVALID_SESSION_FORMAT",
            message="Session ID must be numeric",
            status=400,
            details={"session": session},
        )

    session_id = int(session)

    if session_id <= 0:
        raise DomainError(
            code="INVALID_SESSION_ID",
            message="Session ID must be a positive number",
            status=400,
            details={"session": session},
        )

    return session_id
