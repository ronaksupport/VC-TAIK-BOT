from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def player_buttons():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("⏸ Pause", callback_data="pause"),
            InlineKeyboardButton("▶️ Resume", callback_data="resume")
        ],
        [
            InlineKeyboardButton("⏭ Skip", callback_data="skip")
        ]
    ])
