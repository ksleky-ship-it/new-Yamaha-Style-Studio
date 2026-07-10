"""Validation error classes."""


class ValidationError(Exception):
    """Base exception for validation errors."""
    pass


class FileValidationError(ValidationError):
    """Raised when file validation fails."""
    pass


class ConfigValidationError(ValidationError):
    """Raised when configuration validation fails."""
    pass