

# Chat

## Completions

Types:

```python
from jarvisbot.types.chat import (
    ChatCompletion,
    ChatCompletionAssistantMessageParam,
    ChatCompletionChunk,
    ChatCompletionContentPartParam,
    ChatCompletionContentPartImageParam,
    ChatCompletionContentPartTextParam,
    ChatCompletionMessageToolCallParam,
    ChatCompletionFunctionMessageParam,
    ChatCompletionMessage,
    ChatCompletionMessageParam,
    ChatCompletionMessageToolCall,
    ChatCompletionNamedToolChoiceParam,
    ChatCompletionRole,
    ChatCompletionSystemMessageParam,
    ChatCompletionToolParam,
    ChatCompletionToolChoiceOptionParam,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam,
)
```

Methods:

- <code title="post /jarvis/v1/token/proxy_llm/llmapi_v1_chat_completions">client.base.chat.completions.<a href="./src/jarvisbot/resources/chat/completions.py">create</a>(\*\*<a href="src/jarvisbot/types/chat/completion_create_params.py">params</a>) -> <a href="./src/jarvisbot/types/chat/chat_completion.py">ChatCompletion</a></code>


# Images

Types:

```python
from jarvisbot.types import Image, ImagesResponse
```

Methods:

- <code title="post /jarvis/v1/token/proxy_img/sdapi_v1_txt2img">client.base.images.<a href="./src/jarvisbot/resources/images.py">create_variation</a>(\*\*<a href="src/jarvisbot/types/image_create_variation_params.py">params</a>) -> <a href="./src/jarvisbot/types/images_response.py">ImagesResponse</a></code>
- <code title="post /jarvis/v1/token/proxy_img/sdapi_v1_img2img">client.base.images.<a href="./src/jarvisbot/resources/images.py">generate</a>(\*\*<a href="src/jarvisbot/types/image_generate_params.py">params</a>) -> <a href="./src/jarvisbot/types/images_response.py">ImagesResponse</a></code>

# Audio

## Transcriptions

Types:

```python
from jarvisbot.types.audio import Transcription
```

Methods:

- <code title="post /jarvis/v1/token/proxy_asr/asrapi_v1_asr">client.base.audio.transcriptions.<a href="./src/jarvisbot/resources/audio/transcriptions.py">create</a>(\*\*<a href="src/jarvisbot/types/audio/transcription_create_params.py">params</a>) -> <a href="./src/jarvisbot/types/audio/transcription.py">Transcription</a></code>


## Speech

Methods:

- <code title="post /jarvis/v1/token/proxy_tts/ttsapi_v1_tts">client.base.audio.speech.<a href="./src/jarvisbot/resources/audio/speech.py">create</a>(\*\*<a href="src/jarvisbot/types/audio/speech_create_params.py">params</a>) -> HttpxBinaryResponseContent</code>


