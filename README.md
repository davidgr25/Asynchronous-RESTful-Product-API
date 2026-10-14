# Product Catalog & Inventory RESTful API (FastAPI)

Asynchronous RESTful microservice built with FastAPI, Layered Architecture, and SQLAlchemy 2.0 with asynchronous persistence (SQLite + aiosqlite).

## 1. Layered Architecture
- **API / Routers (`app/api/`)**: Handlers for HTTP requests, dependency injection, and status codes.
- **Services (`app/services/`)**: Business logic, SKU uniqueness validation, and HTTP exceptions.
- **Repositories (`app/repositories/`)**: Asynchronous data access layer using SQLAlchemy 2.0 `AsyncSession`, `select()`, and `commit()`.
- **Models (`app/models/`)**: Declarative ORM models.
- **Schemas (`app/schemas/`)**: Pydantic DTOs for input validation and serialization.
- **Core (`app/core/`)**: Async engine and session configuration.

## 2. Installation & Execution
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
