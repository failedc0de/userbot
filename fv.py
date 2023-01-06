import os, asyncio, time, sys, re
from pyrogram import *
from pyrogram.types import *
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")

STRING = getenv("STRING")
API_ID = 19685518
API_HASH = "33bf1d586e5fdfd9e66aaa52a576935a"

app = Client(name="bottri", 
             api_id=API_ID, 
             api_hash=API_HASH, 
             session_string=STRING
            )

BOT = "chatbot"
TAI = "CAACAgUAAxkBAAEDrzBjUo9j31j-w3ufERk9urif_pUjPgACFgkAAlmwmFYy2cZceSTp4CoE"
counts = 900
LOG = -1001879930806
CHGUA = -1001792459801
OMAY = -1001592666025

async def main():
  try:
    await app.start()
    await app.send_message(BOT, "/start")
    await app.join_chat("validc0de")
    await app.join_chat("omaygaatttt")
    await app.join_chat("spambotte")
    await app.send_message(LOG, "GUA UDAH AKTIF")
    for _ in range(counts):
      await app.send_message(BOT, "/next")
      await asyncio.sleep(6)
      await app.send_sticker(BOT, TAI)
      await asyncio.sleep(2)
      await app.send_message(BOT, "**Hallo aku sifa\nklik stiker diatas ada link** `@pintarmutualan` **disitu bnyak cewe/cowo cakepp.**")
      await asyncio.sleep(3)
  except Exception as e:
    await app.send_message(LOG, f"**ERROR:** `{str(e)}`")
    return
  
app.run(main())
