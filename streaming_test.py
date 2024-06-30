from openai import OpenAI
import os

client = OpenAI()

speech_file_path = "speech.mp3"

response = client.audio.speech.create(
    model="tts-1-hd",
    voice="alloy",
    input="Tell me a story about the old west."
)

# Stream the response content and write it to a file
with open(speech_file_path, "wb") as file:
    for chunk in response.iter_bytes():
        file.write(chunk)

