import time
from pathlib import Path
from jarvisbot import JarvisBot

client = JarvisBot(app_token="your app token")

speech_file_path = Path(__file__).parent / "speech.mp3"


def main() -> None:
    # Create text-to-speech audio file
    with client.base.audio.speech.with_streaming_response.create(
            text="the quick brown fox jumped over the lazy dogs",
    ) as response:
        response.stream_to_file(speech_file_path)

    # Create transcription from audio file
    transcription = client.base.audio.transcriptions.create(
        files=speech_file_path,
        input_format="mp3"
    )
    print(transcription.text)


if __name__ == "__main__":
    main()
