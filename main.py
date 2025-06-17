from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import asyncio
import os

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

client = TelegramClient('session', api_id, api_hash)

async def update_time():
    await client.start()
    while True:
        now = datetime.now()
        current_time = now.strftime('%H:%M')
        await client(UpdateProfileRequest(first_name=f"Islombek 🕒 {current_time}"))
        await asyncio.sleep(60 - now.second)

with client:
    client.loop.run_until_complete(update_time())
