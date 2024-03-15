from __future__ import annotations

import os
import asyncio
import logging
from typing import TYPE_CHECKING, Iterator, AsyncIterator

import pytest

from jarvisbot import JarvisBot, AsyncJarvisBot

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

pytest.register_assert_rewrite("tests.utils")

logging.getLogger("jarvisbot").setLevel(logging.DEBUG)


app_token = "you app token"


@pytest.fixture(scope="session")
def client(request: FixtureRequest) -> Iterator[JarvisBot]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    with JarvisBot(app_token=app_token, _strict_response_validation=strict) as client:
        yield client


@pytest.fixture(scope="session")
async def async_client(request: FixtureRequest) -> AsyncIterator[AsyncJarvisBot]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    async with AsyncJarvisBot(app_token=app_token, _strict_response_validation=strict) as client:
        yield client
