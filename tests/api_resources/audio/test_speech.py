from __future__ import annotations

import pytest

import jarvisbot._legacy_response as _legacy_response
from jarvisbot import JarvisBot, AsyncJarvisBot


class TestSpeech:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: JarvisBot) -> None:
        speech = client.base.audio.speech.create(
            text="string",
        )
        assert isinstance(speech, _legacy_response.HttpxBinaryResponseContent)

    @parametrize
    def test_method_create_with_all_params(self, client: JarvisBot) -> None:
        speech = client.base.audio.speech.create(
            text="string",
            model="string",
            speaker_id="string",
            response_format="mp3",
            speed=0.25,
        )
        assert isinstance(speech, _legacy_response.HttpxBinaryResponseContent)


class TestAsyncSpeech:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncJarvisBot) -> None:
        speech = await async_client.base.audio.speech.create(
            text="string",
        )
        assert isinstance(speech, _legacy_response.HttpxBinaryResponseContent)

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJarvisBot) -> None:
        speech = await async_client.base.audio.speech.create(
            text="string",
            model="string",
            speaker_id="string",
            response_format="mp3",
            speed=0.25,
        )
        assert isinstance(speech, _legacy_response.HttpxBinaryResponseContent)
