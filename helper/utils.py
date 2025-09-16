import math
import time
import re
import os
import shutil
from datetime import datetime
from pytz import timezone
from config import Config, Txt
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 5.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "{0}{1}".format(
            "".join(["▣" for _ in range(math.floor(percentage / 5))]),
            "".join(["▢" for _ in range(20 - math.floor(percentage / 5))])
        )

        tmp = progress + Txt.PROGRESS_BAR.format(
            round(percentage, 2),
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            estimated_total_time if estimated_total_time != "" else "0 s"
        )
        try:
            await message.edit(
                text=f"{ud_type}\n\n{tmp}",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("✖️ 𝖢𝖺𝗇𝖼𝖾𝗅 ✖️", callback_data="close")]]
                ),
            )
        except:
            pass


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    dic_powerN = {0: " ", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + dic_powerN[n] + "B"


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + "d, ") if days else "")
        + ((str(hours) + "h, ") if hours else "")
        + ((str(minutes) + "m, ") if minutes else "")
        + ((str(seconds) + "s, ") if seconds else "")
        + ((str(milliseconds) + "ms, ") if milliseconds else "")
    )
    return tmp[:-2]


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)


async def send_log(b, u):
    if Config.LOG_CHANNEL is not None:
        curr = datetime.now(timezone("Asia/Kolkata"))
        date = curr.strftime("%d %B, %Y")
        time = curr.strftime("%I:%M:%S %p")
        await b.send_message(
            Config.LOG_CHANNEL,
            f"<b>#𝖭𝖾𝗐𝖴𝗌𝖾𝗋 👤</b> \n\n"
            f"<b><i>𝖴𝗌𝖾𝗋 𝖬𝖾𝗇𝗍𝗂𝗈𝗇 : {u.mention}</b></i>\n"
            f"<b><i>𝖴𝗌𝖾𝗋 𝖨𝖣</b> : `{u.id}`</b></i>\n"
            f"<b><i>𝖥𝗂𝗋𝗌𝗍 𝖭𝖺𝗆e : {u.first_name}</b></i>\n"
            f"<b><i>𝖫𝖺𝗌𝗍 𝖭𝖺𝗆𝖾 : {u.last_name}</b></i>\n"
            f"<b><i>𝖴𝗌𝖾𝗋 𝖭𝖺𝗆e : @{u.username}</b></i>\n"
            f"<b><i>𝖴𝗌𝖾𝗋 𝖫𝗂𝗇𝗄 : <a href='tg://openmessage?user_id={u.id}'>𝖢𝗅𝗂𝖼𝗄 𝖧𝖾𝗋𝖾</a></b></i>\n"
            f"<b><i>𝖣𝖺𝗍𝖾 : {date}\n𝖳𝗂𝗆𝖾 : {time}</b></i>",
        )


def add_prefix_suffix(input_string, prefix="", suffix=""):
    pattern = r"(?P<filename>.*?)(\.\w+)?$"
    match = re.search(pattern, input_string)
    if match:
        filename = match.group("filename")
        extension = match.group(2) or ""
        if prefix is None:
            if suffix is None:
                return f"{filename}{extension}"
            return f"{filename} {suffix}{extension}"
        elif suffix is None:
            if prefix is None:
                return f"{filename}{extension}"
            return f"{prefix}{filename}{extension}"
        else:
            return f"{prefix}{filename} {suffix}{extension}"
    else:
        return input_string


def makedir(name: str):
    """
    Create a directory with the specified name.
    If a directory with the same name already exists, it will be removed and a new one will be created.
    """
    if os.path.exists(name):
        shutil.rmtree(name)
    os.mkdir(name)

# Dont remove Credits
# Developer Telegram @MyselfNeon
# Update channel - @NeonFiles
