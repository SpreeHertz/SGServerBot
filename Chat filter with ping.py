import discord
from discord.ext import commands
import asyncio
import time

TOKEN = ''

client = commands.Bot (command_prefix = '%')

chat_filter = ["FUCK","NIGGA","MOTHERFUCKER","CUNT","NIGGER","BITCH","SHIT","DICK","RAPE","FUCKING PIECE OF SHIT","FUCKING","COCKSUKER","COCKSUCKA"]
bypass_list = []


@client.event
async def on_ready ():
    await client.change_presence(game=discord.Game(name='Prefix = %'))
    print ('Bot is ready.')

@client.command
async def ping():
    await client.say('Pong!')
        
@client.command(pass_context=True)
async def clear(ctx,amount=100):
    channel = ctx.message.channel
    messgaes = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
        await client.delete_messages(messages)
        await client.say('Messages deleted.')
        
@client.event
async def on_message(warn):
 contents = message.content.split (" ")#contents is a list type
 for word in contents:
     if word.upper () in chat_filter:
         if not message.author.id in bypass_list:
             await client.delete_message (message)
             await client.send_message (message.channel, "**Hey!** You're not allowed to use that word here. Please avoid it.")

             
       




client.run(TOKEN)

