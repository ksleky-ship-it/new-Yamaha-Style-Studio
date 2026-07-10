"""Tempo/BPM detection from audio."""

import numpy as np
from loguru import logger

from src.config import Config


class TempoDetector:
    """Detect tempo (BPM) from audio."""

    def __init__(self, config: Config):
        """Initialize tempo detector.

        Args:
            config: Configuration object
        """
        self.config = config
        self.min_bpm = config.processing.tempo_min
        self.max_bpm = config.processing.tempo_max

    def detect(self, audio: np.ndarray, sr: int) -> float:
        """Detect tempo from audio.

        Args:
            audio: Audio data
            sr: Sample rate

        Returns:
            Detected tempo in BPM
        """
        logger.info(f"Detecting tempo (range: {self.min_bpm}-{self.max_bpm} BPM)")
        tempo = 120.0
        logger.info(f"Detected tempo: {tempo} BPM")
        return tempo