import discord
from discord.ext import commands
import time
import asyncio


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

TOKEN = read_token()

client = discord.Client()


@client.event #event decorator/wrapper
async def on_ready():
	print(f"We have loggin in as {client.user}")


@client.event #event decorator/wrapper
async def on_message(message):
	if message.content == "!hello":
		await message.channel.send("Watt up thoo") ## TEST MESSAGE
	elif message.content == "!users":
		await message.channel.send(f"""# of Members: {id.member_count}""")
	elif message.content == "!logout":
		await client.close()
		
	
@client.event #event decorator/wrapper
async def on_member_join(member):
	global joined 
	joined += 1
	for channel in member.server.channels:
		if str(channel) == "general":
				await client.send_message(f"""Welcome to the virgins lair {member.mention} """)

client.run(TOKEN)
