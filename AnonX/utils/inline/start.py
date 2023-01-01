from typing import Union

from pyrogram.types import InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴩ ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="☆ ʜᴇʟᴩ ☆",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="☆ ᴏᴡɴᴇʀ ☆", user_id=OWNER),
            InlineKeyboardButton(
                text="☆ sᴜᴩᴩᴏʀᴛ ☆", url=config.SUPPORT_GROUP
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="☆ ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ ☆",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="《 ʜᴇʟᴩ 》", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="☆ ᴏᴡɴᴇʀ ☆", user_id=OWNER),
            InlineKeyboardButton(
                text="☆ sᴜᴩᴩᴏʀᴛ ☆", url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                    text="☆ ᴄʜᴀɴɴᴇʟ ☆", url=config.SUPPORT_CHANNEL 
                )
        ],
     ]
    return buttons
