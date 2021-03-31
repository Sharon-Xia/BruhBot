# bot.py
import os

import discord
from dotenv import load_dotenv

BRUH_CHANNEL = "bruh"
BRUH_FILTER_CHANNEL = "shilter"

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


def valid_bruh(potential_bruh):

    processed_bruh = potential_bruh.replace(" ", "").lower()

    bruhset = {"b", "r", "u", "h"}

    valid_bruhs = {"brough", "breh", "brih", "broh", ":bruh:",
                   ":regional_indicator_b::regional_indicator_r::regional_indicator_u::regional_indicator_h:",
                   "브로", "大哥"}

    print("\nprocessed bruh: '" + processed_bruh + "'\n")

    return processed_bruh in valid_bruhs or set(processed_bruh) == bruhset


async def process_and_send_message(channel, message):
    msgtext = "<@{0}> `sent to the {1} channel:`\n{2}".format(
        str(message.author.id),
        BRUH_CHANNEL,
        ">>> " + message.content if message.content else "")
    files = [await attachment.to_file() for attachment in message.attachments]
    await channel.send(msgtext, files=files)


@client.event
async def on_message(message):
    # https://discordpy.readthedocs.io/en/latest/faq.html#why-does-on-message-make-my-commands-stop-working
    # await client.process_commands(message)

    print('message got:', message)
    if message.author == client.user: return
    
    # need to redo valid_bruh to check for emotes since disc doesn't process them as raw text
    if not valid_bruh(message.content) and message.channel.name == BRUH_CHANNEL:
        category, position = message.channel.category, message.channel.position
        filter_channel = discord.utils.get(message.guild.channels, name=BRUH_FILTER_CHANNEL) or await message.guild.create_text_channel(BRUH_FILTER_CHANNEL, category=category, position=position)
        print(category, filter_channel)

        await process_and_send_message(filter_channel, message)
        await message.delete()
    

client.run(TOKEN)