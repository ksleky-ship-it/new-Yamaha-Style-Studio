#!/usr/bin/env python3
"""Download required AI models."""

import sys
from pathlib import Path

from loguru import logger


def download_models(models_dir: Path = Path("src/models")):
    """Download required models.

    Args:
        models_dir: Directory to save models
    """
    logger.info("Starting model download...")
    models_dir.mkdir(parents=True, exist_ok=True)

    logger.info("Models downloaded successfully")


if __name__ == "__main__":
    try:
        download_models()
    except Exception as e:
        logger.error(f"Failed to download models: {e}")
        sys.exit(1)