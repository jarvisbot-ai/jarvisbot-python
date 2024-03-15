# JarvisBot Python API library
> [!IMPORTANT]
> This SDK is fork from OpenAI repository[tag 1.12.0], we try our best to make it compatible with OPENAI, but it may change in the future.

The JarvisBot Python library provides convenient access to the JarvisBot REST API from any Python 3.8+
application. The library includes type definitions for all request params and response fields,
and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

## Access Token
> [!IMPORTANT]
> JarvisBot SDK is currently undergoing rapid development, which may lead to stability and compatibility issues. You can email support@jarvisbot.ai to request an access token. We will periodically open up trials.

## Installation

```sh
pip install jarvisbot-python
```

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from jarvisbot import JarvisBot

client = JarvisBot(
    # This is the default and can be omitted
    app_token=os.environ.get("JARVISBOT_APP_TOKEN"),
)

chat_completion = client.base.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ]
)
```

While you can provide an `app_token` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `JARVISBOT_APP_TOKEN="My App Token"` to your `.env` file
so that your App Token is not stored in source control.

## Async usage

Simply import `AsyncJarvisBot` instead of `JarvisBot` and use `await` with each API call:

```python
import os
import asyncio
from jarvisbot import AsyncJarvisBot

client = AsyncJarvisBot(
    # This is the default and can be omitted
    app_token=os.environ.get("JARVISBOT_APP_TOKEN"),
)


async def main() -> None:
    chat_completion = await client.base.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
    )


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

## Streaming Responses

We provide support for streaming responses using Server Side Events (SSE).

```python
from jarvisbot import JarvisBot

client = JarvisBot()

stream = client.base.chat.completions.create(
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
```

The async client uses the exact same interface.

```python
from jarvisbot import AsyncJarvisBot

client = AsyncJarvisBot()


async def main():
    stream = await client.base.chat.completions.create(
        messages=[{"role": "user", "content": "Say this is a test"}],
        stream=True,
    )
    async for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")


asyncio.run(main())
```

## Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `jarvisbot.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `jarvisbot.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `jarvisbot.APIError`.

```python
import jarvisbot
from jarvisbot import JarvisBot

client = JarvisBot()

try:
    client.base.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful assistant.",
                "role": "system"
            },
            {
                "content": "What is the capital of France?",
                "role": "user"
            }
        ],
    )
except jarvisbot.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except jarvisbot.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except jarvisbot.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as followed:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from jarvisbot import JarvisBot

# Configure the default for all requests:
client = JarvisBot(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).base.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I get the name of the current day in Node.js?",
        }
    ],
)
```

### Timeouts

By default requests time out after 10 minutes. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/#fine-tuning-the-configuration) object:

```python
from jarvisbot import JarvisBot

# Configure the default for all requests:
client = JarvisBot(
    # 20 seconds (default is 10 minutes)
    timeout=20.0,
)

# More granular control:
client = JarvisBot(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5 * 1000).base.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I list all files in a directory using Python?",
        }
    ]
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

## Advanced

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `JARVISBOT_LOG` to `debug`.

```shell
$ export JARVISBOT_LOG=debug
```

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from jarvisbot import JarvisBot

client = JarvisBot()
response = client.base.chat.completions.with_raw_response.create(
    messages=[{
        "role": "user",
        "content": "Say this is a test",
    }]
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion)
```

For the sync client this will mostly be the same with the exception
of `content` & `text` will be methods instead of properties. In the
async client, all methods will be async.

A migration script will be provided & the migration in general should
be smooth.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

As such, `.with_streaming_response` methods return a different [`APIResponse`](https://github.com/jarvisbot-ai/jarvisbot-python/tree/main/src/jarvisbot/_response.py) object, and the async client returns an [`AsyncAPIResponse`](https://github.com/jarvisbot-ai/jarvisbot-python/tree/main/src/jarvisbot/_response.py) object.

```python
with client.base.chat.completions.with_streaming_response.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
) as response:
    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for proxies
- Custom transports
- Additional [advanced](https://www.python-httpx.org/advanced/#client-instances) functionality

```python
import httpx
from jarvisbot import JarvisBot

client = JarvisBot(
    # Or use the `JARVISBOT_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.


## Requirements

Python 3.8 or higher.
