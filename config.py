import os
import time
import re

# ID pattern for detecting numeric Telegram IDs
id_pattern = re.compile(r'^.\d+$')


class Config(object):
    """Main configuration class for the Rename Bot"""

    # --- Pyrogram Client Config ---
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # --- Database Config ---
    DB_NAME = os.environ.get("DB_NAME", "MyselfNeon")
    DB_URL = os.environ.get("DB_URL", "")

    # --- Bot Info ---
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get(
        "START_PIC",
        "https://files.catbox.moe/tc8drk.jpg"
    )

    # --- Admins ---
    ADMIN = [
        int(admin) if id_pattern.search(admin) else admin
        for admin in os.environ.get('ADMIN', '841851780').split()
    ]

    # --- Channels & Logs ---
    FORCE_SUB = os.environ.get("FORCE_SUB", "NeonFiles")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001889915480"))

    # --- Webhook / Deployment Config ---
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))

    # --- Scheduled Restart & Keep Alive ---
    SCHEDULE_RESTART = False  # Set True for 24h scheduled restart
    KEEP_ALIVE_URL = os.environ.get(
        "KEEP_ALIVE_URL",
        "https://rename2gb-bot-82je.onrender.com/"
    )


class Txt(object):
    """All text templates for messages and commands"""

    START_TXT = (
        "<b><i>Hᴇʟʟᴏ</i> {} 👋</b>\n\n"
        "<i>I Aᴍ A Pᴏᴡᴇʀғᴜʟ Aᴅᴠᴀɴᴄᴇᴅ Rᴇɴᴀᴍᴇ Bᴏᴛ.\n"
        "Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ <a href='https://t.me/MyselfNeon'>NᴇᴏɴAɴᴜʀᴀɢ</a>.\n\n"
        "• Rᴇɴᴀᴍᴇ Fɪʟᴇs\n"
        "• Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏs ♻️ Fɪʟᴇs\n"
        "• Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴀᴘᴛɪᴏɴ.</i>"
    )

    ABOUT_TXT = (
        "╭───────────────⍟\n"
        "├<b><i>🤖 Mʏ Nᴀᴍᴇ</i></b> : <b>{}</b>\n"
        "├<b><i>🖥️ Dᴇᴠᴇʟᴏᴘᴇʀ</i></b> : "
        "<a href=https://t.me/Talk2NeonBot><b><i>Cᴏɴᴛᴀᴄᴛ Mᴇ</i></b></a>\n"
        "├<b><i>👨‍💻 Pʀᴏɢʀᴀᴍᴍᴇʀ</i></b> : "
        "<a href=https://t.me/MyselfNeon><b><i>MʏsᴇʟғNᴇᴏɴ</i></b></a>\n"
        "├<b><i>📕 Lɪʙʀᴀʀʏ</i></b> : "
        "<a href=https://github.com/pyrogram><b><i>Pʏʀᴏɢʀᴀᴍ</i></b></a>\n"
        "├<b><i>✏️ Lᴀɴɢᴜᴀɢᴇ</i></b> : "
        "<a href=https://www.python.org><b><i>Pʏᴛʜᴏɴ 3</i></b></a>\n"
        "├<b><i>💾 Dᴀᴛᴀʙᴀsᴇ</i></b> : "
        "<a href=https://cloud.mongodb.com><b><i>Mᴏɴɢᴏ DB</i></b></a>\n"
        "├<b><i>📢 Cʜᴀɴɴᴇʟ</i></b> : "
        "<a href=https://t.me/NeonFiles><b><i>Rᴇɴᴀᴍᴇ ᴠ4.5.0</i></a></b>\n"
        "╰───────────────⍟"
    )

    HELP_TXT = (
        "⁉️ <b><u>__Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ__</u></b>\n\n"
        "🔸 <i>Start & Send Any Photo To Set Thumbnail Automatically</i>\n"
        "🔸 <i>Use /view_thumb To View Your Thumbnail</i>\n"
        "🔸 <i>Use /del_thumb To Delete Your Old Thumbnail</i>\n\n"
        "⁉️ <b><u>__Hᴏᴡ Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ__</u></b>\n\n"
        "🔹 <i>Use /set_caption To Set Caption</i>\n"
        "🔹 <i>Use /see_caption To View Caption</i>\n"
        "🔹 <i>Use /del_caption To Delete Caption</i>\n\n"
        "⁉️ **__Example__**\n"
        "<code>/set_caption</code>\n"
        "📕 Name ➠ : {filename}\n"
        "🔗 Size ➠ : {filesize}\n"
        "⏰ Duration ➠ : {duration}\n\n"
        "⁉️ <b><u>__Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ__</u></b>\n"
        "<i>Send Any File → Type New Name → Select Format</i>\n\n"
        "<b>🎊 </b><a href=https://t.me/Talk2NeonBot><b><i>Contact Developer</i></b></a>"
    )

    PROGRESS_BAR = (
        "\n<b><i>🔗 Sɪᴢᴇ :</i></b> {1} | {2}\n"
        "️<b><i>⏳️ Dᴏɴᴇ :</i></b> {0}%\n"
        "<b><i>🚀 Sᴘᴇᴇᴅ :</i></b> {3}/s\n"
        "️<b><i>⏰️ ETA :</i></b> {4}"
    )

    DONATE_TXT = (
        "<b><i>Tʜᴀɴᴋs Fᴏʀ Sʜᴏᴡɪɴɢ Iɴᴛᴇʀᴇsᴛ Iɴ Dᴏɴᴀᴛɪᴏɴ! ❤️</i></b>\n\n"
        "<b><i>If You Like My Bots & Projects, You Can 🎁 Donate Any Amount.</i></b>\n\n"
        "<b><i>🛍 UPI ID:</i></b> <code>NeonAn23@axl</code>\n\n"
        "<b><i>💬 For Any Help Message @Talk2NeonBot</i></b>"
    )
