# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional, overload
from typing_extensions import Literal

import httpx

from ..types import Completion, completion_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import required_args, maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    async_to_raw_response_wrapper
)
from .._streaming import Stream, AsyncStream
from .._base_client import (
    make_request_options,
)

__all__ = [
    "Completions",
    "AsyncCompletions",
    "CompletionsWithRawResponse",
    "AsyncCompletionsWithRawResponse",
    "CompletionsWithStreamingResponse",
    "AsyncCompletionsWithStreamingResponse"
]


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
            prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]], None],
            suffix: Optional[str] | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
            echo: Optional[bool] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
            stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
            logprobs: Optional[int] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            best_of: Optional[int] | NotGiven = NOT_GIVEN,
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
    ) -> Completion:
        """
        Creates a completion for the provided prompt and parameters.

        Args:
          model: ID of the model to use.

          prompt: The prompt(s) to generate completions for, encoded as a string, array of
              strings, array of tokens, or array of token arrays.

              Note that <|endoftext|> is the document separator that the model sees during
              training, so if a prompt is not specified the model will generate as if from the
              beginning of a new document.

          best_of: Generates `best_of` completions server-side and returns the "best" (the one with
              the highest log probability per token). Results cannot be streamed.

              When used with `n`, `best_of` controls the number of candidate completions and
              `n` specifies how many to return – `best_of` must be greater than `n`.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          echo: Echo back the prompt in addition to the completion

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the GPT
              tokenizer) to an associated bias value from -100 to 100. You can use this
              [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs.
              Mathematically, the bias is added to the logits generated by the model prior to
              sampling. The exact effect will vary per model, but values between -1 and 1
              should decrease or increase likelihood of selection; values like -100 or 100
              should result in a ban or exclusive selection of the relevant token.

              As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token
              from being generated.

          logprobs: Include the log probabilities on the `logprobs` most likely output tokens, as
              well the chosen tokens. For example, if `logprobs` is 5, the API will return a
              list of the 5 most likely tokens. The API will always return the `logprob` of
              the sampled token, so there may be up to `logprobs+1` elements in the response.

              The maximum value for `logprobs` is 5.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the
              completion.

              The token count of your prompt plus `max_tokens` cannot exceed the model's
              context length.
              for counting tokens.

          n: How many completions to generate for each prompt.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result.

              Determinism is not guaranteed, and you should refer to the `system_fingerprint`
              response parameter to monitor changes in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream: Whether to stream back partial progress. If set, tokens will be sent as
              data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          suffix: The suffix that comes after a completion of inserted text.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

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
            model: Optional[str] | NotGiven = NOT_GIVEN,
            prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]], None],
            stream: Literal[True],
            best_of: Optional[int] | NotGiven = NOT_GIVEN,
            echo: Optional[bool] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            logprobs: Optional[int] | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
            suffix: Optional[str] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
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
    ) -> Stream[Completion]:
        """
        Creates a completion for the provided prompt and parameters.

        Args:
          model: ID of the model to use.

          prompt: The prompt(s) to generate completions for, encoded as a string, array of
              strings, array of tokens, or array of token arrays.

              Note that <|endoftext|> is the document separator that the model sees during
              training, so if a prompt is not specified the model will generate as if from the
              beginning of a new document.

          stream: Whether to stream back partial progress. If set, tokens will be sent as
              data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          best_of: Generates `best_of` completions server-side and returns the "best" (the one with
              the highest log probability per token). Results cannot be streamed.

              When used with `n`, `best_of` controls the number of candidate completions and
              `n` specifies how many to return – `best_of` must be greater than `n`.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          echo: Echo back the prompt in addition to the completion

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the GPT
              tokenizer) to an associated bias value from -100 to 100. You can use this
              [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs.
              Mathematically, the bias is added to the logits generated by the model prior to
              sampling. The exact effect will vary per model, but values between -1 and 1
              should decrease or increase likelihood of selection; values like -100 or 100
              should result in a ban or exclusive selection of the relevant token.

              As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token
              from being generated.

          logprobs: Include the log probabilities on the `logprobs` most likely output tokens, as
              well the chosen tokens. For example, if `logprobs` is 5, the API will return a
              list of the 5 most likely tokens. The API will always return the `logprob` of
              the sampled token, so there may be up to `logprobs+1` elements in the response.

              The maximum value for `logprobs` is 5.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the
              completion.

              The token count of your prompt plus `max_tokens` cannot exceed the model's
              context length.
              for counting tokens.

          n: How many completions to generate for each prompt.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result.

              Determinism is not guaranteed, and you should refer to the `system_fingerprint`
              response parameter to monitor changes in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          suffix: The suffix that comes after a completion of inserted text.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

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
            model: Optional[str] | NotGiven = NOT_GIVEN,
            prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]], None],
            stream: bool,
            best_of: Optional[int] | NotGiven = NOT_GIVEN,
            echo: Optional[bool] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            logprobs: Optional[int] | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
            suffix: Optional[str] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
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
    ) -> Completion | Stream[Completion]:
        """
        Creates a completion for the provided prompt and parameters.

        Args:
          model: ID of the model to use.

          prompt: The prompt(s) to generate completions for, encoded as a string, array of
              strings, array of tokens, or array of token arrays.

              Note that <|endoftext|> is the document separator that the model sees during
              training, so if a prompt is not specified the model will generate as if from the
              beginning of a new document.

          stream: Whether to stream back partial progress. If set, tokens will be sent as
              data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          best_of: Generates `best_of` completions server-side and returns the "best" (the one with
              the highest log probability per token). Results cannot be streamed.

              When used with `n`, `best_of` controls the number of candidate completions and
              `n` specifies how many to return – `best_of` must be greater than `n`.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          echo: Echo back the prompt in addition to the completion

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the GPT
              tokenizer) to an associated bias value from -100 to 100. You can use this
              [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs.
              Mathematically, the bias is added to the logits generated by the model prior to
              sampling. The exact effect will vary per model, but values between -1 and 1
              should decrease or increase likelihood of selection; values like -100 or 100
              should result in a ban or exclusive selection of the relevant token.

              As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token
              from being generated.

          logprobs: Include the log probabilities on the `logprobs` most likely output tokens, as
              well the chosen tokens. For example, if `logprobs` is 5, the API will return a
              list of the 5 most likely tokens. The API will always return the `logprob` of
              the sampled token, so there may be up to `logprobs+1` elements in the response.

              The maximum value for `logprobs` is 5.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the
              completion.

              The token count of your prompt plus `max_tokens` cannot exceed the model's
              context length.
              for counting tokens.

          n: How many completions to generate for each prompt.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result.

              Determinism is not guaranteed, and you should refer to the `system_fingerprint`
              response parameter to monitor changes in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          suffix: The suffix that comes after a completion of inserted text.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

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

    @required_args(["prompt"], ["prompt", "stream"])
    def create(
            self,
            *,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]], None],
            best_of: Optional[int] | NotGiven = NOT_GIVEN,
            echo: Optional[bool] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            logprobs: Optional[int] | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
            stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
            suffix: Optional[str] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
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
    ) -> Completion | Stream[Completion]:
        return self._post(
            "/completions",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "best_of": best_of,
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "suffix": suffix,
                    "temperature": temperature,
                    "top_p": top_p,
                    "user": user,
                    "min_p": min_p,
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
            cast_to=Completion,
            stream=stream or False,
            stream_cls=Stream[Completion],
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
            model: Optional[str] | NotGiven = NOT_GIVEN,
            prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]], None],
            best_of: Optional[int] | NotGiven = NOT_GIVEN,
            echo: Optional[bool] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            logprobs: Optional[int] | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
            stream: Optional[Literal[False]] | NotGiven = NOT_GIVEN,
            suffix: Optional[str] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
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
    ) -> Completion:
        """
        Creates a completion for the provided prompt and parameters.

        Args:
          model: ID of the model to use.

          prompt: The prompt(s) to generate completions for, encoded as a string, array of
              strings, array of tokens, or array of token arrays.

              Note that <|endoftext|> is the document separator that the model sees during
              training, so if a prompt is not specified the model will generate as if from the
              beginning of a new document.

          best_of: Generates `best_of` completions server-side and returns the "best" (the one with
              the highest log probability per token). Results cannot be streamed.

              When used with `n`, `best_of` controls the number of candidate completions and
              `n` specifies how many to return – `best_of` must be greater than `n`.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          echo: Echo back the prompt in addition to the completion

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the GPT
              tokenizer) to an associated bias value from -100 to 100. You can use this
              [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs.
              Mathematically, the bias is added to the logits generated by the model prior to
              sampling. The exact effect will vary per model, but values between -1 and 1
              should decrease or increase likelihood of selection; values like -100 or 100
              should result in a ban or exclusive selection of the relevant token.

              As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token
              from being generated.

          logprobs: Include the log probabilities on the `logprobs` most likely output tokens, as
              well the chosen tokens. For example, if `logprobs` is 5, the API will return a
              list of the 5 most likely tokens. The API will always return the `logprob` of
              the sampled token, so there may be up to `logprobs+1` elements in the response.

              The maximum value for `logprobs` is 5.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the
              completion.

              The token count of your prompt plus `max_tokens` cannot exceed the model's
              context length.

          n: How many completions to generate for each prompt.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result.

              Determinism is not guaranteed, and you should refer to the `system_fingerprint`
              response parameter to monitor changes in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          stream: Whether to stream back partial progress. If set, tokens will be sent as
              data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          suffix: The suffix that comes after a completion of inserted text.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

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
            model: Optional[str] | NotGiven = NOT_GIVEN,
            prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]], None],
            stream: Literal[True],
            best_of: Optional[int] | NotGiven = NOT_GIVEN,
            echo: Optional[bool] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            logprobs: Optional[int] | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
            suffix: Optional[str] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
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
    ) -> AsyncStream[Completion]:
        """
        Creates a completion for the provided prompt and parameters.

        Args:
          model: ID of the model to use.

          prompt: The prompt(s) to generate completions for, encoded as a string, array of
              strings, array of tokens, or array of token arrays.

              Note that <|endoftext|> is the document separator that the model sees during
              training, so if a prompt is not specified the model will generate as if from the
              beginning of a new document.

          stream: Whether to stream back partial progress. If set, tokens will be sent as
              data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          best_of: Generates `best_of` completions server-side and returns the "best" (the one with
              the highest log probability per token). Results cannot be streamed.

              When used with `n`, `best_of` controls the number of candidate completions and
              `n` specifies how many to return – `best_of` must be greater than `n`.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          echo: Echo back the prompt in addition to the completion

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the GPT
              tokenizer) to an associated bias value from -100 to 100. You can use this
              [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs.
              Mathematically, the bias is added to the logits generated by the model prior to
              sampling. The exact effect will vary per model, but values between -1 and 1
              should decrease or increase likelihood of selection; values like -100 or 100
              should result in a ban or exclusive selection of the relevant token.

              As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token
              from being generated.

          logprobs: Include the log probabilities on the `logprobs` most likely output tokens, as
              well the chosen tokens. For example, if `logprobs` is 5, the API will return a
              list of the 5 most likely tokens. The API will always return the `logprob` of
              the sampled token, so there may be up to `logprobs+1` elements in the response.

              The maximum value for `logprobs` is 5.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the
              completion.

              The token count of your prompt plus `max_tokens` cannot exceed the model's
              context length.

          n: How many completions to generate for each prompt.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result.

              Determinism is not guaranteed, and you should refer to the `system_fingerprint`
              response parameter to monitor changes in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          suffix: The suffix that comes after a completion of inserted text.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

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
            model: Optional[str] | NotGiven = NOT_GIVEN,
            prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]], None],
            stream: bool,
            best_of: Optional[int] | NotGiven = NOT_GIVEN,
            echo: Optional[bool] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            logprobs: Optional[int] | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
            suffix: Optional[str] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
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
    ) -> Completion | AsyncStream[Completion]:
        """
        Creates a completion for the provided prompt and parameters.

        Args:
          model: ID of the model to use.

          prompt: The prompt(s) to generate completions for, encoded as a string, array of
              strings, array of tokens, or array of token arrays.

              Note that <|endoftext|> is the document separator that the model sees during
              training, so if a prompt is not specified the model will generate as if from the
              beginning of a new document.

          stream: Whether to stream back partial progress. If set, tokens will be sent as
              data-only
              [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format)
              as they become available, with the stream terminated by a `data: [DONE]`
              message.

          best_of: Generates `best_of` completions server-side and returns the "best" (the one with
              the highest log probability per token). Results cannot be streamed.

              When used with `n`, `best_of` controls the number of candidate completions and
              `n` specifies how many to return – `best_of` must be greater than `n`.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          echo: Echo back the prompt in addition to the completion

          frequency_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on their
              existing frequency in the text so far, decreasing the model's likelihood to
              repeat the same line verbatim.

          logit_bias: Modify the likelihood of specified tokens appearing in the completion.

              Accepts a JSON object that maps tokens (specified by their token ID in the GPT
              tokenizer) to an associated bias value from -100 to 100. You can use this
              [tokenizer tool](/tokenizer?view=bpe) to convert text to token IDs.
              Mathematically, the bias is added to the logits generated by the model prior to
              sampling. The exact effect will vary per model, but values between -1 and 1
              should decrease or increase likelihood of selection; values like -100 or 100
              should result in a ban or exclusive selection of the relevant token.

              As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token
              from being generated.

          logprobs: Include the log probabilities on the `logprobs` most likely output tokens, as
              well the chosen tokens. For example, if `logprobs` is 5, the API will return a
              list of the 5 most likely tokens. The API will always return the `logprob` of
              the sampled token, so there may be up to `logprobs+1` elements in the response.

              The maximum value for `logprobs` is 5.

          max_tokens: The maximum number of [tokens](/tokenizer) that can be generated in the
              completion.

              The token count of your prompt plus `max_tokens` cannot exceed the model's
              context length.
              for counting tokens.

          n: How many completions to generate for each prompt.

              **Note:** Because this parameter generates many completions, it can quickly
              consume your token quota. Use carefully and ensure that you have reasonable
              settings for `max_tokens` and `stop`.

          presence_penalty: Number between -2.0 and 2.0. Positive values penalize new tokens based on
              whether they appear in the text so far, increasing the model's likelihood to
              talk about new topics.

          seed: If specified, our system will make a best effort to sample deterministically,
              such that repeated requests with the same `seed` and parameters should return
              the same result.

              Determinism is not guaranteed, and you should refer to the `system_fingerprint`
              response parameter to monitor changes in the backend.

          stop: Up to 4 sequences where the API will stop generating further tokens. The
              returned text will not contain the stop sequence.

          suffix: The suffix that comes after a completion of inserted text.

          temperature: What sampling temperature to use, between 0 and 2. Higher values like 0.8 will
              make the output more random, while lower values like 0.2 will make it more
              focused and deterministic.

              We generally recommend altering this or `top_p` but not both.

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

    @required_args(["prompt"], ["prompt", "stream"])
    async def create(
            self,
            *,
            model: Optional[str] | NotGiven = NOT_GIVEN,
            prompt: Union[str, List[str], Iterable[int], Iterable[Iterable[int]], None],
            best_of: Optional[int] | NotGiven = NOT_GIVEN,
            echo: Optional[bool] | NotGiven = NOT_GIVEN,
            frequency_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            logit_bias: Optional[Dict[str, int]] | NotGiven = NOT_GIVEN,
            logprobs: Optional[int] | NotGiven = NOT_GIVEN,
            max_tokens: Optional[int] | NotGiven = NOT_GIVEN,
            n: Optional[int] | NotGiven = NOT_GIVEN,
            presence_penalty: Optional[float] | NotGiven = NOT_GIVEN,
            seed: Optional[int] | NotGiven = NOT_GIVEN,
            stop: Union[Optional[str], List[str], None] | NotGiven = NOT_GIVEN,
            stream: Optional[Literal[False]] | Literal[True] | NotGiven = NOT_GIVEN,
            suffix: Optional[str] | NotGiven = NOT_GIVEN,
            temperature: Optional[float] | NotGiven = NOT_GIVEN,
            top_p: Optional[float] | NotGiven = NOT_GIVEN,
            user: str | NotGiven = NOT_GIVEN,
            min_p: Optional[float] | NotGiven = NOT_GIVEN,
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
    ) -> Completion | AsyncStream[Completion]:
        return await self._post(
            "/completions",
            body=maybe_transform(
                {
                    "model": model,
                    "prompt": prompt,
                    "best_of": best_of,
                    "echo": echo,
                    "frequency_penalty": frequency_penalty,
                    "logit_bias": logit_bias,
                    "logprobs": logprobs,
                    "max_tokens": max_tokens,
                    "n": n,
                    "presence_penalty": presence_penalty,
                    "seed": seed,
                    "stop": stop,
                    "stream": stream,
                    "suffix": suffix,
                    "temperature": temperature,
                    "top_p": top_p,
                    "user": user,
                    "min_p": min_p,
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
            cast_to=Completion,
            stream=stream or False,
            stream_cls=AsyncStream[Completion],
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
