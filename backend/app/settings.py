"""Local environment configuration helpers."""

from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_PATH = PROJECT_ROOT / ".env"


def load_local_environment(env_path: Path = ENV_PATH) -> None:
    """Load root .env values without overriding shell-provided variables."""
    load_dotenv(env_path, override=False)
