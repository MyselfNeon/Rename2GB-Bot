# ---------------------------------------------------
# File Name: Start & Cb.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# Created: 2025-11-21
# Last Modified: 2025-11-22
# Version: Latest
# License: MIT License
# ---------------------------------------------------

import random
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    ForceReply, 
    CallbackQuery
)
from helper.database import jishubotz
from config import Config, Txt  

# ======================= START ======================= #

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await jishubotz.add_user(client, message)

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton('🔊 Uᴘᴅᴀᴛᴇs', url='https://t.me/NeonFiles'),
            InlineKeyboardButton('♻️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/+o1s-8MppL2syYTI9')
        ],
        [
            InlineKeyboardButton('❤️‍🩹 Aʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('🛠️ Hᴇʟᴘ', callback_data='help')
        ],
        [
            InlineKeyboardButton("👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url='https://t.me/MyselfNeon')
        ]
    ])

    if Config.START_PIC:
        await message.reply_photo(
            Config.START_PIC, 
            caption=Txt.START_TXT.format(user.mention), 
            reply_markup=buttons
        )
    else:
        await message.reply_text(
            text=Txt.START_TXT.format(user.mention), 
            reply_markup=buttons, 
            disable_web_page_preview=True
        )

# ======================= CALLBACK HANDLER ======================= #

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 

    if data == "start":
        await query.message.edit_text(
            text=Txt.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton('🔊 Uᴘᴅᴀᴛᴇs', url='https://t.me/NeonFiles'),
                    InlineKeyboardButton('♻️ Sᴜᴩᴩᴏʀᴛ', url='https://t.me/Talk2NeonBot')
                ],
                [
                    InlineKeyboardButton('❤️‍🩹 Aʙᴏᴜᴛ', callback_data='about'),
                    InlineKeyboardButton('🛠️ Hᴇʟᴘ', callback_data='help')
                ],
                [
                    InlineKeyboardButton("👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ", url='https://t.me/MyselfNeon')
                ]
            ])
        )
        await query.answer()

    elif data == "help":
        await query.message.edit_text(
            text=Txt.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("⚡ Aᴅᴍɪɴ Pᴀɴᴇʟ", url="https://myselfneon.github.io/neon/")],
                [
                    InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data="close"),
                    InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data="start")
                ]
            ])            
        )
        await query.answer()

    elif data == "about":
        await query.message.edit_text(
            text=Txt.ABOUT_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🤖 Mᴏʀᴇ Bᴏᴛs", url="https://t.me/NeonFiles")],
                [
                    InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data="close"),
                    InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data="start")
                ]
            ])            
        )
        await query.answer()

    elif data == "close":
        try:
            await query.message.delete()
            if query.message.reply_to_message:
                await query.message.reply_to_message.delete()
        except:
            pass
        await query.answer()

# ======================= DONATE ======================= #

@Client.on_message(filters.private & filters.command(["donate", "d"]))
async def donate(client, message):
    text = Txt.DONATE_TXT
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🦋 Aᴅᴍɪɴ", url="https://t.me/MyselfNeon"), 
            InlineKeyboardButton("✖️ Cʟᴏꜱᴇ", callback_data="close")
        ]
    ])
    await message.reply_text(text=text, reply_markup=buttons)


# Dont remove Credits
# Developer Telegram @MyselfNeon
# Update channel - @NeonFiles
