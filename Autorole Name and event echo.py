import discord
from discord.ext import commands
import asyncio

TOKEN = ''
players = {}



client = commands.Bot (command_prefix = '%')

chat_filter = ["FUCK","NIGGA","MOTHERFUCKER","CUNT","NIGGER","BITCH","SHIT","DICK","RAPE","FUCKING PIECE OF SHIT","FUCKING","COCKSUKER","COCKSUCKA"]
bypass_list = []

@client.event
async def on_ready ():
    await client.change_presence(game=discord.Game(name='with Legos!'))
    print ('Bot is ready.')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member,server.roles, name = 'Good')
    await client.add_roles(member, role)

@client.event
async def on_message(message):
    await client.process_commands(message)
    channel = message.channel
    if message.content.startswith('%ping'):
        await client.send_message(channel,'Pong!')

@client.event
async def on_message(message):
    if message.content == "%cookie":
        await client.send_message(message.channel, ":cookie:")        

@client.command(pass_context=True)
async def clear(ctx,amount=100):
    channel = ctx.message.channel
    messgaes = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
        await client.delete_messages(messages)
        await client.say('Messages deleted.')        

@client.event
async def on_message(message):
 contents = message.content.split (" ")#contents is a list type
 for word in contents:
     if word.upper () in chat_filter:
         if not message.author.mention in bypass_list:
             await client.delete_message (message)
             await client.send_message (message.channel, "**Hey!**You're not allowed to use that word here. Please avoid it.")

             



             
client.run(TOKEN)


