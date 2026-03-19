import openai

async def speech_to_text(file):
    audio_file = open(file, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]
