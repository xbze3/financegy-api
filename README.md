# 🏦 FinanceGY Market Data API

A production-style REST API built with **FastAPI** that exposes financial market data from the **Guyana Stock Exchange (GSE)**.

This API is powered by **[FinanceGY](https://pypi.org/project/financegy/)**, an open-source Python library (also developed by me) that provides programmatic access to GSE securities, trade history, and session data. The API layer focuses on clean REST design, validation, documentation, and deployment readiness.

---

## Live Service

The API is publicly deployed and accessible at:

**Base URL:** [ https://financegy-api.onrender.com/ ]

**Interactive API Documentation:** [ https://financegy-api.onrender.com/docs ]

**OpenAPI Specification:** [ https://financegy-api.onrender.com/v1/openapi.json ]

This live deployment allows developers, applications, and dashboards to
access Guyana Stock Exchange data programmatically without needing to
install the FinanceGY library locally.

---

## Features

### Implemented

- RESTful API built with FastAPI
- Powered by the `financegy` Python library
- OpenAPI / Swagger documentation
- Pydantic request & response models (typed API contracts)
- Centralized input validation and consistent error handling
- API-level rate limiting (SlowAPI)
- Dockerized local development environment

### Planned / In Progress

- API-level caching (Redis when scaling becomes necessary)
- Cloud deployment (e.g. Render)

---

## API Documentation

Once the API is running, interactive documentation is available at:

- **Swagger UI:** `/docs`
- **ReDoc:** `/redoc`
- **OpenAPI Specification:** `/v1/openapi.json`

These docs are auto-generated and always stay in sync with the codebase. Check them out for route descriptions and requirements.

---

## About FinanceGY (Underlying Data Library)

**FinanceGY** is an unofficial Python library for accessing financial data from the **Guyana Stock Exchange (GSE)**. It provides a simple and consistent interface for retrieving securities and trade data programmatically.

### Installation

```bash
pip install financegy
```

### Quick Start

```python
import financegy

# Get a list of all traded securities
securities = financegy.get_securities()

# Get the name of a security by its ticker symbol
security_name = financegy.get_security_by_symbol("DDL")

# Get the most recent trade data for a security
recent_trade = financegy.get_recent_trade("DDL")

# Get all trade data for the most recent year
recent_year = financegy.get_security_recent_year("DDL")

# Get trade data for a specific trading session
session_trades = financegy.get_session_trades("1136")

# Get session trade data for a specific security
security_session_trade = financegy.get_security_session_trade("DDL", "1136")

# Search for securities by name or symbol
search_results = financegy.search_securities("DDL")

# Get all trades for a given year
year_trades = financegy.get_trades_for_year("DDL", "2019")

# Get historical trades within a date range
historical_trades = financegy.get_historical_trades(
    symbol="DDL",
    start_date="01/06/2020",
    end_date="01/2022"
)
```

---

## Data Utilities (FinanceGY)

| Function                              | Description                                 |
| ------------------------------------- | ------------------------------------------- |
| `to_dataframe(data)`                  | Converts trade data into a Pandas DataFrame |
| `save_to_csv(data, filename, path)`   | Saves data to a CSV file                    |
| `save_to_excel(data, filename, path)` | Saves data to an Excel file                 |

---

## Caching System (FinanceGY)

FinanceGY includes a lightweight local caching system to reduce unnecessary requests and improve performance.

- Cached responses are stored as JSON files in a local `cache/` directory
- Cache entries are valid for **7 days**
- Cached data is returned instantly when available

### Clearing the Cache

```python
import financegy
financegy.clear_cache()
```

### Bypassing Cache for a Request

```python
recent_trade = financegy.get_recent_trade("DDL", use_cache=False)
```

---

## Architecture Overview

```
routers → services → financegy → GSE data source
```

The API acts as a clean HTTP interface on top of the FinanceGY library, making the data accessible to frontend applications and other services.

---

## Running Locally (Docker)

The API can be run locally using **Docker Compose**, which automatically builds the image and binds ports for you.

### Prerequisites

- Docker
- Docker Compose

### Start the API

```bash
docker compose up --build
```

For subsequent runs (no dependency or Dockerfile changes):

```bash
docker compose up
```

The API will be available at:

```
http://localhost:8000/v1
```

To stop the containers:

```bash
docker compose down
```

---

## Rate Limiting

This API uses **SlowAPI** to protect endpoints from abuse.

- Strict per-route limits are applied to heavy or more sensitive endpoints (e.g. search, historical data)
- Limits are currently enforced in-memory

---

## Roadmap

- [x] Core API endpoints
- [x] OpenAPI / Swagger documentation
- [x] Pydantic response models
- [x] Centralized error handling
- [x] Rate limiting
- [x] Docker support
- [ ] API-level caching (Redis)
- [ ] Cloud deployment (Render)

---

## License

This project is licensed under the **MIT License**.
