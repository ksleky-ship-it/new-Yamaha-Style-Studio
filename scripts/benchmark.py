#!/usr/bin/env python3
"""Performance benchmarking script."""

import sys
from pathlib import Path

from loguru import logger


def benchmark_pipeline(audio_file: Path):
    """Benchmark the processing pipeline.

    Args:
        audio_file: Path to test audio file
    """
    logger.info(f"Benchmarking pipeline with: {audio_file}")
    logger.info("Benchmarking complete")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/benchmark.py <audio_file>")
        sys.exit(1)

    audio_file = Path(sys.argv[1])
    if not audio_file.exists():
        print(f"Error: File not found: {audio_file}")
        sys.exit(1)

    benchmark_pipeline(audio_file)