"""Provider-neutral image generation contract.

This module deliberately contains no network client. The default adapter is
BLOCKED, and the test double only returns simulated metadata without writing
an image file. A real provider must be separately reviewed and implemented.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol


class AdapterBlocked(RuntimeError):
    """Raised when generation is not explicitly and safely configured."""


@dataclass(frozen=True)
class GenerationRequest:
    figure_id: str
    prompt: str
    output_dir: Path
    requested_size: str = "2560x1600"


@dataclass(frozen=True)
class GenerationResult:
    status: str
    provider: str
    figure_id: str
    output_path: Path | None = None
    sha256: str | None = None
    estimated_cost_usd: float | None = None
    note: str = ""


class ImageGenerationAdapter(Protocol):
    def generate(self, request: GenerationRequest) -> GenerationResult:
        """Generate and persist an image only for an enabled real provider."""


class BlockedAdapter:
    """Safe default. It never contacts a service or creates a file."""

    provider = "disabled"

    def generate(self, request: GenerationRequest) -> GenerationResult:
        raise AdapterBlocked(
            "Image generation is BLOCKED: configure a reviewed provider, confirm its terms, "
            "and obtain explicit budget approval before making any request."
        )


class TestDoubleAdapter:
    """No-cost test double. It never creates a fake PNG or any other image."""

    provider = "test-double"

    def generate(self, request: GenerationRequest) -> GenerationResult:
        if not request.figure_id.startswith("CH"):
            raise ValueError("figure_id must be a chapter-scoped permanent ID")
        if not request.prompt.strip():
            raise ValueError("prompt must not be empty")
        return GenerationResult(
            status="simulated",
            provider=self.provider,
            figure_id=request.figure_id,
            output_path=None,
            sha256=None,
            estimated_cost_usd=0.0,
            note="Test-only simulation. No image bytes were generated or written.",
        )


def require_paid_authorization(
    *,
    provider: str,
    enabled: bool,
    budget_approved: bool,
    max_spend_usd: float,
    estimated_cost_usd: float,
) -> None:
    """Fail closed unless provider use and a sufficient non-zero cap are explicit."""
    if not provider or provider == "disabled":
        raise AdapterBlocked("No image provider is enabled.")
    if not enabled:
        raise AdapterBlocked("Image provider calls require explicit enablement.")
    if not budget_approved:
        raise AdapterBlocked("Image provider calls require explicit budget approval.")
    if max_spend_usd <= 0:
        raise AdapterBlocked("max_spend_usd must be greater than zero.")
    if estimated_cost_usd < 0 or estimated_cost_usd > max_spend_usd:
        raise AdapterBlocked("Estimated cost is outside the approved spend cap.")


def default_adapter() -> ImageGenerationAdapter:
    return BlockedAdapter()
