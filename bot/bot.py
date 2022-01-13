import os
import discord
from dotenv import load_dotenv
load_dotenv()

class Bot(discord.Client):
    
    async def on_ready(self):
        print(f'{client.user.name} has connected to Discord!')

client = Bot()
client.run(os.getenv('BOT_TOKEN'))

