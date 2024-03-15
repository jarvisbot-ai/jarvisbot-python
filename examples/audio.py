import time
from pathlib import Path
from jarvisbot import JarvisBot

client = JarvisBot(app_token="your app token")

speech_file_path = Path(__file__).parent / "speech.mp3"


def main() -> None:
    stream_to_speakers()

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


def stream_to_speakers() -> None:
    import pyaudio

    player_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)

    start_time = time.time()

    with client.base.audio.speech.with_streaming_response.create(
            response_format="pcm",  # similar to WAV, but without a header chunk at the start.
            text="""I see skies of blue and clouds of white
                The bright blessed days, the dark sacred nights
                And I think to myself
                What a wonderful world""",
    ) as response:
        print(f"Time to first byte: {int((time.time() - start_time) * 1000)}ms")
        for chunk in response.iter_bytes(chunk_size=1024):
            player_stream.write(chunk)

    print(f"Done in {int((time.time() - start_time) * 1000)}ms.")


if __name__ == "__main__":
    main()
