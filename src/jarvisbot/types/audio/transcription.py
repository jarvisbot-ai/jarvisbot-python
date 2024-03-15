from typing import List
from ..._models import BaseModel

__all__ = ["Transcription"]


class Transcription(BaseModel):
    id: str
    """A unique identifier for the transcription."""

    object: str
    """The object type."""

    created: int
    """The Unix timestamp (in seconds) of when the chat completion was created."""

    model: str
    """The model used for the transcription."""

    message: str
    """The message for the transcription."""

    text: str
    """The text for the transcription."""
