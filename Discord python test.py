import discord
import logging

logging.basicConfig(level=logging.INFO)

client = discord.Client()

lyrics = ["we're no strangers to love",
"you know the rules and so do I",
"a full commitment's what I'm thinking of",
"you wouldn't get this from any other guy",
"I just wanna tell you how I'm feeling",
"gotta make you understand",
"never gonna give you up",
"never gonna let you down",
"never gonna run around and desert you",
"never gonna make you cry",
"never gonna say goodbye", 
"never gonna tell a lie and hurt you", 
"we've known each other for so long", 
"your heart's been aching, but you're too shy to say it", 
"inside, we both know what's been going on", 
"we know the game and we're gonna play it", 
"and if you ask me how I'm feeling", 
"don't tell me you're too blind to see", 
"never gonna give you up"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content
    if str(message.content) in lyrics:
        location = lyrics.index(message.content)
        await message.channel.send(lyrics[location+1])


client.run('ODc1NTMzMDkyMDUwMzE3MzQy.YRW5uw.9iYHImKJPnOr7nzAmY9Zi58wv5Y')
