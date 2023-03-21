# bot.py
import os
import random

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

    users = []

    whitelist = [659666664346091530, 398769543482179585]
    for i in range(0, len(whitelist)):
        users.append(await client.fetch_user(whitelist[i]))

    if client.user == message.author:
        return

    if message.content.startswith("!sb"):
        l = list(message.content)
        world_list = remove_prefix(l)

        b = spongeefy(world_list)
        await message.channel.send(listToString(b))

        if not isinstance(message.channel, discord.DMChannel):
            await message.delete()

    if message.content.startswith("ratio") and message.content.endswith("ratio"):
        await message.channel.send(f"+ {pickratio(message, r)}")

    if message.content.startswith("!suggest"):
        julian = await client.fetch_user(398769543482179585)
        await julian.send(message.content)

    if message.content.startswith("!list"):
        await message.channel.send(f"{r}")

    if message.content.startswith("!add") and message.author in users:
        r = get_list(message)
        r.append(remove_suggest(message))
        await message.channel.send(f"added")


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


def remove_suggest(m):
    g = list(m.content)
    for i in range(0, 5):
        g.remove(g[0])
    return listToString(g)

def get_list(m):
    return ["bozo", "touch grass", "go outside", "get real", "we do a little trolling", "counter ratio", "10.20.11.123",
         "boom beach lvl 100", f"common {m.author.name} W", "gangnam style", "¿Donde esta la biblioteca?"]

def pickratio(m, r):
    x = random.randrange(len(r))
    return r[x]


client.run(TOKEN)
