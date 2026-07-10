"""Configuration management for YamahaStyleStudio."""

import json
from pathlib import Path
from typing import Any, Dict

import yaml
from pydantic import BaseModel, Field


class AudioConfig(BaseModel):
    """Audio processing configuration."""

    sample_rate: int = Field(44100, ge=8000, le=192000)
    channels: int = Field(2, ge=1, le=8)
    bit_depth: int = Field(16)
    normalize: bool = True
    normalization_level: float = Field(-3.0, ge=-60, le=0)


class ProcessingConfig(BaseModel):
    """Processing pipeline configuration."""

    transcription_model: str = Field("basic_pitch")
    tempo_min: int = Field(40, ge=20, le=400)
    tempo_max: int = Field(240, ge=20, le=400)
    chord_enabled: bool = True
    genre_enabled: bool = True
    structure_enabled: bool = True


class SynthesisConfig(BaseModel):
    """Synthesis configuration."""

    sty_format: str = Field("sff2")
    midi_format: str = Field("smf_type1")
    ticks_per_quarter: int = Field(480, ge=96, le=960)


class OutputConfig(BaseModel):
    """Output configuration."""

    base_dir: str = "output"
    create_subdirs: bool = True
    formats: list = Field(default_factory=lambda: ["sty", "mid"])
    keep_intermediates: bool = True


class Config(BaseModel):
    """Main configuration class."""

    audio: AudioConfig = Field(default_factory=AudioConfig)
    processing: ProcessingConfig = Field(default_factory=ProcessingConfig)
    synthesis: SynthesisConfig = Field(default_factory=SynthesisConfig)
    output: OutputConfig = Field(default_factory=OutputConfig)
    debug: bool = False
    environment: str = Field("production")

    @classmethod
    def from_file(cls, filepath: Path | str) -> "Config":
        """Load configuration from YAML or JSON file."""
        filepath = Path(filepath)
        if not filepath.exists():
            raise FileNotFoundError(f"Config file not found: {filepath}")

        with open(filepath, "r") as f:
            if filepath.suffix in [".yaml", ".yml"]:
                data = yaml.safe_load(f)
            elif filepath.suffix == ".json":
                data = json.load(f)
            else:
                raise ValueError(f"Unsupported file format: {filepath.suffix}")

        return cls(**data)

    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return self.model_dump()

    def to_yaml(self) -> str:
        """Convert configuration to YAML string."""
        return yaml.dump(self.model_dump())