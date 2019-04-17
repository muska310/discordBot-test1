import json
import time
import asyncio
import random

from discord import Game
from discord.ext.commands import Bot

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

TOKEN = read_token()

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
		description='Provides an answer to a yes/no question.',
	       	pass_context = True)
async def eight_ball(context):
	possible_responses = [
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
		await client.send_message(message.channel, 'Hi! testBot ready!')
	elif message.content.startswith('!flip'):
		flip = random.choice(['Heads', 'Tails'])
		await client.send_message(message.channel, flip)
	


client.run(TOKEN)
