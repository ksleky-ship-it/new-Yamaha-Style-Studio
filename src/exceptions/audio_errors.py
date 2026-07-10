"""Audio processing error classes."""


class AudioError(Exception):
    """Base exception for audio-related errors."""
    pass


class AudioLoadError(AudioError):
    """Raised when audio file cannot be loaded."""
    pass


class AudioProcessingError(AudioError):
    """Raised when audio processing fails."""
    pass


class InvalidAudioFormat(AudioError):
    """Raised when audio format is not supported."""
    pass