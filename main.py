import os
from pyrogram import Client, filters, enums
from pyrogram.types import Message
import asyncio
import logging
import sys
import time
from random import choice
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
STRING_SESSION = os.environ.get("STRING_SESSION")
CMD = "."
BOTT = "chatbot"

LOOP = asyncio.get_event_loop()

app = Client(name="bot5",
             api_id=API_ID,
             api_hash=API_HASH,
             session_string=STRING_SESSION,
            )
            
async def main():
  await app.start()
  gua = await app.get_me()
  await app.send_message(BOTT, "/next")
  await asyncio.sleep(6)
  await app.send_message(BOTT, f"**halo aku {gua.mention} mau ngasih tau kalau kamu sekarang bisa cari pacar di** @pintarbot\n\n**LINK:** @pintarbot\n\n**Kalau gabisa di klik salin** `@pintarbot` **taro di menu search**")
  await asyncio.sleep(6)
  await app.send_message(BOTT, "/next")
  
if __name__ == "__main__":
    LOOP.run_until_complete(main())
