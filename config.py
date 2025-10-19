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

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))


# Keep-Alive URL
KEEP_ALIVE_URL = environ.get("KEEP_ALIVE_URL", "https://rename2gb-bot-82je.onrender.com/")  # <-- Add this line

class Txt(object):
    # part of text configuration
    START_TXT = """<b><i>Hᴇʟʟᴏ</i> {} 👋 <i>\n\nI Aᴍ Pᴏᴡᴇʀғᴜʟ Aᴅᴠᴀɴᴄᴇᴅ Rᴇɴᴀᴍᴇ Bᴏᴛ.\nDᴇᴠᴇʟᴏᴘᴇᴅ Bʏ <a href='https://t.me/MyselfNeon'>NᴇᴏɴAɴᴜʀᴀɢ</a>.\n\n• Rᴇɴᴀᴍᴇ Fɪʟᴇs \n• Cᴏɴᴠᴇʀᴛ Vɪᴅᴇᴏs ♻️ Fɪʟᴇs \n• Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ Aɴᴅ Cᴀᴘᴛɪᴏɴ.</i></b>"""

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

    HELP_TXT = """
⁉️ <b><u>__Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ__</u></b>
  
🔸 <i>**Sᴛᴀʀᴛ & Sᴇɴᴅ Aɴʏ Pʜᴏᴛᴏ ᴛᴏ Sᴇᴛ Tʜᴜᴍʙɴᴀɪʟ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ /start**</i>
🔸 <i>**Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ ᴛᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ /view_thumb**</i>
🔸 <i>**Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ ᴛᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴᴀɪʟ /del_thumb**</i>

⁉️ <b><u>__Hᴏᴡ Tᴏ Sᴇᴛ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ__</u></b>

🔹 <i>**Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ ᴛᴏ Sᴇᴛ ᴀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ /set_caption**</i>
🔹 <i>**Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ ᴛᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ /see_caption**</i>
🔹 <i>**Usᴇ Tʜɪs Cᴏᴍᴍᴀɴᴅ ᴛᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ /del_caption**</i>

⁉️ **__Exᴀᴍᴘʟᴇ_**
```
<code>/set_caption</code> 📕 Name ➠ : {filename}

<b>🔗 Size ➠ : {filesize} 
<b>⏰ Duration ➠ : {duration}```

⁉️ <b><u><i>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</i></u></b>

<i>**Sᴇɴᴅ Aɴʏ Fɪʟᴇ Aɴᴅ Tʏᴘᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ Aɴᴅ Sᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ Dᴏᴄᴜᴍᴇɴᴛ, Vɪᴅᴇᴏ, Aᴜᴅɪᴏ ]**</i> 

<b><i>🎊 </b></i><a href=https://t.me/Talk2NeonBot><b><i>Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ</i></b></a>
"""

    PROGRESS_BAR = """\n
 <b><i>🔗 Sɪᴢᴇ :</i></b> {1} | {2}
️ <b><i>⏳️ Dᴏɴᴇ :</i></b> {0}%
 <b><i>🚀 Sᴘᴇᴇᴅ :</i></b> {3}/s
️ <b><i>⏰️ ETA :</i></b> {4}
"""

    DONATE_TXT = """
<b><i>Tʜᴀɴᴋs Fᴏʀ Sʜᴏᴡɪɴɢ Iɴᴛᴇʀᴇsᴛ Iɴ Dᴏɴᴀᴛɪᴏɴ! ❤️</i></b>

<b><i>Iғ Yᴏᴜ Lɪᴋᴇ Mʏ Bᴏᴛs & Pʀᴏᴊᴇᴄᴛs, Yᴏᴜ Cᴀɴ 🎁 Dᴏɴᴀᴛᴇ Mᴇ Aɴʏ Aᴍᴏᴜɴᴛ Fʀᴏᴍ 10 Rs Uᴘᴛᴏ Yᴏᴜʀ Cʜᴏɪᴄᴇ</i></b>

<b><i>🛍 UPI ID:</i></b> `NeonAn23@axl`


<b><i>💬 Fᴏʀ Aɴʏ Hᴇʟᴘ Msɢ @Talk2NeonBot </i></b>
"""



