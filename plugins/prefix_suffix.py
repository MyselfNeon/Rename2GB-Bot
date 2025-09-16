from pyrogram import Client, filters, enums
from helper.database import jishubotz


# ======================= PREFIX ======================= #

@Client.on_message(filters.private & filters.command('set_prefix'))
async def add_prefix(client, message):
    """Set a custom prefix for the user."""

    if len(message.command) == 1:
        return await message.reply_text(
            "**__Give The Prefix__\n\nExample:- `/set_prefix @Madflix_Bots`**"
        )

    prefix = message.text.split(" ", 1)[1]
    ms = await message.reply_text("Please Wait ...")
    await jishubotz.set_prefix(message.from_user.id, prefix)
    await ms.edit("**Prefix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_prefix'))
async def delete_prefix(client, message):
    """Delete the saved prefix."""

    ms = await message.reply_text("Please Wait ...")
    prefix = await jishubotz.get_prefix(message.from_user.id)

    if not prefix:
        return await ms.edit("**You Don't Have Any Prefix ❌**")

    await jishubotz.set_prefix(message.from_user.id, None)
    await ms.edit("**Prefix Deleted Successfully 🗑️**")


@Client.on_message(filters.private & filters.command('see_prefix'))
async def see_prefix(client, message):
    """View the current saved prefix."""

    ms = await message.reply_text("Please Wait ...")
    prefix = await jishubotz.get_prefix(message.from_user.id)

    if prefix:
        await ms.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await ms.edit("**You Don't Have Any Prefix ❌**")


# ======================= SUFFIX ======================= #

@Client.on_message(filters.private & filters.command('set_suffix'))
async def add_suffix(client, message):
    """Set a custom suffix for the user."""

    if len(message.command) == 1:
        return await message.reply_text(
            "**__Give The Suffix__\n\nExample:- `/set_suffix @Madflix_Bots`**"
        )

    suffix = message.text.split(" ", 1)[1]
    ms = await message.reply_text("Please Wait ...")
    await jishubotz.set_suffix(message.from_user.id, suffix)
    await ms.edit("**Suffix Saved Successfully ✅**")


@Client.on_message(filters.private & filters.command('del_suffix'))
async def delete_suffix(client, message):
    """Delete the saved suffix."""

    ms = await message.reply_text("Please Wait ...")
    suffix = await jishubotz.get_suffix(message.from_user.id)

    if not suffix:
        return await ms.edit("**You Don't Have Any Suffix ❌**")

    await jishubotz.set_suffix(message.from_user.id, None)
    await ms.edit("**Suffix Deleted Successfully ✅**")


@Client.on_message(filters.private & filters.command('see_suffix'))
async def see_suffix(client, message):
    """View the current saved suffix."""

    ms = await message.reply_text("Please Wait ...")
    suffix = await jishubotz.get_suffix(message.from_user.id)

    if suffix:
        await ms.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await ms.edit("**You Don't Have Any Suffix ❌**")


# Dont remove Credits
# Developer Telegram @MyselfNeon
# Update channel - @NeonFiles
