# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional, overload
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    async_to_raw_response_wrapper
)
from ..._streaming import Stream, AsyncStream
from ...types.chat import (
    ChatCompletion,
    ChatCompletionChunk,
    ChatCompletionToolParam,
    ChatCompletionMessageParam,
    ChatCompletionToolChoiceOptionParam,
    completion_create_params,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Completions", "AsyncCompletions"]


class Completions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionsWithRawResponse:
        return CompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionsWithStreamingResponse:
        return CompletionsWithStreamingResponse(self)

    @overload
    def create(
            self,
            *,
            messages: Iterable[ChatCompletionMessageParam],
            functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
            function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
            tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
            tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
            stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            top_k: Optional[float] | NotGiven = NOT_GIVEN,
            repeat_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias_type: Optional[str] | NotGiven = NOT_GIVEN,
            mirostat_mode: Optional[int] | NotGiven = NOT_GIVEN,
            mirostat_tau: Optional[float] | NotGiven = NOT_GIVEN,
            mirostat_eta: Optional[float] | NotGiven = NOT_GIVEN,
            grammar: Optional[str] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """
        Creates a model response for the given chat conversation.

        Args:
          messages: A list of messages comprising the conversation so far.

          functions: Deprecated in favor of `tools`.

            A list of functions the model may generate JSON inputs for.

          model: ID of the model to use. See the
              table for details on which models work with the Chat API.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via `{"name": "my_function"}` forces the model to call that
              function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.



          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion.

              The total length of input tokens and generated tokens is limited by the model's
              context length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output. Compatible with
              Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

          tool_choice: Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help JarvisBot to monitor
              and detect abuse.

          min_p: Sets a minimum base probability threshold for token selection.
              The Min-P sampling method was designed as an alternative to Top-P, and aims to ensure
               a balance of quality and variety. The parameter min_p represents the minimum probability
               for a token to be considered, relative to the probability of the most likely token.
               For example, with min_p=0.05 and the most likely token having a probability of 0.9,
               logits with a value less than 0.045 are filtered out.

          top_k: Limit the next token selection to the K most probable tokens.

          repeat_penalty: A penalty applied to each token that is already generated. This helps prevent the model
             from repeating itself.

          logit_bias_type:

          mirostat_mode: Enable Mirostat constant-perplexity algorithm of the specified version (1 or 2; 0 = disabled)

          mirostat_tau: Mirostat target entropy, i.e. the target perplexity - lower values produce focused and
                coherent text, larger values produce more diverse and less coherent text

          mirostat_eta: Mirostat learning rate

          grammar:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
            self,
            *,
            messages: Iterable[ChatCompletionMessageParam],
            functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
            function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
            tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
            tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
            stream: Literal[True],
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            top_k: Optional[float] | NotGiven = NOT_GIVEN,
            repeat_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias_type: Optional[str] | NotGiven = NOT_GIVEN,
            mirostat_mode: Optional[int] | NotGiven = NOT_GIVEN,
            mirostat_tau: Optional[float] | NotGiven = NOT_GIVEN,
            mirostat_eta: Optional[float] | NotGiven = NOT_GIVEN,
            grammar: Optional[str] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[ChatCompletionChunk]:
        """
        Creates a model response for the given chat conversation.

        Args:
          messages: A list of messages comprising the conversation so far.

          model: ID of the model to use. See the
              table for details on which models work with the Chat API.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via `{"name": "my_function"}` forces the model to call that
              function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`. This option is currently not available on the `gpt-4-vision-preview`
              model.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion.

              The total length of input tokens and generated tokens is limited by the model's
              context length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

          tool_choice: Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for.

          top_logprobs: An integer between 0 and 5 specifying the number of most likely tokens to return
              at each token position, each with an associated log probability. `logprobs` must
              be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help JarvisBot to monitor
              and detect abuse.

          min_p: Sets a minimum base probability threshold for token selection.
              The Min-P sampling method was designed as an alternative to Top-P, and aims to ensure
               a balance of quality and variety. The parameter min_p represents the minimum probability
               for a token to be considered, relative to the probability of the most likely token.
               For example, with min_p=0.05 and the most likely token having a probability of 0.9,
               logits with a value less than 0.045 are filtered out.

          top_k: Limit the next token selection to the K most probable tokens.

          repeat_penalty: A penalty applied to each token that is already generated. This helps prevent the model
             from repeating itself.

          logit_bias_type:

          mirostat_mode: Enable Mirostat constant-perplexity algorithm of the specified version (1 or 2; 0 = disabled)

          mirostat_tau: Mirostat target entropy, i.e. the target perplexity - lower values produce focused and
                coherent text, larger values produce more diverse and less coherent text

          mirostat_eta: Mirostat learning rate

          grammar:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
            self,
            *,
            messages: Iterable[ChatCompletionMessageParam],
            functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
            function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
            tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
            tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
            stream: bool,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            top_k: Optional[float] | NotGiven = NOT_GIVEN,
            repeat_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias_type: Optional[str] | NotGiven = NOT_GIVEN,
            mirostat_mode: Optional[int] | NotGiven = NOT_GIVEN,
            mirostat_tau: Optional[float] | NotGiven = NOT_GIVEN,
            mirostat_eta: Optional[float] | NotGiven = NOT_GIVEN,
            grammar: Optional[str] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        """
        Creates a model response for the given chat conversation.

        Args:
          messages: A list of messages comprising the conversation so far.

          model: ID of the model to use. See the
              table for details on which models work with the Chat API.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via `{"name": "my_function"}` forces the model to call that
              function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`. This option is currently not available on the `gpt-4-vision-preview`
              model.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion.

              The total length of input tokens and generated tokens is limited by the model's
              context length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

          tool_choice: Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for.

          top_logprobs: An integer between 0 and 5 specifying the number of most likely tokens to return
              at each token position, each with an associated log probability. `logprobs` must
              be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help JarvisBot to monitor
              and detect abuse.

          min_p: Sets a minimum base probability threshold for token selection.
              The Min-P sampling method was designed as an alternative to Top-P, and aims to ensure
               a balance of quality and variety. The parameter min_p represents the minimum probability
               for a token to be considered, relative to the probability of the most likely token.
               For example, with min_p=0.05 and the most likely token having a probability of 0.9,
               logits with a value less than 0.045 are filtered out.

          top_k: Limit the next token selection to the K most probable tokens.

          repeat_penalty: A penalty applied to each token that is already generated. This helps prevent the model
             from repeating itself.

          logit_bias_type:

          mirostat_mode: Enable Mirostat constant-perplexity algorithm of the specified version (1 or 2; 0 = disabled)

          mirostat_tau: Mirostat target entropy, i.e. the target perplexity - lower values produce focused and
                coherent text, larger values produce more diverse and less coherent text

          mirostat_eta: Mirostat learning rate

          grammar:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages"], ["messages", "stream"])
    def create(
            self,
            *,
            messages: Iterable[ChatCompletionMessageParam],
            functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
            function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
            tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
            tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
            stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            top_k: Optional[float] | NotGiven = NOT_GIVEN,
            repeat_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias_type: Optional[str] | NotGiven = NOT_GIVEN,
            mirostat_mode: Optional[int] | NotGiven = NOT_GIVEN,
            mirostat_tau: Optional[float] | NotGiven = NOT_GIVEN,
            mirostat_eta: Optional[float] | NotGiven = NOT_GIVEN,
            grammar: Optional[str] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | Stream[ChatCompletionChunk]:
        return self._post(
            self._client.urls.url_chat,
            body=maybe_transform(
                {
                    "messages": messages,
                    "functions": functions,
                    "function_call": function_call,
                    "tools": tools,
                    "tool_choice": tool_choice,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "top_p": top_p,
                    "min_p": min_p,
                    "stop": stop,
                    "stream": stream,
                    "presence_penalty": presence_penalty,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "seed": seed,
                    "response_format": response_format,
                    "model": model,
                    "n": n,
                    "user": user,
                    "top_k": top_k,
                    "repeat_penalty": repeat_penalty,
                    "logit_bias_type": logit_bias_type,
                    "mirostat_mode": mirostat_mode,
                    "mirostat_tau": mirostat_tau,
                    "mirostat_eta": mirostat_eta,
                    "grammar": grammar
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=Stream[ChatCompletionChunk],
        )


class AsyncCompletions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionsWithRawResponse:
        return AsyncCompletionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionsWithStreamingResponse:
        return AsyncCompletionsWithStreamingResponse(self)

    @overload
    async def create(
            self,
            *,
            messages: Iterable[ChatCompletionMessageParam],
            functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
            function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
            tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
            tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
            stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            top_k: Optional[float] | NotGiven = NOT_GIVEN,
            repeat_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias_type: Optional[str] | NotGiven = NOT_GIVEN,
            mirostat_mode: Optional[int] | NotGiven = NOT_GIVEN,
            mirostat_tau: Optional[float] | NotGiven = NOT_GIVEN,
            mirostat_eta: Optional[float] | NotGiven = NOT_GIVEN,
            grammar: Optional[str] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion:
        """
        Creates a model response for the given chat conversation.

        Args:

          messages: A list of messages comprising the conversation so far.

          functions: Deprecated in favor of `tools`.

            A list of functions the model may generate JSON inputs for.

          model: ID of the model to use. See the
              table for details on which models work with the Chat API.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via `{"name": "my_function"}` forces the model to call that
              function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.



          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion.

              The total length of input tokens and generated tokens is limited by the model's
              context length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output. Compatible with
              Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

          tool_choice: Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help JarvisBot to monitor
              and detect abuse.

          min_p: Sets a minimum base probability threshold for token selection.
              The Min-P sampling method was designed as an alternative to Top-P, and aims to ensure
               a balance of quality and variety. The parameter min_p represents the minimum probability
               for a token to be considered, relative to the probability of the most likely token.
               For example, with min_p=0.05 and the most likely token having a probability of 0.9,
               logits with a value less than 0.045 are filtered out.

          top_k: Limit the next token selection to the K most probable tokens.

          repeat_penalty: A penalty applied to each token that is already generated. This helps prevent the model
             from repeating itself.

          logit_bias_type:

          mirostat_mode: Enable Mirostat constant-perplexity algorithm of the specified version (1 or 2; 0 = disabled)

          mirostat_tau: Mirostat target entropy, i.e. the target perplexity - lower values produce focused and
                coherent text, larger values produce more diverse and less coherent text

          mirostat_eta: Mirostat learning rate

          grammar:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
            self,
            *,
            messages: Iterable[ChatCompletionMessageParam],
            functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
            function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
            tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
            tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
            stream: Literal[True],
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            top_k: Optional[float] | NotGiven = NOT_GIVEN,
            repeat_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias_type: Optional[str] | NotGiven = NOT_GIVEN,
            mirostat_mode: Optional[int] | NotGiven = NOT_GIVEN,
            mirostat_tau: Optional[float] | NotGiven = NOT_GIVEN,
            mirostat_eta: Optional[float] | NotGiven = NOT_GIVEN,
            grammar: Optional[str] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[ChatCompletionChunk]:
        """
        Creates a model response for the given chat conversation.

        Args:
          messages: A list of messages comprising the conversation so far.

          model: ID of the model to use. See the
              table for details on which models work with the Chat API.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via `{"name": "my_function"}` forces the model to call that
              function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`. This option is currently not available on the `gpt-4-vision-preview`
              model.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion.

              The total length of input tokens and generated tokens is limited by the model's
              context length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

          tool_choice: Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for.

          top_logprobs: An integer between 0 and 5 specifying the number of most likely tokens to return
              at each token position, each with an associated log probability. `logprobs` must
              be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help JarvisBot to monitor
              and detect abuse.

          min_p: Sets a minimum base probability threshold for token selection.
              The Min-P sampling method was designed as an alternative to Top-P, and aims to ensure
               a balance of quality and variety. The parameter min_p represents the minimum probability
               for a token to be considered, relative to the probability of the most likely token.
               For example, with min_p=0.05 and the most likely token having a probability of 0.9,
               logits with a value less than 0.045 are filtered out.

          top_k: Limit the next token selection to the K most probable tokens.

          repeat_penalty: A penalty applied to each token that is already generated. This helps prevent the model
             from repeating itself.

          logit_bias_type:

          mirostat_mode: Enable Mirostat constant-perplexity algorithm of the specified version (1 or 2; 0 = disabled)

          mirostat_tau: Mirostat target entropy, i.e. the target perplexity - lower values produce focused and
                coherent text, larger values produce more diverse and less coherent text

          mirostat_eta: Mirostat learning rate

          grammar:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
            self,
            *,
            messages: Iterable[ChatCompletionMessageParam],
            functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
            function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
            tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
            tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
            stream: bool,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            top_k: Optional[float] | NotGiven = NOT_GIVEN,
            repeat_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias_type: Optional[str] | NotGiven = NOT_GIVEN,
            mirostat_mode: Optional[int] | NotGiven = NOT_GIVEN,
            mirostat_tau: Optional[float] | NotGiven = NOT_GIVEN,
            mirostat_eta: Optional[float] | NotGiven = NOT_GIVEN,
            grammar: Optional[str] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        """
        Creates a model response for the given chat conversation.

        Args:
          messages: A list of messages comprising the conversation so far.

          model: ID of the model to use. See the
              table for details on which models work with the Chat API.

          stream: If set, partial message deltas will be sent, like in ChatGPT. Tokens will be
              sent as data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          function_call: Deprecated in favor of `tool_choice`.

              Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via `{"name": "my_function"}` forces the model to call that
              function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          functions: Deprecated in favor of `tools`.

              A list of functions the model may generate JSON inputs for.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the
              tokenizer) to an associated bias value from -100 to 100. Mathematically, the
              bias is added to the logits generated by the model prior to sampling. The exact
              effect will vary per model, but values between -1 and 1 should decrease or
              increase likelihood of selection; values like -100 or 100 should result in a ban
              or exclusive selection of the relevant token.

          logprobs: Whether to return log probabilities of the output tokens or not. If true,
              returns the log probabilities of each output token returned in the `content` of
              `message`. This option is currently not available on the `gpt-4-vision-preview`
              model.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the chat
              completion.

              The total length of input tokens and generated tokens is limited by the model's
              context length.

          n: How many chat completion choices to generate for each input message. Note that
              you will be charged based on the number of generated tokens across all of the
              choices. Keep `n` as `1` to minimize costs.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          response_format: An object specifying the format that the model must output.

              Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the
              message the model generates is valid JSON.

              **Important:** when using JSON mode, you **must** also instruct the model to
              produce JSON yourself via a system or user message. Without this, the model may
              generate an unending stream of whitespace until the generation reaches the token
              limit, resulting in a long-running and seemingly "stuck" request. Also note that
              the message content may be partially cut off if `finish_reason="length"`, which
              indicates the generation exceeded `max_tokens` or the conversation exceeded the
              max context length.

          seed: This feature is in Beta. If specified, our system will make a best effort to
              sample deterministically, such that repeated requests with the same `seed` and
              parameters should return the same result. Determinism is not guaranteed, and you
              should refer to the `system_fingerprint` response parameter to monitor changes
              in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

          tool_choice: Controls which (if any) function is called by the model. `none` means the model
              will not call a function and instead generates a message. `auto` means the model
              can pick between generating a message or calling a function. Specifying a
              particular function via
              `{"type": "function", "function": {"name": "my_function"}}` forces the model to
              call that function.

              `none` is the default when no functions are present. `auto` is the default if
              functions are present.

          tools: A list of tools the model may call. Currently, only functions are supported as a
              tool. Use this to provide a list of functions the model may generate JSON inputs
              for.

          top_logprobs: An integer between 0 and 5 specifying the number of most likely tokens to return
              at each token position, each with an associated log probability. `logprobs` must
              be set to `true` if this parameter is used.

          top_p: An alternative to sampling with temperature, called nucleus sampling, where the
              model considers the results of the tokens with top_p probability mass. So 0.1
              means only the tokens comprising the top 10% probability mass are considered.

              We generally recommend altering this or `temperature` but not both.

          user: A unique identifier representing your end-user, which can help JarvisBot to monitor
              and detect abuse.

          min_p: Sets a minimum base probability threshold for token selection.
              The Min-P sampling method was designed as an alternative to Top-P, and aims to ensure
               a balance of quality and variety. The parameter min_p represents the minimum probability
               for a token to be considered, relative to the probability of the most likely token.
               For example, with min_p=0.05 and the most likely token having a probability of 0.9,
               logits with a value less than 0.045 are filtered out.

          top_k: Limit the next token selection to the K most probable tokens.

          repeat_penalty: A penalty applied to each token that is already generated. This helps prevent the model
             from repeating itself.

          logit_bias_type:

          mirostat_mode: Enable Mirostat constant-perplexity algorithm of the specified version (1 or 2; 0 = disabled)

          mirostat_tau: Mirostat target entropy, i.e. the target perplexity - lower values produce focused and
                coherent text, larger values produce more diverse and less coherent text

          mirostat_eta: Mirostat learning rate

          grammar:

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["messages"], ["messages", "stream"])
    async def create(
            self,
            *,
            messages: Iterable[ChatCompletionMessageParam],
            functions: Iterable[completion_create_params.Function] | NotGiven = NOT_GIVEN,
            function_call: completion_create_params.FunctionCall | NotGiven = NOT_GIVEN,
            tools: Iterable[ChatCompletionToolParam] | NotGiven = NOT_GIVEN,
            tool_choice: ChatCompletionToolChoiceOptionParam | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str]] | NotGiven = NOT_GIVEN,
            stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            response_format: completion_create_params.ResponseFormat | NotGiven = NOT_GIVEN,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            top_k: Optional[float] | NotGiven = NOT_GIVEN,
            repeat_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias_type: Optional[str] | NotGiven = NOT_GIVEN,
            mirostat_mode: Optional[int] | NotGiven = NOT_GIVEN,
            mirostat_tau: Optional[float] | NotGiven = NOT_GIVEN,
            mirostat_eta: Optional[float] | NotGiven = NOT_GIVEN,
            grammar: Optional[str] | NotGiven = NOT_GIVEN,
            # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
            # The extra values given here take precedence over values defined on the client or passed to this method.
            extra_headers: Headers | None = None,
            extra_query: Query | None = None,
            extra_body: Body | None = None,
            timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChatCompletion | AsyncStream[ChatCompletionChunk]:
        return await self._post(
            self._client.urls.url_chat,
            body=maybe_transform(
                {
                    "messages": messages,
                    "functions": functions,
                    "function_call": function_call,
                    "tools": tools,
                    "tool_choice": tool_choice,
                    "max_tokens": max_tokens,
                    "temperature": temperature,
                    "top_p": top_p,
                    "min_p": min_p,
                    "stop": stop,
                    "stream": stream,
                    "presence_penalty": presence_penalty,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "seed": seed,
                    "response_format": response_format,
                    "model": model,
                    "n": n,
                    "user": user,
                    "top_k": top_k,
                    "repeat_penalty": repeat_penalty,
                    "logit_bias_type": logit_bias_type,
                    "mirostat_mode": mirostat_mode,
                    "mirostat_tau": mirostat_tau,
                    "mirostat_eta": mirostat_eta,
                    "grammar": grammar
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ChatCompletion,
            stream=stream or False,
            stream_cls=AsyncStream[ChatCompletionChunk],
        )


class CompletionsWithRawResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.create = to_raw_response_wrapper(
            completions.create,
        )


class AsyncCompletionsWithRawResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.create = async_to_raw_response_wrapper(
            completions.create,
        )


class CompletionsWithStreamingResponse:
    def __init__(self, completions: Completions) -> None:
        self._completions = completions

        self.create = to_streamed_response_wrapper(
            completions.create,
        )


class AsyncCompletionsWithStreamingResponse:
    def __init__(self, completions: AsyncCompletions) -> None:
        self._completions = completions

        self.create = async_to_streamed_response_wrapper(
            completions.create,
        )
