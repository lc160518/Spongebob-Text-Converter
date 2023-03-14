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

    if client.user == message.author:
        return

    if message.content.startswith("spongefy"):
        l = list(message.content)
        for i in range(0,8):
            del l[i]
        print(l)


words = "beeueyeye"


def spongefy(words):
    x = list(words)
    print(x)

spongefy(words)

client.run(TOKEN)
