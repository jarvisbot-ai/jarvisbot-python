from __future__ import annotations

import os
from typing import Any, Union, Mapping
from urllib.parse import urljoin
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    is_mapping,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import JarvisBotError, APIStatusError, TokenValidationError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .types.token import CheckResponse, Urls
from ._constants import TOKEN_CHECK_PATH, DEFAULT_BASE_URL

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "JarvisBot",
    "AsyncJarvisBot",
    "Client",
    "AsyncClient",
]


class JarvisBot(SyncAPIClient):
    base: resources.Base
    with_raw_response: JarvisBotWithRawResponse
    with_streaming_response: JarvisBotWithStreamedResponse

    # client options
    app_token: str
    organization: str | None

    def __init__(
            self,
            *,
            app_token: str | None = None,
            organization: str | None = None,
            base_url: str | httpx.URL | None = None,
            timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
            max_retries: int = DEFAULT_MAX_RETRIES,
            default_headers: Mapping[str, str] | None = None,
            default_query: Mapping[str, object] | None = None,
            # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
            http_client: httpx.Client | None = None,
            # Enable or disable schema validation for data returned by the API.
            # When enabled an error APIResponseValidationError is raised
            # if the API responds with invalid data for the expected schema.
            #
            # This parameter may be removed or changed in the future.
            # If you rely on this feature, please open a GitHub issue
            # outlining your use-case to help us decide if it should be
            # part of our public interface in the future.
            _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous JarvisBot client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `app_token` from `JARVISBOT_APP_TOKEN`
        - `organization` from `JARVISBOT_ORG_ID`
        """
        if app_token is None:
            app_token = os.environ.get("JARVISBOT_APP_TOKEN")
        if app_token is None:
            raise JarvisBotError(
                "The app_token client option must be set either by passing app_token to the client or by setting the JARVISBOT_APP_TOKEN environment variable"
            )
        self.app_token = app_token

        if organization is None:
            organization = os.environ.get("JARVISBOT_ORG_ID")
        self.organization = organization

        if base_url is None:
            base_url = os.environ.get("JARVISBOT_BASE_URL")
        if base_url is None:
            base_url = DEFAULT_BASE_URL

        urls_json = {
            "url_chat": "",
            "url_asr": "",
            "url_tts": "",
            "url_txt2img": "",
            "url_img2img": ""
        }
        self.urls = Urls(**urls_json)

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream
        self.base = resources.Base(self)
        self.with_raw_response = JarvisBotWithRawResponse(self)
        self.with_streaming_response = JarvisBotWithStreamedResponse(self)
        self.check()

    def check(self) -> None:
        if self.app_token is None:
            raise TokenValidationError("Token is None")
        check_result = self.get(
            urljoin(TOKEN_CHECK_PATH, self.app_token),
            cast_to=CheckResponse,
        )
        if check_result.code != 0:
            raise TokenValidationError(f"Token is not valid: response message: {check_result.msg}")
        else:
            if check_result.data is not None:
                self.urls = check_result.data

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        app_token = self.app_token
        return {"App-token": f"{app_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "JarvisBot-Organization": self.organization if self.organization is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
            self,
            *,
            app_token: str | None = None,
            organization: str | None = None,
            base_url: str | httpx.URL | None = None,
            timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
            http_client: httpx.Client | None = None,
            max_retries: int | NotGiven = NOT_GIVEN,
            default_headers: Mapping[str, str] | None = None,
            set_default_headers: Mapping[str, str] | None = None,
            default_query: Mapping[str, object] | None = None,
            set_default_query: Mapping[str, object] | None = None,
            _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            app_token=app_token or self.app_token,
            organization=organization or self.organization,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
            self,
            err_msg: str,
            *,
            body: object,
            response: httpx.Response,
    ) -> APIStatusError:
        data = body.get("error", body) if is_mapping(body) else body
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=data)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=data)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=data)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=data)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=data)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=data)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=data)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=data)
        return APIStatusError(err_msg, response=response, body=data)


class AsyncJarvisBot(AsyncAPIClient):
    # chat: resources.AsyncChat
    # images: resources.AsyncImages
    # audio: resources.AsyncAudio
    base: resources.AsyncBase
    with_raw_response: AsyncJarvisBotWithRawResponse
    with_streaming_response: AsyncJarvisBotWithStreamedResponse

    # client options
    app_token: str
    organization: str | None

    def __init__(
            self,
            *,
            app_token: str | None = None,
            organization: str | None = None,
            base_url: str | httpx.URL | None = None,
            timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
            max_retries: int = DEFAULT_MAX_RETRIES,
            default_headers: Mapping[str, str] | None = None,
            default_query: Mapping[str, object] | None = None,
            # Configure a custom httpx client. See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
            http_client: httpx.AsyncClient | None = None,
            # Enable or disable schema validation for data returned by the API.
            # When enabled an error APIResponseValidationError is raised
            # if the API responds with invalid data for the expected schema.
            #
            # This parameter may be removed or changed in the future.
            # If you rely on this feature, please open a GitHub issue
            # outlining your use-case to help us decide if it should be
            # part of our public interface in the future.
            _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async JarvisBot client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `app_token` from `JARVISBOT_APP_TOKEN`
        - `organization` from `JARVISBOT_ORG_ID`
        """
        if app_token is None:
            app_token = os.environ.get("JARVISBOT_APP_TOKEN")
        if app_token is None:
            raise JarvisBotError(
                "The app_token client option must be set either by passing app_token to the client or by setting the JARVISBOT_APP_TOKEN environment variable"
            )
        self.app_token = app_token

        if organization is None:
            organization = os.environ.get("JARVISBOT_ORG_ID")
        self.organization = organization

        if base_url is None:
            base_url = os.environ.get("JARVISBOT_BASE_URL")
        if base_url is None:
            base_url = DEFAULT_BASE_URL

        urls_json = {
            "url_chat": "",
            "url_asr": "",
            "url_tts": "",
            "url_txt2img": "",
            "url_img2img": ""
        }
        self.urls = Urls(**urls_json)

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream
        self.base = resources.AsyncBase(self)
        self.with_raw_response = AsyncJarvisBotWithRawResponse(self)
        self.with_streaming_response = AsyncJarvisBotWithStreamedResponse(self)
        self.check(base_url, max_retries, timeout, __version__, _strict_response_validation)

    def check(self,
              base_url: str | httpx.URL,
              max_retries: int,
              timeout: Union[float, Timeout, None, NotGiven],
              version: str,
              _strict_response_validation: bool
              ) -> None:
        if self.app_token is None:
            raise TokenValidationError("Token is None")
        client = SyncAPIClient(base_url=base_url, max_retries=max_retries, timeout=timeout, version=version,
                               _strict_response_validation=_strict_response_validation
                               )
        check_result = client.get(
            urljoin(TOKEN_CHECK_PATH, self.app_token),
            cast_to=CheckResponse,
        )
        if check_result.code != 0:
            raise TokenValidationError(f"Token is not valid: response message: {check_result.msg}")
        else:
            if check_result.data is not None:
                self.urls = check_result.data

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        app_token = self.app_token
        return {"App-token": f"{app_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "JarvisBot-Organization": self.organization if self.organization is not None else Omit(),
            **self._custom_headers,
        }

    def copy(
            self,
            *,
            app_token: str | None = None,
            organization: str | None = None,
            base_url: str | httpx.URL | None = None,
            timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
            http_client: httpx.AsyncClient | None = None,
            max_retries: int | NotGiven = NOT_GIVEN,
            default_headers: Mapping[str, str] | None = None,
            set_default_headers: Mapping[str, str] | None = None,
            default_query: Mapping[str, object] | None = None,
            set_default_query: Mapping[str, object] | None = None,
            _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            app_token=app_token or self.app_token,
            organization=organization or self.organization,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
            self,
            err_msg: str,
            *,
            body: object,
            response: httpx.Response,
    ) -> APIStatusError:
        data = body.get("error", body) if is_mapping(body) else body
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=data)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=data)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=data)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=data)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=data)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=data)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=data)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=data)
        return APIStatusError(err_msg, response=response, body=data)


