import asyncio

from jarvisbot import AsyncJarvisBot

client = AsyncJarvisBot(app_token="your app token")


async def main() -> None:
    stream = await client.base.chat.completions.create(
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
    async for completion in stream:
        if completion.choices[0].delta.content is not None:
            print(completion.choices[0].delta.content, end="")
    await stream.close()
    print()


asyncio.run(main())
