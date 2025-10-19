import asyncio
import logging
import os
from datetime import datetime
from pytz import timezone
from pyrogram import Client, __version__
from pyrogram.raw.all import layer
import pyromod
import pyrogram.utils
import aiohttp
from aiohttp import web

from config import Config, KEEP_ALIVE_URL
from route import web_server  # your async web_server

# Fix for invalid peer IDs
pyrogram.utils.MIN_CHAT_ID = -999999999999
pyrogram.utils.MIN_CHANNEL_ID = -1009999999999

# Setup structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------------------- SAFE TASK WRAPPER ----------------------
async def safe_task(coro, name="Task"):
    """Run a long-running task safely with exception handling."""
    while True:
        try:
            await coro()
        except Exception as e:
            logging.error(f"{name} failed: {e}")
            await asyncio.sleep(5)  # prevent crash loops

# ---------------------- KEEP-ALIVE TASK ----------------------
async def keep_alive():
    """Send a GET request to KEEP_ALIVE_URL every 300 seconds."""
    async with aiohttp.ClientSession() as session:
        while True:
            try:
                await session.get(KEEP_ALIVE_URL)
                logging.info("Sent keep-alive request.")
            except Exception as e:
                logging.error(f"Keep-alive request failed: {e}")
            await asyncio.sleep(300)

# ---------------------- BOT CLASS ----------------------
class Bot(Client):
    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},  # load all plugins
            sleep_threshold=15
        )

    async def on_startup(self):
        """Custom startup tasks."""
        me = await self.get_me()
        self.mention = me.mention if hasattr(me, "mention") else f"@{me.username}"
        self.username = me.username
        self.uptime = datetime.now()

        logging.info(f"{me.first_name} Started... ✨️")

        # Notify admins
        for admin_id in Config.ADMIN:
            try:
                msg = await self.send_message(admin_id, "**__Rename Bot 2GB Is Started... 🚀__**")
                await asyncio.sleep(10)
                await self.delete_messages(chat_id=admin_id, message_ids=msg.id)
            except Exception as e:
                logging.warning(f"Failed to notify admin {admin_id}: {e}")

        # Send log to log channel
        if Config.LOG_CHANNEL:
            try:
                curr = datetime.now(timezone("Asia/Kolkata"))
                date = curr.strftime('%d %B, %Y')
                time = curr.strftime('%I:%M:%S %p')
                await self.send_message(
                    Config.LOG_CHANNEL,
                    f"**⚡ __{self.mention} Restarted__**\n\n"
                    f"📅 **__Date :__** __{date}__\n"
                    f"⏰ **__Time :__** __{time}__\n"
                    f"🌐 **__Timezone :__** __Asia/Kolkata__\n"
                    f"🉐 **__Version :__** __v{__version__} Layer{layer}__"
                )
            except Exception as e:
                logging.warning(f"Failed to send log channel message: {e}")

        # Start web server if enabled
        if Config.WEBHOOK:
            try:
                web_app = await web_server()
                runner = web.AppRunner(web_app)
                await runner.setup()
                site = web.TCPSite(runner, "0.0.0.0", 8080)
                await site.start()
                logging.info("Web server started on port 8080")
            except Exception as e:
                logging.error(f"Failed to start web server: {e}")

# ---------------------- OPTIONAL SCHEDULED RESTART ----------------------
async def scheduled_restart(bot: Bot):
    """Restart the bot once every 24 hours."""
    while True:
        await asyncio.sleep(24*60*60)  # 24 hours
        logging.info("Scheduled bot restart initiated...")
        if Config.LOG_CHANNEL:
            try:
                await bot.send_message(Config.LOG_CHANNEL, "🔄 Bot restarting (scheduled)...")
            except:
                pass
        os.execl(sys.executable, sys.executable, *sys.argv)

# ---------------------- MAIN ----------------------
async def main():
    bot = Bot()
    try:
        await bot.start()
        await bot.on_startup()

        # Start safe background tasks
        asyncio.create_task(safe_task(keep_alive, "Keep-Alive"))
        if Config.SCHEDULE_RESTART:
            asyncio.create_task(safe_task(lambda: scheduled_restart(bot), "Scheduled-Restart"))

        # Keep the bot running forever
        await asyncio.Event().wait()
    except Exception as e:
        logging.error(f"Bot crashed: {e}")
        await bot.stop()
        await asyncio.sleep(5)
        raise e

# ---------------------- RUN ----------------------
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
