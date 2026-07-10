"""Pipeline execution error classes."""


class PipelineError(Exception):
    """Base exception for pipeline-related errors."""
    pass


class PipelineExecutionError(PipelineError):
    """Raised when pipeline execution fails."""
    pass


class PipelineValidationError(PipelineError):
    """Raised when pipeline validation fails."""
    pass