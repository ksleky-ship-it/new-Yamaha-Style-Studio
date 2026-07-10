"""Tests for audio loading and processing."""

import pytest
from src.core.audio import AudioLoader
from src.exceptions import InvalidAudioFormat


class TestAudioLoader:
    """Test cases for AudioLoader."""

    def test_audio_loader_init(self, config):
        """Test AudioLoader initialization."""
        loader = AudioLoader(config)
        assert loader.sr == config.audio.sample_rate

    def test_invalid_format(self, config):
        """Test loading invalid audio format."""
        loader = AudioLoader(config)
        with pytest.raises(InvalidAudioFormat):
            loader.load("file.txt")