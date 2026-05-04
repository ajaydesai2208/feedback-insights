"""Tests for FastAPI route behavior that does not call OpenAI."""

from fastapi.testclient import TestClient

from backend.app.main import app


def test_health_endpoint() -> None:
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_feedback_endpoint_fails_gracefully_without_api_key(monkeypatch) -> None:
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with TestClient(app) as client:
        response = client.post("/feedback", json={"text": "Please add CSV export."})

    assert response.status_code == 503
    assert response.json()["detail"] == "OPENAI_API_KEY is not set"
