import discord
from discordc2.config import config
from discordc2.logger.logger import Logger as logger
from discordc2.logger.log_type import Log_Type

class Bot(discord.Client):
    async def on_ready(self):
        logger.log(f'DiscordC2 logged on as {self.user}', Log_Type.INFO)

class C2Bot:
    def __init__(self):
        self.intents = discord.Intents.default()
        self.intents.message_content = True
        self.bot = Bot(intents=self.intents)

    async def start(self):
        await self.bot.start(config.bot_token)

    async def getAllChannels(self):
        channels = []
        for guild in self.bot.guilds:
            if guild.id == config.bot_guild:
                cats = [cat.name for cat in guild.categories]
                for channel in guild.channels:
                    id = channel.id
                    name = channel.name
                    category = channel.category
                    category_id = channel.category_id
                    channel_info = f"| category: {category} ({category_id}) | id: {id} | name: {name} |"
                    if name not in cats:
                        channels.append(channel_info)
        return channels
    
    async def info(self):
        for guild in self.bot.guilds:
            if guild.id == config.bot_guild:
                id = guild.id
                name = guild.name
                owner_name = ""
                owner_id = ""
                members = guild.member_count
                server_info = f"""
SERVER INFORMATION        
 ___________________________
|                           
|  server_id: {id}          
|  server_name: {name}      
|  owner_name: {owner_name} 
|  owner_id: {owner_id}     
|  members: {members}       
|___________________________ 

"""
                return server_info
            
    async def nuke(self):
        for guild in self.bot.guilds:
            if guild.id == config.bot_guild:
                for c in guild.channels:
                    try:
                        logger.log("Deleting... " + c.name, Log_Type.INFO)
                        await c.delete()
                        logger.log("Deleted " + c.name, Log_Type.INFO)
                    except:
                        logger.log("Could not delete " + c.name, Log_Type.WARN)

    async def stop(self):
        await self.bot.close()
    
c2_instance = C2Bot()
