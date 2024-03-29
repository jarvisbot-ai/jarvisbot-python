from __future__ import annotations

from .speech import (
    Speech,
    AsyncSpeech,
    SpeechWithRawResponse,
    AsyncSpeechWithRawResponse,
    SpeechWithStreamingResponse,
    AsyncSpeechWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

from .transcriptions import (
    Transcriptions,
    AsyncTranscriptions,
    TranscriptionsWithRawResponse,
    AsyncTranscriptionsWithRawResponse,
    TranscriptionsWithStreamingResponse,
    AsyncTranscriptionsWithStreamingResponse,
)

__all__ = ["Audio", "AsyncAudio"]


class Audio(SyncAPIResource):
    @cached_property
    def transcriptions(self) -> Transcriptions:
        return Transcriptions(self._client)

    @cached_property
    def speech(self) -> Speech:
        return Speech(self._client)

    @cached_property
    def with_raw_response(self) -> AudioWithRawResponse:
        return AudioWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudioWithStreamingResponse:
        return AudioWithStreamingResponse(self)


class AsyncAudio(AsyncAPIResource):
    @cached_property
    def transcriptions(self) -> AsyncTranscriptions:
        return AsyncTranscriptions(self._client)

    @cached_property
    def speech(self) -> AsyncSpeech:
        return AsyncSpeech(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAudioWithRawResponse:
        return AsyncAudioWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudioWithStreamingResponse:
        return AsyncAudioWithStreamingResponse(self)


class AudioWithRawResponse:
    def __init__(self, audio: Audio) -> None:
        self._audio = audio

    @cached_property
    def transcriptions(self) -> TranscriptionsWithRawResponse:
        return TranscriptionsWithRawResponse(self._audio.transcriptions)

    @cached_property
    def speech(self) -> SpeechWithRawResponse:
        return SpeechWithRawResponse(self._audio.speech)


class AsyncAudioWithRawResponse:
    def __init__(self, audio: AsyncAudio) -> None:
        self._audio = audio

    @cached_property
    def transcriptions(self) -> AsyncTranscriptionsWithRawResponse:
        return AsyncTranscriptionsWithRawResponse(self._audio.transcriptions)

    @cached_property
    def speech(self) -> AsyncSpeechWithRawResponse:
        return AsyncSpeechWithRawResponse(self._audio.speech)


class AudioWithStreamingResponse:
    def __init__(self, audio: Audio) -> None:
        self._audio = audio

    @cached_property
    def transcriptions(self) -> TranscriptionsWithStreamingResponse:
        return TranscriptionsWithStreamingResponse(self._audio.transcriptions)

    @cached_property
    def speech(self) -> SpeechWithStreamingResponse:
        return SpeechWithStreamingResponse(self._audio.speech)


class AsyncAudioWithStreamingResponse:
    def __init__(self, audio: AsyncAudio) -> None:
        self._audio = audio

    @cached_property
    def transcriptions(self) -> AsyncTranscriptionsWithStreamingResponse:
        return AsyncTranscriptionsWithStreamingResponse(self._audio.transcriptions)

    @cached_property
    def speech(self) -> AsyncSpeechWithStreamingResponse:
        return AsyncSpeechWithStreamingResponse(self._audio.speech)
