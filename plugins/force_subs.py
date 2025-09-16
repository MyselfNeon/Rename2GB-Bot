from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant

from config import Config
from helper.database import jishubotz


# ======================= Force Sub Helper ======================= #

async def not_subscribed(_, client, message):
    """Check if user is subscribed to the FORCE_SUB channel or banned."""
    await jishubotz.add_user(client, message)

    if not Config.FORCE_SUB:
        return False

    try:
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)
        if user.status == enums.ChatMemberStatus.BANNED:
            return True
        else:
            return False
    except UserNotParticipant:
        pass

    return True


# ======================= Force Sub Handler ======================= #

@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    """Ask user to join the update channel if not subscribed."""
    buttons = [
        [InlineKeyboardButton(text="📢 Join Update Channel 📢", url=f"https://t.me/{Config.FORCE_SUB}")]
    ]

    text = (
        f"<b>Hello {message.from_user.mention} \n\n"
        f"You Need To Join In My Channel To Use Me\n\n"
        f"Kindly Please Join Channel</b>"
    )

    try:
        user = await client.get_chat_member(Config.FORCE_SUB, message.from_user.id)
        if user.status == enums.ChatMemberStatus.BANNED:
            return await client.send_message(
                message.from_user.id,
                text="Sorry You Are Banned To Use Me"
            )
    except UserNotParticipant:
        return await message.reply_text(
            text=text,
            quote=True,
            reply_markup=InlineKeyboardMarkup(buttons)
        )

    return await message.reply_text(
        text=text,
        quote=True,
        reply_markup=InlineKeyboardMarkup(buttons)
    )


# Dont remove Credits
# Developer Telegram @MyselfNeon
# Update channel - @NeonFiles
