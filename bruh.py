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

    valid_bruhs = {"bruh", "brough", "breh", "brih", "broh", "brhu", ":bruh:",
                   ":regional_indicator_b::regional_indicator_r::regional_indicator_u::regional_indicator_h:",
                   "브로", "大哥"}

    return processed_bruh in valid_bruhs

def process_message(message):
    return "Dirty capper <@" + str(message.author.id) + "> sent to the " + BRUH_CHANNEL + " channel:\n\t" + message.content

@client.event
async def on_message(message):
    print('mesage got:', message)
    if message.author == client.user: return
    
    if not valid_bruh(message.content) and message.channel.name == BRUH_CHANNEL:
        category, position = message.channel.category, message.channel.position
        filter_channel = discord.utils.get(message.guild.channels, name=BRUH_FILTER_CHANNEL) or await message.guild.create_text_channel(BRUH_FILTER_CHANNEL, category=category, position=position)
        print(category, filter_channel)


        await filter_channel.send(process_message(message))


        '''
        channels = await message.guild.fetch_channels()
        print(channels, "\n\n")
        print([channel.type for channel in channels])
        textChannelNames = [channel.name for channel in channels if channel.type is discord.ChannelType.text]
        print(textChannelNames)
        if BRUH_FILTER_CHANNEL not in textChannelNames:
            bruhfilterchannel = await message.guild.create_text_channel('shilter')
        else:
            for channel in channels:
                if channel.name == BRUH_FILTER_CHANNEL:
                    bruhfilterchannel = channel
                    break

        await bruhfilterchannel.send(message)
        '''
    

client.run(TOKEN)
