"""Tests for FastAPI route behavior that does not call OpenAI."""

from fastapi.testclient import TestClient

from backend.app.main import app
from backend.app.schemas import ExtractionResult


def _use_temp_database(monkeypatch, tmp_path) -> None:
    monkeypatch.setenv("FEEDBACK_INSIGHTS_DB", str(tmp_path / "feedback.sqlite3"))


def _mock_extraction(monkeypatch) -> None:
    def fake_extract(feedback_text: str) -> ExtractionResult:
        if "slow" in feedback_text.lower():
            return ExtractionResult(
                sentiment="negative",
                themes=["dashboard speed"],
                action_items=["Improve dashboard speed"],
            )
        return ExtractionResult(
            sentiment="positive",
            themes=["product usefulness"],
            action_items=[],
        )

    monkeypatch.setattr("backend.app.services.extract_feedback_insights", fake_extract)


def test_health_endpoint(monkeypatch, tmp_path) -> None:
    _use_temp_database(monkeypatch, tmp_path)
    with TestClient(app) as client:
        response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_feedback_endpoint_fails_gracefully_without_api_key(monkeypatch, tmp_path) -> None:
    _use_temp_database(monkeypatch, tmp_path)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with TestClient(app) as client:
        response = client.post("/feedback", json={"text": "Please add CSV export."})

    assert response.status_code == 503
    assert response.json()["detail"] == "OPENAI_API_KEY is not set"


def test_post_feedback_then_get_dashboard_succeeds(monkeypatch, tmp_path) -> None:
    _use_temp_database(monkeypatch, tmp_path)
    _mock_extraction(monkeypatch)

    with TestClient(app) as client:
        post_response = client.post(
            "/feedback",
            json={"text": "The product is useful.\nThe dashboard is slow."},
        )
        dashboard_response = client.get("/dashboard")

    assert post_response.status_code == 201
    assert dashboard_response.status_code == 200
    dashboard = dashboard_response.json()
    assert dashboard["total_feedback"] == 2
    assert dashboard["theme_frequencies"]
    assert dashboard["sentiment_distribution"] == {
        "positive": 1,
        "neutral": 0,
        "negative": 1,
    }
    assert dashboard["sentiment_trend"]


def test_post_feedback_then_get_feedback_succeeds(monkeypatch, tmp_path) -> None:
    _use_temp_database(monkeypatch, tmp_path)
    _mock_extraction(monkeypatch)

    with TestClient(app) as client:
        post_response = client.post(
            "/feedback",
            json={"text": "The product is useful.\nThe dashboard is slow."},
        )
        feedback_response = client.get("/feedback")

    assert post_response.status_code == 201
    assert feedback_response.status_code == 200
    records = feedback_response.json()
    assert len(records) == 2
    assert {record["feedback_text"] for record in records} == {
        "The product is useful.",
        "The dashboard is slow.",
    }


def test_repeated_dashboard_and_feedback_reads_after_insert(monkeypatch, tmp_path) -> None:
    _use_temp_database(monkeypatch, tmp_path)
    _mock_extraction(monkeypatch)

    with TestClient(app) as client:
        post_response = client.post(
            "/feedback",
            json={"text": "The product is useful.\nThe dashboard is slow."},
        )
        assert post_response.status_code == 201

        for _ in range(3):
            dashboard_response = client.get("/dashboard")
            feedback_response = client.get("/feedback")

            assert dashboard_response.status_code == 200
            assert feedback_response.status_code == 200
            assert dashboard_response.json()["total_feedback"] == 2
            assert len(feedback_response.json()) == 2
