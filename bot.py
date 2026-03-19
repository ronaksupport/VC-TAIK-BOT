from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream.quality import HighQualityAudio

from ai import ai_reply
from voice import speech_to_text, eleven_voice
from music import download_song
from queue import add_queue, next_song
from buttons import player_buttons
from config import *

app = Client("ultra", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
vc = PyTgCalls(app)


# 🎤 VOICE AUTO REPLY
@app.on_message(filters.voice)
async def voice_ai(client, message):
    file = await message.download()

    text = await speech_to_text(file)

    reply = await ai_reply(text)

    voice = eleven_voice(reply)

    await vc.change_stream(
        GROUP_ID,
        InputAudioStream(voice, HighQualityAudio())
    )

    await message.reply(f"🧠 {reply}")


# 🎵 MUSIC QUEUE
@app.on_message(filters.command("play"))
async def play(client, message):
    query = " ".join(message.command[1:])
    song = download_song(query)

    add_queue(song)

    await message.reply(
        f"🎶 Added: {query}",
        reply_markup=player_buttons()
    )

    if len(queue) == 1:
        await vc.change_stream(
            GROUP_ID,
            InputAudioStream(song, HighQualityAudio())
        )


# 🔁 SKIP BUTTON
@app.on_callback_query()
async def callbacks(client, cb):
    if cb.data == "skip":
        song = next_song()
        if song:
            await vc.change_stream(
                GROUP_ID,
                InputAudioStream(song, HighQualityAudio())
            )
        await cb.answer("Skipped")


# 🚀 AUTO JOIN + AUTO RESTART
async def main():
    await app.start()
    await vc.start()

    await vc.join_group_call(
        GROUP_ID,
        InputAudioStream("silence.mp3", HighQualityAudio())
    )

    print("🔥 ULTRA BOT RUNNING")

from pyrogram import idle
app.run(main())
