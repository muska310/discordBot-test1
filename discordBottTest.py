# ID: 552262976082542596
#Token: NTUyMjYyOTc2MDgyNTQyNTk2.D19CUw.p1x5hgVX1n5JccS_v7rUBNb6WLo
#8
#https://discordapp.com/oauth2/authorize?client_id=552262976082542596&scope=bot&permissions=8
# watch: https://www.youtube.com/watch?v=DHbVpx-IpH8 


import json
import time
import asyncio
import random

from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")

client = Bot(command_prefix = BOT_PREFIX)

@client.event 
async def on_ready():
	await client.change_presence(game=Game(name="with humans"))
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')
	
@client.command(name='8ball', 
		description='Provides an answer to a yes/no question.'
	       	aliases =['eight_ball', 'eightball', '8-ball'],
	       	pass_context = True)
async def eight_ball(context):
	possible_responces = [
		'That is a resounding no',
		'It is not looking likely',
		'Too hard to tell',
		'It is quite possible',
		'Definitely',
	]
	await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command()
async def square(number):
	squared_value = int(number) + int(number)
	await client.say(str(number) + " squared is " + str(squared_value))
		

@client.event
async def on_message(message):
	if message.content.startswith('!hello'):
		await client.sebd_message(message.channel, 'Hi! testBot ready!')
	elif message.content.startswith('!flip):
		flip = random.choice(['Heads', 'Tails'])
		await client.send_message(message.channel, flip)
	elif 

client.run(TOKEN)

