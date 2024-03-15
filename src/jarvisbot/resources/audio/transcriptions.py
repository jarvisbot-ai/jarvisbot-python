from __future__ import annotations

import io
import os
from typing import List, Union, Mapping, cast, Dict, IO
from typing_extensions import Literal
import base64

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven, FileTypes, FileContent, PathLike
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, file_to_base64
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...types.audio import Transcription, transcription_create_params
from ..._base_client import (
    make_request_options,
)

__all__ = [
    "Transcriptions",
    "AsyncTranscriptions",
    "TranscriptionsWithRawResponse",
    "AsyncTranscriptionsWithRawResponse",
    "TranscriptionsWithStreamingResponse",
    "AsyncTranscriptionsWithStreamingResponse"
]


class Transcriptions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TranscriptionsWithRawResponse:
        return TranscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TranscriptionsWithStreamingResponse:
        return TranscriptionsWithStreamingResponse(self)

    def create(
            self,
            *,
            files: FileContent,
            lang: str | NotGiven = NOT_GIVEN,
            input_format: str,
            request_id: str | NotGiven = NOT_GIVEN,
            response_format: Literal["json", "verbose_json"] | NotGiven = NOT_GIVEN,
            temperature: float | NotGiven = NOT_GIVEN,
            temperature_inc: float | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Transcription:
        """
        Transcribes audio into the input language.

        Args:
          file:
              The audio file object (not file name) to transcribe, in one of these formats:
              flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

          lang: The language of the input audio. Supplying the input language in
              [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will
              improve accuracy and latency.

          input_format: The format of the input audio file.

          request_id: The id of the request.

          response_format: The format of the transcript output, in one of these options: `json` or `verbose_json`.

          temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the
              output more random, while lower values like 0.2 will make it more focused and
              deterministic. If set to 0, the model will use
              [log probability](https://en.wikipedia.org/wiki/Log_probability) to
              automatically increase the temperature until certain thresholds are hit.

          temperature_inc:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        b64_file = file_to_base64(files)
        body = deepcopy_minimal(
            {
                "files": b64_file,
                "lang": lang,
                "input_format": input_format,
                "request_id": request_id,
                "response_format": response_format,
                "temperature": temperature,
                "temperature_inc": temperature_inc,
            }
        )
        return self._post(
            self._client.urls.url_asr,
            body=maybe_transform(body, transcription_create_params.TranscriptionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transcription,
        )


class AsyncTranscriptions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTranscriptionsWithRawResponse:
        return AsyncTranscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTranscriptionsWithStreamingResponse:
        return AsyncTranscriptionsWithStreamingResponse(self)

    async def create(
            self,
            *,
            files: FileContent,
            lang: str | NotGiven = NOT_GIVEN,
            input_format: str,
            request_id: str | NotGiven = NOT_GIVEN,
            response_format: Literal["json", "verbose_json"] | NotGiven = NOT_GIVEN,
            temperature: float | NotGiven = NOT_GIVEN,
            temperature_inc: float | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Transcription:
        """
        Transcribes audio into the input language.

        Args:
          files:
              The audio file object (not file name) to transcribe, in one of these formats:
              flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

          lang: The language of the input audio. Supplying the input language in
              [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will
              improve accuracy and latency.

          input_format: The format of the input audio file.

          request_id: The id of the request.

          response_format: The format of the transcript output, in one of these options: `json` or `verbose_json`.

          temperature: The sampling temperature, between 0 and 1. Higher values like 0.8 will make the
              output more random, while lower values like 0.2 will make it more focused and
              deterministic. If set to 0, the model will use
              [log probability](https://en.wikipedia.org/wiki/Log_probability) to
              automatically increase the temperature until certain thresholds are hit.

          temperature_inc:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        b64_file = file_to_base64(files)
        body = deepcopy_minimal(
            {
                "files": b64_file,
                "lang": lang,
                "input_format": input_format,
                "request_id": request_id,
                "response_format": response_format,
                "temperature": temperature,
                "temperature_inc": temperature_inc,
            }
        )
        return await self._post(
            self._client.urls.url_asr,
            body=maybe_transform(body, transcription_create_params.TranscriptionCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transcription,
        )


class TranscriptionsWithRawResponse:
    def __init__(self, transcriptions: Transcriptions) -> None:
        self._transcriptions = transcriptions

        self.create = _legacy_response.to_raw_response_wrapper(
            transcriptions.create,
        )


class AsyncTranscriptionsWithRawResponse:
    def __init__(self, transcriptions: AsyncTranscriptions) -> None:
        self._transcriptions = transcriptions

        self.create = _legacy_response.async_to_raw_response_wrapper(
            transcriptions.create,
        )


class TranscriptionsWithStreamingResponse:
    def __init__(self, transcriptions: Transcriptions) -> None:
        self._transcriptions = transcriptions

        self.create = to_streamed_response_wrapper(
            transcriptions.create,
        )


class AsyncTranscriptionsWithStreamingResponse:
    def __init__(self, transcriptions: AsyncTranscriptions) -> None:
        self._transcriptions = transcriptions

        self.create = async_to_streamed_response_wrapper(
            transcriptions.create,
        )
