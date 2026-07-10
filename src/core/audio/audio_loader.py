"""Audio file loading and normalization."""

from pathlib import Path
from typing import Tuple

import librosa
import numpy as np
from loguru import logger

from src.config import Config
from src.exceptions import AudioLoadError, InvalidAudioFormat


class AudioLoader:
    """Load and preprocess audio files."""

    SUPPORTED_FORMATS = [".mp3", ".wav", ".flac", ".ogg", ".m4a"]

    def __init__(self, config: Config):
        """Initialize audio loader.

        Args:
            config: Configuration object
        """
        self.config = config
        self.sr = config.audio.sample_rate

    def load(
        self, audio_path: Path | str, mono: bool = False
    ) -> Tuple[np.ndarray, int]:
        """Load audio file.

        Args:
            audio_path: Path to audio file
            mono: Convert to mono if True

        Returns:
            Tuple of (audio_data, sample_rate)

        Raises:
            InvalidAudioFormat: If file format is not supported
            AudioLoadError: If loading fails
        """
        audio_path = Path(audio_path)

        if audio_path.suffix.lower() not in self.SUPPORTED_FORMATS:
            raise InvalidAudioFormat(
                f"Format {audio_path.suffix} not supported. "
                f"Supported: {self.SUPPORTED_FORMATS}"
            )

        try:
            logger.info(f"Loading audio file: {audio_path}")
            audio, sr = librosa.load(str(audio_path), sr=self.sr, mono=mono)
            logger.info(f"Audio loaded: duration={len(audio)/sr:.2f}s, sr={sr}Hz")
            return audio, sr
        except Exception as e:
            raise AudioLoadError(f"Failed to load audio file: {e}") from e

    def normalize(self, audio: np.ndarray, target_db: float = -3.0) -> np.ndarray:
        """Normalize audio to target loudness.

        Args:
            audio: Audio data
            target_db: Target loudness in dB

        Returns:
            Normalized audio data
        """
        logger.info(f"Normalizing audio to {target_db}dB")
        rms = np.sqrt(np.mean(audio**2))
        current_db = 20 * np.log10(rms + 1e-10)
        gain_db = target_db - current_db
        gain = 10 ** (gain_db / 20)
        normalized = audio * gain
        normalized = np.tanh(normalized)
        return normalized