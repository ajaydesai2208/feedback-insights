"""FastAPI application entrypoint."""

from collections.abc import AsyncIterator, Iterator
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlite3 import Connection

from backend.app.dashboard import build_dashboard
from backend.app.db import connect, initialize_database, list_feedback
from backend.app.llm import LLMConfigurationError, LLMOutputError, LLMProviderError
from backend.app.schemas import (
    DashboardResponse,
    FeedbackCreateRequest,
    FeedbackCreateResponse,
    FeedbackRecordResponse,
    HealthResponse,
)
from backend.app.services import ingest_feedback_batch


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    connection = connect()
    try:
        initialize_database(connection)
        yield
    finally:
        connection.close()


app = FastAPI(title="Feedback Insights API", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


def get_connection() -> Iterator[Connection]:
    connection = connect()
    try:
        initialize_database(connection)
        yield connection
    finally:
        connection.close()


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.post("/feedback", response_model=FeedbackCreateResponse, status_code=status.HTTP_201_CREATED)
def create_feedback(
    request: FeedbackCreateRequest,
    connection: Connection = Depends(get_connection),
) -> FeedbackCreateResponse:
    try:
        records = ingest_feedback_batch(connection, request.text)
    except LLMConfigurationError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
    except LLMOutputError as exc:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc
    except LLMProviderError as exc:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=str(exc)) from exc

    return FeedbackCreateResponse(records=records)


@app.get("/feedback", response_model=list[FeedbackRecordResponse])
def get_feedback(connection: Connection = Depends(get_connection)) -> list[FeedbackRecordResponse]:
    return list_feedback(connection)


@app.get("/dashboard", response_model=DashboardResponse)
def get_dashboard(connection: Connection = Depends(get_connection)) -> DashboardResponse:
    return build_dashboard(list_feedback(connection))
