from __future__ import annotations

from typing import Union, Dict
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_streamed_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...types.audio import speech_create_params
from ..._base_client import (
    make_request_options,
)

__all__ = [
    "Speech",
    "AsyncSpeech",
    "SpeechWithRawResponse",
    "AsyncSpeechWithRawResponse",
    "SpeechWithStreamingResponse",
    "AsyncSpeechWithStreamingResponse"
]


class Speech(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpeechWithRawResponse:
        return SpeechWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeechWithStreamingResponse:
        return SpeechWithStreamingResponse(self)

    def create(
            self,
            *,
            text: str,
            model: str | NotGiven = NOT_GIVEN,
            speaker_id: str | NotGiven = NOT_GIVEN,
            response_format: str | NotGiven = NOT_GIVEN,
            speed: float | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> _legacy_response.HttpxBinaryResponseContent:
        """
        Generates audio from the input text.

        Args:
          text: The text to generate audio for. The maximum length is 4096 characters.

          model:TTS model

          speaker_id:

          response_format:

          speed: The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is
              the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            self._client.urls.url_tts,
            body=maybe_transform(
                {
                    "text": text,
                    "model": model,
                    "speaker_id": speaker_id,
                    "response_format": response_format,
                    "speed": speed
                },
                speech_create_params.SpeechCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=_legacy_response.HttpxBinaryResponseContent,
        )


class AsyncSpeech(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpeechWithRawResponse:
        return AsyncSpeechWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeechWithStreamingResponse:
        return AsyncSpeechWithStreamingResponse(self)

    async def create(
            self,
            *,
            text: str,
            model: str | NotGiven = NOT_GIVEN,
            speaker_id: str | NotGiven = NOT_GIVEN,
            response_format: str | NotGiven = NOT_GIVEN,
            speed: float | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> _legacy_response.HttpxBinaryResponseContent:
        """
        Generates audio from the input text.

        Args:
          text: The text to generate audio for. The maximum length is 4096 characters.

          model:tts model

          speaker_id:

          response_format:

          speed: The speed of the generated audio. Select a value from `0.25` to `4.0`. `1.0` is
              the default.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            self._client.urls.url_tts,
            body=maybe_transform(
                {
                    "text": text,
                    "model": model,
                    "speaker_id": speaker_id,
                    "response_format": response_format,
                    "speed": speed
                },
                speech_create_params.SpeechCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=_legacy_response.HttpxBinaryResponseContent,
        )


class SpeechWithRawResponse:
    def __init__(self, speech: Speech) -> None:
        self._speech = speech

        self.create = _legacy_response.to_raw_response_wrapper(
            speech.create,
        )


class AsyncSpeechWithRawResponse:
    def __init__(self, speech: AsyncSpeech) -> None:
        self._speech = speech

        self.create = _legacy_response.async_to_raw_response_wrapper(
            speech.create,
        )


class SpeechWithStreamingResponse:
    def __init__(self, speech: Speech) -> None:
        self._speech = speech

        self.create = to_custom_streamed_response_wrapper(
            speech.create,
            StreamedBinaryAPIResponse,
        )


class AsyncSpeechWithStreamingResponse:
    def __init__(self, speech: AsyncSpeech) -> None:
        self._speech = speech

        self.create = async_to_custom_streamed_response_wrapper(
            speech.create,
            AsyncStreamedBinaryAPIResponse,
        )
