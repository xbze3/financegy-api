from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class DomainError(Exception):
    code: str
    message: str
    status: int = 400
    details: dict[str, Any] | None = None


def error_payload(
    *, code: str, message: str, request_id: str, details: dict[str, Any] | None = None
):
    return {
        "error": {
            "code": code,
            "message": message,
            "details": details or {},
            "request_id": request_id,
        }
    }
