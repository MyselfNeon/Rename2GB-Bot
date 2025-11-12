# ---------------------------------------------------
# File Name: Thumbnail.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# Created: 2025-11-21
# Last Modified: 2025-11-22
# Version: Latest
# License: MIT License
# ---------------------------------------------------

from pyrogram import Client, filters
from helper.database import jishubotz

# ======================= VIEW THUMB ======================= #

@Client.on_message(filters.private & filters.command(['view_thumb', 'viewthumb']))
async def view_thumb(client, message):
    """Send the user's saved thumbnail, if exists."""
    thumb = await jishubotz.get_thumbnail(message.from_user.id)

    if thumb:
        await client.send_photo(chat_id=message.chat.id, photo=thumb)
    else:
        await message.reply_text(
            "<b><i>Yᴏᴜ Dᴏɴ'ᴛ Hᴀᴠᴇ Aɴʏ Tʜᴜᴍʙɴᴀɪʟ ❌</i></b>"
        )

# ======================= DELETE THUMB ======================= #

@Client.on_message(filters.private & filters.command(['del_thumb', 'delthumb']))
async def remove_thumb(client, message):
    """Delete the user's saved thumbnail."""
    await jishubotz.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text(
        "<b><i>Tʜᴜᴍʙɴᴀɪʟ Dᴇʟᴇᴛᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ 🗑️</i></b>"
    )

# ======================= SAVE THUMB ======================= #

@Client.on_message(filters.private & filters.photo)
async def add_thumb(client, message):
    """Save a new thumbnail from user's sent photo."""
    temp = await message.reply_text("<b><i>Pʟᴇᴀsᴇ Wᴀɪᴛ ...</i></b>")
    await jishubotz.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)
    await temp.edit("<b><i>Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ✅️</i></b>")


# Dont remove Credits
# Developer Telegram @MyselfNeon
# Update channel - @NeonFiles
