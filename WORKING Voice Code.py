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
    player.start()
    
def func():
    player = "ID"
    players[0] = player
    
    
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
