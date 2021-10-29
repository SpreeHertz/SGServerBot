import discord
from discord.ext import commands
import asyncio
import youtube_dl


TOKEN = ''
players = {}



client = commands.Bot (command_prefix = '%')

@client.event
async def on_ready ():
    await client.change_presence(game=discord.Game(name='Beep Boop'))
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


        
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    await client.say('I have joined your voice channel.')

@client.command(pass_context=True)
async def leave(ctx):
 server = ctx.message.server
 voice_client = client.voice_client_in(server)
 await voice_client.disconnect()
 await client.say('I have left your voice channel.')

@client.command(pass_context=True)
async def play(ctx,url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = players
    
def func():
    player = "ID"
    players[0] = player
    player.start()
    
@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    await client.say('Paused audio.')

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    await client.say('Audio stopped.')

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    await client.say('Audio resumed.')


                
client.run(TOKEN)


