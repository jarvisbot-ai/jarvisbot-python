from __future__ import annotations

from typing import Union, Optional, Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpeechCreateParams"]


class SpeechCreateParams(TypedDict, total=False):
    text: Required[str]
    """The text to generate audio for. The maximum length is 4096 characters."""

    model: str
    """
    The model used for the speech generation.
    """

    speaker_id: str
    """
    The id of the speaker.
    """

    response_format: str
    """
    The format of the generated audio.
    """

    speed: float
    """The speed of the generated audio.

    Select a value from `0.25` to `4.0`. `1.0` is the default.
    """
