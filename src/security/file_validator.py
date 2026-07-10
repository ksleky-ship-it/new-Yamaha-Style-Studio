"""File validation and security checks."""

from pathlib import Path

from src.exceptions import FileValidationError

MAX_FILE_SIZE = 1024 * 1024 * 500
ALLOWED_EXTENSIONS = [".mp3", ".wav", ".flac", ".ogg", ".m4a"]


class FileValidator:
    """Validate input and output files."""

    @staticmethod
    def validate_input_file(filepath: Path | str) -> bool:
        """Validate input audio file.

        Args:
            filepath: Path to input file

        Returns:
            True if valid

        Raises:
            FileValidationError: If validation fails
        """
        filepath = Path(filepath)

        if not filepath.exists():
            raise FileValidationError(f"File not found: {filepath}")

        if filepath.suffix.lower() not in ALLOWED_EXTENSIONS:
            raise FileValidationError(
                f"Invalid extension: {filepath.suffix}. "
                f"Allowed: {ALLOWED_EXTENSIONS}"
            )

        file_size = filepath.stat().st_size
        if file_size > MAX_FILE_SIZE:
            raise FileValidationError(
                f"File too large: {file_size / 1024 / 1024:.1f}MB. "
                f"Max: {MAX_FILE_SIZE / 1024 / 1024:.1f}MB"
            )

        return True

    @staticmethod
    def validate_output_dir(dirpath: Path | str) -> Path:
        """Validate and create output directory.

        Args:
            dirpath: Output directory path

        Returns:
            Path object of validated directory
        """
        dirpath = Path(dirpath)
        dirpath.mkdir(parents=True, exist_ok=True)
        return dirpath