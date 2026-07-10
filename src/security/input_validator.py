"""Input validation and sanitization."""

import re

from src.exceptions import ValidationError


class InputValidator:
    """Validate and sanitize user inputs."""

    @staticmethod
    def validate_preset_name(preset: str) -> bool:
        """Validate preset name.

        Args:
            preset: Preset name

        Returns:
            True if valid

        Raises:
            ValidationError: If invalid
        """
        if not isinstance(preset, str):
            raise ValidationError("Preset name must be a string")

        if not re.match(r"^[a-z_]+$", preset):
            raise ValidationError("Preset name must contain only lowercase letters and underscores")

        return True

    @staticmethod
    def sanitize_filename(filename: str) -> str:
        """Sanitize filename to remove invalid characters.

        Args:
            filename: Original filename

        Returns:
            Sanitized filename
        """
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        filename = re.sub(r'\s+', '_', filename)
        return filename