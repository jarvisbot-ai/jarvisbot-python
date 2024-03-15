from __future__ import annotations

import pytest

from jarvisbot import JarvisBot, AsyncJarvisBot
from jarvisbot.types.audio import Transcription
from tests.utils import assert_matches_type


class TestTranscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: JarvisBot) -> None:
        transcription = client.base.audio.transcriptions.create(
            files=b"raw file contents",
            input_format="mp3"
        )
        assert_matches_type(Transcription, transcription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: JarvisBot) -> None:
        transcription = client.base.audio.transcriptions.create(
            files=b"raw file contents",
            request_id="string",
            lang="en",
            input_format="mp3",
            response_format="json",
            temperature=0,
            temperature_inc=0.2,
        )
        assert_matches_type(Transcription, transcription, path=["response"])


class TestAsyncTranscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJarvisBot) -> None:
        transcription = await async_client.base.audio.transcriptions.create(
            files=b"raw file contents",
            input_format="mp3"
        )
        assert_matches_type(Transcription, transcription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJarvisBot) -> None:
        transcription = await async_client.base.audio.transcriptions.create(
            files=b"raw file contents",
            request_id="string",
            lang="en",
            input_format="mp3",
            response_format="json",
            temperature=0,
            temperature_inc=0.2,
        )
        assert_matches_type(Transcription, transcription, path=["response"])
