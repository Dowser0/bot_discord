import discord
import asyncio
import func
from decouple import config
from discord.ext import commands
from time import sleep
from openai_ia import openAIQuery

cor = 0xFF0000
client = discord.Client()
bot = commands.Bot(command_prefix='Dowser')
KEY_DISCORD = config('KEY-DISCORD')

@client.event
async def on_ready():
    print('Bot ON')
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(activity=discord.Game(name="a vida fora"))
@client.event
async def on_message(message) :

    if message.content.lower().startswith('!') and len(message.content.lower().split()) :
        message_ = message.content.lower().split('!')
        q = message.content.split('!')
        print(message_[1])
        channel = message.channel
        
        query = message_[1]
         
        response = openAIQuery(query)
        print(response)
      
        embed = func.create_embed(response,q[1])

        await channel.send(embed=embed)
    
client.run(KEY_DISCORD)