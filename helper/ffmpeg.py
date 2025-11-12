# ---------------------------------------------------
# File Name: Ffmpeg.py
# Author: NeonAnurag
# GitHub: https://github.com/MyselfNeon/
# Telegram: https://t.me/MyelfNeon
# Created: 2025-11-21
# Last Modified: 2025-11-22
# Version: Latest
# License: MIT License
# ---------------------------------------------------

import time
import os
import asyncio
from PIL import Image
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from pyrogram.types import Message


async def fix_thumb(thumb):
    width = 0
    height = 0
    try:
        if thumb is not None:
            parser = createParser(thumb)
            metadata = extractMetadata(parser)
            if metadata.has("width"):
                width = metadata.get("width")
            if metadata.has("height"):
                height = metadata.get("height")

            # Open the image file
            with Image.open(thumb) as img:
                # Convert the image to RGB format and save it back to the same file
                img.convert("RGB").save(thumb)

                # Resize the image
                resized_img = img.resize((width, height))

                # Save the resized image in JPEG format
                resized_img.save(thumb, "JPEG")

            parser.close()
    except Exception as e:
        print(e)
        thumb = None

    return width, height, thumb


async def take_screen_shot(video_file, output_directory, ttl):
    out_put_file_name = f"{output_directory}/{time.time()}.jpg"
    file_genertor_command = [
        "ffmpeg",
        "-ss",
        str(ttl),
        "-i",
        video_file,
        "-vframes",
        "1",
        out_put_file_name
    ]
    process = await asyncio.create_subprocess_exec(
        *file_genertor_command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    e_response = stderr.decode().strip()
    t_response = stdout.decode().strip()

    if os.path.lexists(out_put_file_name):
        return out_put_file_name
    return None


async def add_metadata(input_path, output_path, metadata, ms: Message):
    try:
        await ms.edit("<i><b>I Found Metadata, Adding Into Your File ⚡</b></i>")
        command = [
            "ffmpeg", "-y", "-i", input_path, "-map", "0",
            "-c:s", "copy", "-c:a", "copy", "-c:v", "copy",
            "-metadata", f"title={metadata}",        # Set Title Metadata
            "-metadata", f"author={metadata}",       # Set Author Metadata
            "-metadata:s:s", f"title={metadata}",    # Set Subtitle Metadata
            "-metadata:s:a", f"title={metadata}",    # Set Audio Metadata
            "-metadata:s:v", f"title={metadata}",    # Set Video Metadata
            "-metadata", f"artist={metadata}",       # Set Artist Metadata
            output_path
        ]

        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        e_response = stderr.decode().strip()
        t_response = stdout.decode().strip()

        print(e_response)
        print(t_response)

        if os.path.exists(output_path):
            await ms.edit("<i><b>Metadata Has Been Successfully Added To Your File ✅</b></i>")
            return output_path
        else:
            await ms.edit("<i>Failed To Add Metadata To Your File ❌</i>")
            return None

    except Exception as e:
        print(f"Error occurred while adding metadata: {str(e)}")
        await ms.edit("<i><b>An Error Occurred While Adding Metadata To Your File ❌</b></i>")
        return None
        

# Dont remove Credits
# Developer Telegram @MyselfNeon
# Update channel - @NeonFiles
