import os
from pyrogram import Client, filters, enums
from pyrogram.types import Message
import asyncio
import logging
import sys
from sys import executable
from os import execvp
from os import getenv
import time
from random import choice
from dotenv import load_dotenv

load_dotenv(".env")

API_HASH = getenv("API_HASH")
API_ID = int(getenv("API_ID", ""))
STRING_SESSION = getenv("STRING_SESSION")
STIKER = getenv("STIKER")
LINK = getenv("LINK")
CMD = "."
BOTT = getenv("BOTT", "chatbot")
slop = int(getenv("slop", ""))
LOOP = asyncio.get_event_loop()

app = Client(name="botslop",
             api_id=API_ID,
             api_hash=API_HASH,
             session_string=STRING_SESSION,
            )
LOG = -1001879930806

async def main():
  await app.start()
  await app.send_message(BOTT, "/start")
  await app.send_message(LOG, "Aktif")
  try:
    BOT = "chatbot"
    TAI = "CAACAgUAAxkBAAEDrzBjUo9j31j-w3ufERk9urif_pUjPgACFgkAAlmwmFYy2cZceSTp4CoE"
    counts = 900
    for _ in range(counts):
      await app.send_message(BOTT, "/next")
      await asyncio.sleep(5)
      await app.send_sticker(BOTT, TAI)
      await asyncio.sleep(2)
      await app.send_message(BOTT, "**Hallo aku Agnes\nklik stiker diatas ada link @pintarmutualan disitu bnyak cewe/cowo cakepp.**")
      await asyncio.sleep(3)
  except Exception as e:
    await app.send_message(LOG, f"**ERROR:** `{str(e)}`")
    return
  
asyncio.run(main())
