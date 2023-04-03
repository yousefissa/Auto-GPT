import os

import requests
from dotenv import load_dotenv
from playsound import playsound

# Load environment variables from .env file
load_dotenv()

voices = ["ErXwobaYiN019PkySvjV", "EXAVITQu4vr4xnSDxMaL"]

tts_headers = {
    "Content-Type": "application/json",
    "xi-api-key": os.getenv("ELEVENLABS_API_KEY"),
}


def say_text(text, voice_index=0):
    tts_url = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}".format(
        voice_id=voices[voice_index]
    )

    formatted_message = {"text": text}
    response = requests.post(tts_url, headers=tts_headers, json=formatted_message)

    if response.status_code == 200:
        with open("speech.mpeg", "wb") as f:
            f.write(response.content)
        playsound("speech.mpeg")
        # Delete audio file
        os.remove("speech.mpeg")
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.content)
