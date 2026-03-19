import openai
import requests
from config import OPENAI_KEY, ELEVEN_KEY

openai.api_key = OPENAI_KEY


# 🎤 Speech → Text (Whisper)
async def speech_to_text(file):
    with open(file, "rb") as audio:
        transcript = openai.Audio.transcribe(
            "whisper-1",
            audio
        )
    return transcript["text"]


# 👩‍🎤 Text → Female Voice (ElevenLabs)
def text_to_voice(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"

    headers = {
        "xi-api-key": ELEVEN_KEY,
        "Content-Type": "application/json"
    }

    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    response = requests.post(url, headers=headers, json=data)

    with open("ai_voice.mp3", "wb") as f:
        f.write(response.content)

    return "ai_voice.mp3"
