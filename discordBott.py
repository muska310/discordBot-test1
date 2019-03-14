# ID: 552262976082542596
#Token: NTUyMjYyOTc2MDgyNTQyNTk2.D19CUw.p1x5hgVX1n5JccS_v7rUBNb6WLo
#8
#https://discordapp.com/oauth2/authorize?client_id=552262976082542596&scope=bot&permissions=8

import discord
import time
import asyncio

messages = joined = 0

def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

TOKEN = read_token()

client = discord.Client()

#async def update_stats():
#	await client.wait_until_ready()
#	global messages, joined
#	
#	while not client.is_closed():
#		try:
#			with open("stats.txt","a") as f:
#				f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n ")
#			
#			messages = 0
#			joined = 0
#			
#			await  asyncio.sleep(1800) ##SYNCING EVERY 30 MINS
#		except Exception as e:
#			print(e)


@client.event #event decorator/wrapper
async def on_ready():
	print(f"We have loggin in as {client.user}")



@client.event #event decorator/wrapper
async def on_member_join(member):
	global joined 
	joined += 1
	for channel in member.server.channels:
		if str(channel) == "general":
				await client.send_message(f"""Welcome to the virgins lair {member.mention} """)


@client.event #event decorator/wrapper
async def on_message(message):
	global messages
	messages += 1

	id = client.get_guild(555107550350278678)
	channels = ["commands"]
	
	if str(message.channel) in channels:
		if message.content.find("!hello") != -1:
			await message.channel.send("Watt up thoo") ## TEST MESSAGE

		elif message.content == "!users":
			await message.channel.send(f"""# of Members: {id.member_count}""")
		
		elif message.content == "!logout":
			await client.close()

#client.loop.create_task(update_stats())
client.run(TOKEN)

