#!/usr/bin/env python

from jarvisbot import JarvisBot
from pathlib import Path

# gets JARVISBOT_APP_TOKEN from your environment variables
client = JarvisBot(app_token="your app token")

prompt = "An astronaut lounging in a tropical resort in space, pixel art"


def main() -> None:
    # Generate an image based on the prompt
    response = client.base.images.generate(prompt=prompt)

    # Prints response containing a base64 image
    images = response.images
    for index, image in enumerate(images):
        import base64
        bs = base64.b64decode(image)
        with open(f"jarvisbot_sd_{index}.png", "wb") as f:
            f.write(bs)

    response = client.base.images.create_variation(init_images=[Path("jarvisbot_sd_0.png")])
    images = response.images
    for index, image in enumerate(images):
        import base64
        bs = base64.b64decode(image)
        with open(f"jarvisbot_sd_image2image_{index}.png", "wb") as f:
            f.write(bs)


if __name__ == "__main__":
    main()
