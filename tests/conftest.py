"""Pytest configuration and fixtures."""

import pytest
from pathlib import Path

from src.config import Config


@pytest.fixture
def config():
    """Provide a test configuration."""
    return Config(debug=True, environment="development")


@pytest.fixture
def test_audio_file():
    """Provide path to test audio file."""
    return Path("samples/test_audio.mp3")


@pytest.fixture
def temp_output_dir(tmp_path):
    """Provide temporary output directory."""
    return tmp_path / "output"