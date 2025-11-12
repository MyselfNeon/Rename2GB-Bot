# ---------------------------------------------------
# File Name: File_Rename.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# Created: 2025-11-21
# Last Modified: 2025-11-22
# Version: Latest
# License: MIT License
# ---------------------------------------------------

import os
import re
import time
import random
import asyncio

from asyncio import sleep
from PIL import Image
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata

from pyrogram import Client, filters
from pyrogram.enums import MessageMediaType
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply

from helper.ffmpeg import fix_thumb, take_screen_shot, add_metadata
from helper.utils import progress_for_pyrogram, convert, humanbytes, add_prefix_suffix
from helper.database import jishubotz


# ======================= Start Rename ======================= #

@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name

    if file.file_size > 2000 * 1024 * 1024:
        return await message.reply_text(
            "<b><i>Sorry Bro This Bot Doesn't Support Uploading Files Bigger Than 2GB</b></i>"
        )

    try:
        await message.reply_text(
            text=f"**__Please Enter New Filename...__**\n\n**__Old File Name__** :- `{filename}`",
            reply_to_message_id=message.id,
            reply_markup=ForceReply(True)
        )
        await sleep(30)

    except FloodWait as e:
        await sleep(e.value)
        await message.reply_text(
            text=f"**__Please Enter New Filename__**\n\n**Old File Name** :- `{filename}`",
            reply_to_message_id=message.id,
            reply_markup=ForceReply(True)
        )

    except:
        pass


# ======================= Handle Reply (New Name) ======================= #

@Client.on_message(filters.private & filters.reply)
async def refunc(client, message):
    reply_message = message.reply_to_message

    if (reply_message.reply_markup) and isinstance(reply_message.reply_markup, ForceReply):
        new_name = message.text
        await message.delete()

        msg = await client.get_messages(message.chat.id, reply_message.id)
        file = msg.reply_to_message
        media = getattr(file, file.media.value)

        if not "." in new_name:
            if "." in media.file_name:
                extn = media.file_name.rsplit(".", 1)[-1]
            else:
                extn = "mkv"
            new_name = new_name + "." + extn

        await reply_message.delete()

        button = [[InlineKeyboardButton("📁 Document", callback_data="upload_document")]]

        if file.media in [MessageMediaType.VIDEO, MessageMediaType.DOCUMENT]:
            button.append([InlineKeyboardButton("🎥 Video", callback_data="upload_video")])
        elif file.media == MessageMediaType.AUDIO:
            button.append([InlineKeyboardButton("🎵 Audio", callback_data="upload_audio")])

        await message.reply(
            text=f"**__Select The Output File Type__**\n\n**__File Name__ :-** `{new_name}`",
            reply_to_message_id=file.id,
            reply_markup=InlineKeyboardMarkup(button)
        )


# ======================= Callback: Upload ======================= #

@Client.on_callback_query(filters.regex("upload"))
async def doc(bot, update):
    # Create Metadata directory
    if not os.path.isdir("Metadata"):
        os.mkdir("Metadata")

    # Extracting necessary information
    prefix = await jishubotz.get_prefix(update.message.chat.id)
    suffix = await jishubotz.get_suffix(update.message.chat.id)

    new_name = update.message.text
    new_filename_ = new_name.split(":-")[1]

    try:
        new_filename = add_prefix_suffix(new_filename_, prefix, suffix)
    except Exception as e:
        return await update.message.edit(
            f"**__Something Went Wrong Can't Able To Set Prefix Or Suffix 🥺__** \n\n"
            f"**__Contact My Creator :__** @Talk2neonBot\n\n**Error :** `{e}`"
        )

    file_path = f"downloads/{update.from_user.id}/{new_filename}"
    file = update.message.reply_to_message

    ms = await update.message.edit("🚀 <b><i>Trying To Download ...</i></b> ⚡")

    try:
        path = await bot.download_media(
            message=file,
            file_name=file_path,
            progress=progress_for_pyrogram,
            progress_args=("🚀 Try To Downloading...  ⚡", ms, time.time())
        )
    except Exception as e:
        return await ms.edit(e)

    # Metadata Adding
    _bool_metadata = await jishubotz.get_metadata(update.message.chat.id)

    if _bool_metadata:
        metadata = await jishubotz.get_metadata_code(update.message.chat.id)
        metadata_path = f"Metadata/{new_filename}"
        await add_metadata(path, metadata_path, metadata, ms)
    else:
        await ms.edit("⏳ <b><i>Mode Changing ...</i></b> ⚡")

    # Extract Duration
    duration = 0
    try:
        parser = createParser(file_path)
        metadata = extractMetadata(parser)
        if metadata.has("duration"):
            duration = metadata.get("duration").seconds
        parser.close()
    except:
        pass

    # Caption & Thumbnail
    ph_path = None
    user_id = int(update.message.chat.id)
    media = getattr(file, file.media.value)

    c_caption = await jishubotz.get_caption(update.message.chat.id)
    c_thumb = await jishubotz.get_thumbnail(update.message.chat.id)

    if c_caption:
        try:
            caption = c_caption.format(
                filename=new_filename,
                filesize=humanbytes(media.file_size),
                duration=convert(duration)
            )
        except Exception as e:
            return await ms.edit(text=f"Your Caption Error Except Keyword Argument: ({e})")
    else:
        caption = f"**{new_filename}**"

    if (media.thumbs or c_thumb):
        if c_thumb:
            ph_path = await bot.download_media(c_thumb)
            width, height, ph_path = await fix_thumb(ph_path)
        else:
            try:
                ph_path_ = await take_screen_shot(
                    file_path,
                    os.path.dirname(os.path.abspath(file_path)),
                    random.randint(0, duration - 1)
                )
                width, height, ph_path = await fix_thumb(ph_path_)
            except Exception as e:
                ph_path = None
                print(e)

    # Uploading
    await ms.edit("✨ <b><i>Uploading now ...</i></b> ⚡")
    type = update.data.split("_")[1]

    try:
        if type == "document":
            await bot.send_document(
                update.message.chat.id,
                document=metadata_path if _bool_metadata else file_path,
                thumb=ph_path,
                caption=caption,
                progress=progress_for_pyrogram,
                progress_args=("✨ <b><i>Uploading now ...</i></b> ⚡", ms, time.time())
            )

        elif type == "video":
            await bot.send_video(
                update.message.chat.id,
                video=metadata_path if _bool_metadata else file_path,
                caption=caption,
                thumb=ph_path,
                duration=duration,
                progress=progress_for_pyrogram,
                progress_args=("✨ <b><i>Uploading now ...</i></b> ⚡", ms, time.time())
            )

        elif type == "audio":
            await bot.send_audio(
                update.message.chat.id,
                audio=metadata_path if _bool_metadata else file_path,
                caption=caption,
                thumb=ph_path,
                duration=duration,
                progress=progress_for_pyrogram,
                progress_args=("✨ <b><i>Uploading now ...</i></b> ⚡", ms, time.time())
            )

    except Exception as e:
        os.remove(file_path)
        if ph_path:
            os.remove(ph_path)
        return await ms.edit(f"**__Error :__** `{e}`")

    # Cleanup
    await ms.delete()
    if ph_path:
        os.remove(ph_path)
    if file_path:
        os.remove(file_path)


# Dont remove Credits
# Developer Telegram @MyselfNeon
# Update channel - @NeonFiles
