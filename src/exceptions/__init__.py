"""Exception classes for YamahaStyleStudio."""

from src.exceptions.audio_errors import (
    AudioError,
    AudioLoadError,
    AudioProcessingError,
    InvalidAudioFormat,
)
from src.exceptions.pipeline_errors import (
    PipelineError,
    PipelineExecutionError,
    PipelineValidationError,
)
from src.exceptions.validation_errors import (
    ValidationError,
    FileValidationError,
    ConfigValidationError,
)

__all__ = [
    "AudioError",
    "AudioLoadError",
    "AudioProcessingError",
    "InvalidAudioFormat",
    "PipelineError",
    "PipelineExecutionError",
    "PipelineValidationError",
    "ValidationError",
    "FileValidationError",
    "ConfigValidationError",
]