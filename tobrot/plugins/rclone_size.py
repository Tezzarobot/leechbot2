#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) gautamajay52 | 5MysterySD
#
# Copyright 2022 - TeamTele-LeechX
# 
# This is Part of < https://github.com/5MysterySD/Tele-LeechX >
# All Right Reserved

import asyncio
import os
import re

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from tobrot import DESTINATION_FOLDER, LOGGER, UPDATES_CHANNEL 


async def check_size_g(client, message):
    user_id = message.from_user.id 
    u_men = message.from_user.mention
    # await asyncio.sleep(EDIT_SLEEP_TIME_OUT)
    del_it = await message.reply_text("`๐พ Checking Cloud Size... Please Wait !!!`")
    if os.path.exists("rclone.conf"):
        with open("rclone.conf", "r+") as file:
            con = file.read()
            gUP = re.findall(r"\[(.*)\]", con)[0]
            LOGGER.info(gUP)
    destination = f"{DESTINATION_FOLDER}"
    cmd = ["rclone", "size", "--config=./rclone.conf", f"{gUP}:{destination}"]
    gau_tam = await asyncio.create_subprocess_exec(
        *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    gau, tam = await gau_tam.communicate()
    LOGGER.info(gau)
    LOGGER.info(tam)
    LOGGER.info(tam.decode("utf-8"))
    gautam = gau.decode("utf-8")
    LOGGER.info(gautam)
    await asyncio.sleep(5)
    gautam = gautam.replace("Total objects:", "โฃ๐ **Total Files** :").replace("Total size:", "โฃ๐ **Total Size** :")
    await message.reply_text(f"โโโโโ โ __GDriveInfo__ โ โโโโโโโป\nโ\nโฃ๐ค **User** : {u_men}\nโฃ๐ **User ID** : #ID{user_id}\nโฃ๐งพ **Folder Name** : `{DESTINATION_FOLDER}`\n{gautam}โ\nโโโฆ๏ธโ๐ ๐จ๐๐ฃ๐๐ ๐น๐ช {UPDATES_CHANNEL} โฆ๏ธโโน\n\n#CloudSize")
    await del_it.delete()


# gautamajay52


async def g_clearme(client, message):
    inline_keyboard = []
    ikeyboard = []
    ikeyboard.append(
        InlineKeyboardButton("Yes ๐ซ", callback_data=("fuckingdo").encode("UTF-8"))
    )
    ikeyboard.append(
        InlineKeyboardButton("No ๐ค", callback_data=("fuckoff").encode("UTF-8"))
    )
    inline_keyboard.append(ikeyboard)
    reply_markup = InlineKeyboardMarkup(inline_keyboard)
    await message.reply_text(
        "Are you sure? ๐ซ This will delete all your downloads locally ๐ซ",
        reply_markup=reply_markup,
        quote=True,
    )
