import os, time, re
id_pattern = re.compile(r'^.\d+$')


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","MyselfNeon")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://files.catbox.moe/tc8drk.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '841851780').split()]

    # channels logs
    FORCE_SUB   = os.environ.get("FORCE_SUB", "NeonFiles") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001889915480"))

    # web response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))

    # optional restart feature
    SCHEDULE_RESTART = False  # Set True to auto-restart every 24h

    # Keep-Alive URL (for Render, etc.)
    KEEP_ALIVE_URL = os.environ.get("KEEP_ALIVE_URL", "https://rename2gb-bot-82je.onrender.com/")

class Txt(object):
    START_TXT = (
        "<b><i>Hᴇʟʟᴏ</i> {} 👋</b>\n\n"
        "<i>I Aᴍ A Pᴏᴡᴇʀғᴜʟ Aᴅᴠᴀɴᴄᴇᴅ Rᴇɴᴀᴍᴇ Bᴏᴛ.</i>\n"
        "<i>Dᴇᴠᴇʟᴏᴘᴇᴅ Bʏ "
        "<a href='https://t.me/MyselfNeon'>NᴇᴏɴAɴᴜʀᴀɢ</a>.</i>\n\n"
        "• <b><i>Rᴇɴᴀᴍᴇ Fɪʟᴇs</i></b>\n"
        "• <b><i>Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏs ♻️ Fɪʟᴇs</i></b>\n"
        "• <b><i>Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴀᴘᴛɪᴏɴ</i></b>"
    )

    ABOUT_TXT = """
╭───────────────⍟
├<b><i>🤖 Mʏ Nᴀᴍᴇ</i></b> : <b>{}</b>
├<b><i>🖥️ Dᴇᴠᴇʟᴏᴘᴇʀ</i></b> : <a href=https://t.me/Talk2NeonBot><b><i>Cᴏɴᴛᴀᴄᴛ Mᴇ</i></b></a> 
├<b><i>👨‍💻 Pʀᴏɢʀᴀᴍᴍᴇʀ</i></b> : <a href=https://t.me/MyselfNeon><b><i>MʏsᴇʟғNᴇᴏɴ</i></b></a>
├<b><i>📕 Lɪʙʀᴀʀʏ</i></b> : <a href=https://github.com/pyrogram><b><i>Pʏʀᴏɢʀᴀᴍ</i></b></a>
├<b><i>✏️ Lᴀɴɢᴜᴀɢᴇ</i></b> : <a href=https://www.python.org><b><i>Pʏᴛʜᴏɴ 3</i></b></a>
├<b><i>💾 Dᴀᴛᴀʙᴀsᴇ</i></b> : <a href=https://cloud.mongodb.com><b><i>Mᴏɴɢᴏ DB</i></b></a>
├<b><i>📢 Cʜᴀɴɴᴇʟ</i></b> : <a href=https://t.me/NeonFiles><b><i>Rᴇɴᴀᴍᴇ ᴠ4.5.0</i></a></b>     
╰───────────────⍟
"""
