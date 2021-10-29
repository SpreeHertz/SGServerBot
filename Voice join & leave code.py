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
