"""Tests for local environment loading."""

import os

from backend.app.settings import load_local_environment


def test_load_local_environment_uses_root_env_without_overriding_shell_values(
    monkeypatch,
    tmp_path,
) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "\n".join(
            [
                "OPENAI_MODEL=model-from-env-file",
                "FEEDBACK_INSIGHTS_DB=backend/from-env-file.sqlite3",
            ]
        ),
        encoding="utf-8",
    )

    monkeypatch.setenv("OPENAI_MODEL", "model-from-shell")
    monkeypatch.delenv("FEEDBACK_INSIGHTS_DB", raising=False)

    load_local_environment(env_file)

    assert load_local_environment(env_file) is None
    assert os.environ["OPENAI_MODEL"] == "model-from-shell"
    assert os.environ["FEEDBACK_INSIGHTS_DB"] == "backend/from-env-file.sqlite3"
