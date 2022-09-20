import os
from pyrogram import Client, filters, enums
from pyrogram.types import Message
import asyncio
from threading import Event

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
SPAM_COUNT = [0]

def increment_spam_count():
    SPAM_COUNT[0] += 1
    return spam_allowed()


def spam_allowed():
    return SPAM_COUNT[0] < 50

async def main():
  await app.start()
  gua = await app.get_me()
  delay = 6
  count = 10
  delaySpamEvent = Event()
  if count != 0:
    delaySpamEvent.wait(delay)
    await app.send_message(BOTT, "HAI ANJ")
    limit = increment_spam_count()
  
if __name__ == "__main__":
    LOOP.run_until_complete(main())
