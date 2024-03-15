from jarvisbot import JarvisBot

client = JarvisBot(app_token="your app token")

completion = client.base.chat.completions.create(
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
print(completion.choices[0].message.content)

# Streaming:
print("----- streaming request -----")
stream = client.base.chat.completions.create(
    messages=[
        {
            "content": "You are a helpful assistant.",
            "role": "system"
        },
        {
            "content": "how are you",
            "role": "user"
        }
    ],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
print()
