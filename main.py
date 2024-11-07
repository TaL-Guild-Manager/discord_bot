import os
import discord

from contracts.constants import Constants
from api.members_api import members, member
from api.raids_api import raids, boss

_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
PREFIX = Constants.BOT_PREFIX

class KumihoClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == client.user:
            return
        
        if message.content.startswith(f"{PREFIX}help"):
            await message.channel.send('\n'.join(Constants.COMMANDS))
    
        if message.content.startswith(f"{PREFIX}up"):
            await message.channel.send("I'M ALIIIIIIIVE ! And Maengdok sucks")

        if message.content.startswith(f"{PREFIX}membres"):
            await members(message)

        if message.content.startswith(f"{PREFIX}membre"):
            await member(message)

        if message.content.startswith(f"{PREFIX}raids"):
            await raids(message)

        if message.content.startswith(f"{PREFIX}boss"):
            await boss(message)

intents = discord.Intents.default()
intents.message_content = True

client = KumihoClient(intents=intents)
client.run(_TOKEN)
