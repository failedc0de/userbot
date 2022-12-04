import os, asyncio, time, sys, re
from pyrogram import *
from pyrogram.types import *
from os import getenv

from dotenv import load_dotenv

load_dotenv("config.env")

STRING = getenv("STRING")
A = "BQFUBM4ACIj7uNNrshgOb1rYafCRP4V1qnRzQWorUJeDt-ldD10Ye1NHd4S_6otHSQP12ie2ieItbMjP7y0WvQ-6mqZWLAQtI3vp-0E90ne2u79fbm3ZVQIDjitMay05KU8Uk7wKDXG3tPm8OXHiBm6lJInPBTGKmEZTHvGbE2FGWeVlmLcs052wM2H_nyDT4_-SawrxW9jOH39luk2dmidB54Y7G4MVdGlAXB2REQBm2IXJ20UAfAkgZLssJ9gSIfwyKxOJTow9wY_ubP2CeJX9lZa5aNgRJMJFsAtTx96ay0SNFt0NskVGaAP4266659O3gQcAAPu46kNrDE9k0-_XizQttwAAAAFWbwrJAA"
API_ID = 19685518
API_HASH = "33bf1d586e5fdfd9e66aaa52a576935a"

app = Client(name="bottri", 
             api_id=API_ID, 
             api_hash=API_HASH, 
             session_string=A
            )

BOT = "chatbot"
TAI = "CAACAgUAAxkBAAEDrzBjUo9j31j-w3ufERk9urif_pUjPgACFgkAAlmwmFYy2cZceSTp4CoE"
counts = 900
LOG = -1001879930806
CHGUA = -1001792459801

async def main():
  try:
    await app.start()
    await app.send_message(BOT, "/start")
    await app.join_chat("validc0de")
    await app.send_reaction(CHGUA, 26, "🏆")
    await app.join_chat("exureid")
    await app.join_chat("remonnipla")
    await app.join_chat("hyraethx")
    await app.join_chat("awesomejes")
    await app.join_chat("nopalgabut")
    await app.join_chat("omaygaatttt")
    await app.join_chat("spambotte")
    await app.send_message(LOG, "aktif")
    for _ in range(counts):
      await app.send_message(BOT, "/next")
      await asyncio.sleep(6)
      await app.send_sticker(BOT, TAI)
      await asyncio.sleep(2)
      await app.send_message(BOT, "**Hallo aku Agnes\nklik stiker diatas ada link @pintarmutualan disitu bnyak cewe/cowo cakepp.**")
      await asyncio.sleep(3)
  except Exception as e:
    await app.send_message(LOG, f"**ERROR:** `{str(e)}`")
    return
  
app.run(main())
