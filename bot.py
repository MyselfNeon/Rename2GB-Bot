from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
from config import Config
from aiohttp import web
from route import web_server
import pyromod
import pyrogram.utils
import asyncio   # ✅ needed for sleep

pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -1009999999999


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention if hasattr(me, "mention") else f"@{me.username}"
        self.username = me.username  
        self.uptime = datetime.now()   # or Config.BOT_UPTIME if you want a fixed value  

        if Config.WEBHOOK:
            web_app = await web_server()   # ✅ await async web_server
            app = web.AppRunner(web_app)   # ✅ pass Application, not coroutine
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", 8080).start()     

        print(f"{me.first_name} Is Started... ✨️")

        # Send admin message & auto-delete after 10 seconds
        for admin_id in Config.ADMIN:
            try:
                msg = await self.send_message(admin_id, "**__Rename Bot 2GB Is Started... 🚀🚀__**")
                await asyncio.sleep(10)
                await self.delete_messages(chat_id=admin_id, message_ids=msg.id)
            except:
                pass
        
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(
                    Config.LOG_CHANNEL,
                    f"**__{self.mention} Is Restarted ✅__**\n\n"
                    f"📅 **__Date : {date}__**\n"
                    f"⏰ **__Time : {time}__**\n"
                    f"🌐 **__Timezone : Asia/Kolkata               __**\n"
                    f"🉐 **__Version : v{__version__} Layer{layer}__**"
                )                                
            except:
                print("Please Make This Bot Admin In Your Log Channel")

Bot().run()
