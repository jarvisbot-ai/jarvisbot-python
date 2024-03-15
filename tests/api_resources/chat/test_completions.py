from __future__ import annotations

import pytest

from jarvisbot import JarvisBot, AsyncJarvisBot
from jarvisbot.types.chat import ChatCompletion
from tests.utils import assert_matches_type


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: JarvisBot) -> None:
        completion = client.base.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: JarvisBot) -> None:
        completion = client.base.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "description": "string",
                    "name": "string",
                    "parameters": {"foo": "bar"},
                }
            ],
            logit_bias={"foo": 0},
            max_tokens=0,
            n=1,
            presence_penalty=-2,
            response_format={"type": "json_object"},
            seed=-9223372036854776000,
            stop="string",
            stream=False,
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
            ],
            top_p=1,
            user="user-1234",
            min_p=0.05,
            top_k=40,
            repeat_penalty=1.1,
            logit_bias_type="input_ids",
            mirostat_mode=0,
            mirostat_tau=0.1,
            mirostat_eta=0.1,
            grammar=""
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    def test_method_create_overload_2(self, client: JarvisBot) -> None:
        completion_stream = client.base.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            stream=True,
        )
        completion_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: JarvisBot) -> None:
        completion_stream = client.base.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "description": "string",
                    "name": "string",
                    "parameters": {"foo": "bar"},
                }
            ],
            logit_bias={"foo": 0},
            max_tokens=0,
            n=1,
            presence_penalty=-2,
            response_format={"type": "json_object"},
            seed=-9223372036854776000,
            stop="string",
            stream=True,
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
            ],
            top_p=1,
            user="user-1234",
            min_p=0.05,
            top_k=40,
            repeat_penalty=1.1,
            logit_bias_type="input_ids",
            mirostat_mode=0,
            mirostat_tau=0.1,
            mirostat_eta=0.1,
            grammar=""
        )
        completion_stream.response.close()


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncJarvisBot) -> None:
        completion = await async_client.base.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ]
        )
        assert_matches_type(ChatCompletion, completion, path=["response"])

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncJarvisBot) -> None:
        completion_stream = await async_client.base.chat.completions.create(
            messages=[
                {
                    "content": "string",
                    "role": "system",
                }
            ],
            model="string",
            frequency_penalty=-2,
            function_call="none",
            functions=[
                {
                    "description": "string",
                    "name": "string",
                    "parameters": {"foo": "bar"},
                }
            ],
            logit_bias={"foo": 0},
            max_tokens=0,
            n=1,
            presence_penalty=-2,
            response_format={"type": "json_object"},
            seed=-9223372036854776000,
            stop="string",
            stream=True,
            temperature=1,
            tool_choice="none",
            tools=[
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
                {
                    "type": "function",
                    "function": {
                        "description": "string",
                        "name": "string",
                        "parameters": {"foo": "bar"},
                    },
                },
            ],
            top_p=1,
            user="user-1234",
            min_p=0.05,
            top_k=40,
            repeat_penalty=1.1,
            logit_bias_type="input_ids",
            mirostat_mode=0,
            mirostat_tau=0.1,
            mirostat_eta=0.1,
            grammar=""
        )
        await completion_stream.response.aclose()