class JarvisBotWithRawResponse:
    def __init__(self, client: JarvisBot) -> None:
        self.chat = resources.ChatWithRawResponse(client.base.chat)
        self.images = resources.ImagesWithRawResponse(client.base.images)
        self.audio = resources.AudioWithRawResponse(client.base.audio)


class AsyncJarvisBotWithRawResponse:
    def __init__(self, client: AsyncJarvisBot) -> None:
        self.chat = resources.AsyncChatWithRawResponse(client.base.chat)
        self.images = resources.AsyncImagesWithRawResponse(client.base.images)
        self.audio = resources.AsyncAudioWithRawResponse(client.base.audio)


class JarvisBotWithStreamedResponse:
    def __init__(self, client: JarvisBot) -> None:
        self.chat = resources.ChatWithStreamingResponse(client.base.chat)
        self.images = resources.ImagesWithStreamingResponse(client.base.images)
        self.audio = resources.AudioWithStreamingResponse(client.base.audio)


class AsyncJarvisBotWithStreamedResponse:
    def __init__(self, client: AsyncJarvisBot) -> None:
        self.chat = resources.AsyncChatWithStreamingResponse(client.base.chat)
        self.images = resources.AsyncImagesWithStreamingResponse(client.base.images)
        self.audio = resources.AsyncAudioWithStreamingResponse(client.base.audio)


Client = JarvisBot

AsyncClient = AsyncJarvisBot
