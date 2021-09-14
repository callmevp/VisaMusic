# Copyright (C) 2021 By VisaMusicProject

# ===========
# running VisaMusic
# ===========
import logging
import time
import sys
import asyncio
import glob
import importlib
from pathlib import Path
from pyrogram import Client, idle
from config import Veez 
from VisaMusic.videoplayer import app
from VisaMusic.videoplayer import call_py
from helpers.loggings import LOG
 
    
VisaMusic = Client(
    ":memory:",
    Visa.API_ID,
    Visa.API_HASH,
    bot_token=Visa.BOT_TOKEN,
    plugins=dict(root="VisaMusic"),
)

StartTime = time.time()

loop = asyncio.get_event_loop()

_path = f"VisaMusic/*.py"
files = glob.glob(_path)

def load_plugins(plugin_name):
    path = Path(f"VisaMusic/{plugin_name}.py")
    name = "VisaMusic.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(load)
    sys.modules[f"VisaMusic." + plugin_name] = load
    print("Imported => " + plugin_name)

async def start():
    print('\n')
    print('------------------ Initalizing VISA --------------------')
    if VisaMusic:
        await VisaMusic.start()
    await app.start()
    await call_py.start()
    print('------------------------ DONE --------------------------')
    print('------------------ Importing Modules -------------------')
    for name in files:
        with open(name) as a:
            path_ = Path(a.name)
            plugin_name = path_.stem
            load_plugins(plugin_name.replace(".py", ""))
    print('------------------- INITIATED VISA ---------------------')
    print('     Logged in as User =>> {}'.format((await app.get_me()).first_name))
    if VisaMusic:
        print('     Logged in to Bots =>> {}'.format((await VisaMusic.get_me()).first_name))
    print('--------------------------------------------------------')
    await idle()
if __name__ == '__main__':
    is_VisaMusic = bool(Visa.BOT_TOKEN)
    loop.run_until_complete(start())


# VisaMusic.start()
# print("[STATUS]:✅ »» BOT CLIENT STARTED ««")
# app.start()
# print("[STATUS]:✅ »» USERBOT CLIENT STARTED ««")
# call_py.start()
# print("[STATUS]:✅ »» PYTGCALLS CLIENT STARTED ««")
# idle()
# print("[STATUS]:❌ »» BOT STOPPED ««")
