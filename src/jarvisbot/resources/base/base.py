#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 15:36
# @Author  : dell
# @File    : base.py

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..chat import (
    Chat,
    AsyncChat,
)
from ..images import Images, AsyncImages
from ..audio import Audio, AsyncAudio

__all__ = ["Base", "AsyncBase"]


class Base(SyncAPIResource):
    @cached_property
    def chat(self) -> Chat:
        return Chat(self._client)

    @cached_property
    def images(self) -> Images:
        return Images(self._client)

    @cached_property
    def audio(self) -> Audio:
        return Audio(self._client)


class AsyncBase(AsyncAPIResource):
    @cached_property
    def chat(self) -> AsyncChat:
        return AsyncChat(self._client)

    @cached_property
    def images(self) -> AsyncImages:
        return AsyncImages(self._client)

    @cached_property
    def audio(self) -> AsyncAudio:
        return AsyncAudio(self._client)


