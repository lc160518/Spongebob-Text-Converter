# bot.py
import os

import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
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

    if message.content.startswith("!sb"):
        l = list(message.content)
        world_list = remove_prefix(l)

        b = spongeefy(world_list)
        await message.channel.send(listToString(b))

        if not isinstance(message.channel, discord.DMChannel):
            await message.delete()


def remove_prefix(prefix):
    for i in range(0, 4):
        prefix.remove(prefix[0])
    return (prefix)


def spongeefy(words):
    counter = 1

    while counter <= (len(words) - 1):
        words[counter] = words[counter].upper()
        counter += 2
    return (words)


def listToString(words):
    # initialize an empty string
    str1 = ""

    # return string
    return (str1.join(words))


client.run(TOKEN)
