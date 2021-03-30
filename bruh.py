# bot.py
import os

import discord
from dotenv import load_dotenv

BRUH_CHANNEL = "bruh"

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

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


def valid_bruh(potential_bruh):

	processed_bruh = potential_bruh.replace(" ", "").lower()
	
	valid_bruhs = {"bruh", "brough", "breh", "brih", "broh", ":bruh:", 
		":regional_indicator_b: :regional_indicator_r: :regional_indicator_u: :regional_indicator_h:",
		"브로", "大哥"}

	return processed_bruh in valid_bruhs

@client.event
async def on_message(message):

	if not valid_bruh(message.content) and m.channel == BRUH_CHANNEL: # and in bruh channel
		# redirect to another channel
		# send annoying dm to rule breaker


    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))



client.run(TOKEN)