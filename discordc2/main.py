import asyncio
from discordc2.discord_bot.bot import c2_instance
from discordc2.cli.cli import start_cli

async def main():
    bot_task = asyncio.create_task(c2_instance.start())

    cli_task = asyncio.create_task(start_cli())

    await asyncio.gather(bot_task, cli_task)

if __name__ == "__main__":
    asyncio.run(main())
