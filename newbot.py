# -*- coding: utf8 -*-

import os
import random
from dotenv import load_dotenv
from discord.ext import commands
hjonks = [
    'HONK',
    'honk',
    'hjonk',
    'HJONK',
    'hONk',
    'HonK',
    'hONK',
    'HoNk',
    'hOnK',
    'Honk'
    ]

emojis = [
    '<:takebell:694682279087439995>',
    '<:goosebadge:694682278613221397>'
]

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

#Show that we have logged on.S
@bot.event
async def on_ready():
    print('Logged on!')

@bot.event
async def on_member_join(self, member):
    await message.channel.send('Hi' + {member.name} + ', welcome to the soviet union!')

@bot.command()
async def honk(ctx):
    '''
    Honk! hjonk! HonK!1!11
    '''
    #Say the line
    await ctx.send(random.choice(hjonks))
 
@bot.command()
async def respond(ctx):
    '''
    I like my custom emojis
    '''
    #Do the response
    await ctx.message.add_reaction(random.choice(emojis))
    

        
bot.run(TOKEN)
