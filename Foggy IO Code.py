import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
 
Client = discord.Client ()
client = commands.Bot (command_prefix = "!")

chat_filter = ["FUCK","NIGGA","MOTHERFUCKER","CUNT","NIGGER","BITCH","SHIT"]
bypass_list = []

@client.event
async def on_ready ():
    print ("Bot is online and connected to Discord")
    
@client.event
async def on_message (message) :
    if message.content.upper ().startswith ('!COOKIE'):
 userID = message.author.id
 
    await client.send_message(message.channel, "<@%s> :cookie:" % (userID) )
    if message.content.upper().startswith ('!LOOK'):
        args - message.content.split (" ")
        #args[0] = !LOOK
        #args [1] = :cookie:
        await client.send_message (message.channel, "%s" % (" ".join (args[1:]) ) ) 
        
    


    
@client.event
async def on_message(message):
 contents = message.content.split (" ")#contents is a list type
 for word in contents:
     if word.upper () in chat_filter:
         if not message.author.id in bypass_list:
             await client.delete_message (message)
             await client.send_message (message.channel, "**Hey!** You're not allowed to use that word here.Please avoid it.")


client.run("")

