# bot.py
import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} im in')


@client.event
async def on_message(message):
    message.content = message.content.lower()

    gameing = await client.fetch_guild(698997198221738067)
    test_server = await client.fetch_guild(1065705816105160704)

    if client.user == message.author:
        return




client.run(TOKEN)
