from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypedDict, Dict

from ..._types import FileTypes

__all__ = ["TranscriptionCreateParams"]


class TranscriptionCreateParams(TypedDict, total=False):
    files: Required[FileTypes]
    """
    The audio file object (not file name) to transcribe, in one of these formats:
    flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.
    """

    lang: str
    """The language of the input audio.

    Supplying the input language in
    [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will
    improve accuracy and latency.
    """

    input_format: Required[str]
    """
    The format of the input file.
    """

    response_format: Literal["json", "verbose_json"]
    """
    The format of the transcript output, in one of these options: `json` or `verbose_json`.
    """

    temperature: float
    """The sampling temperature, between 0 and 1.

    Higher values like 0.8 will make the output more random, while lower values like
    0.2 will make it more focused and deterministic. If set to 0, the model will use
    [log probability](https://en.wikipedia.org/wiki/Log_probability) to
    automatically increase the temperature until certain thresholds are hit.
    """

    temperature_inc: float

    request_id: str
    """
    The id of the request.
    """

