"""YamahaStyleStudio - Convert MP3 to Yamaha keyboard styles."""

__version__ = "0.1.0"
__author__ = "YamahaStyleStudio Contributors"
__license__ = "MIT"

from src.core.pipeline import Orchestrator
from src.config import Config

__all__ = ["Orchestrator", "Config"]