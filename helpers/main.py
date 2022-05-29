from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls, idle

bot = Client(
    "Love",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "Love.Plugins"},
    )

Plincy = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    
    )

user = PyTgCalls(Plincy,
    cache_duration=100,
    overload_quiet_mode=True,)

call_py = PyTgCalls(Plincy, overload_quiet_mode=True)

with Client("Love", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with plincy as app:
    me_plincy = app.get_me()
