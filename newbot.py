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

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
        print('Logged on!')
@bot.event
#async def on_member_join(self,member):
 #       await message.channel.send('Hi' + {member.name} + ', welcome to the soviet union!')

@bot.command
async def honk(ctx):
    '''
    Honk! hjonk! HonK!1!11
    '''
    #Say the line
    await ctx.send(random.choice(hjonks))
 
        
#async def on_message(self,message):
    #don't respond to ourselves
 #   if message.author == self.user:
  #      return

   # if message.content == '!motherrussia':
    #    await message.channel.send('Russia is our sacred power, Russia is our beloved country. Mighty will, great glory - Your possession for all time! Glory to our free Fatherland, The fraternal peoples of the age-old union, The ancestors of this wisdom of the people! Glory to the country! We proud of you! From the southern seas to the polar region Spread our forests and fields. You alone in the world! You are the only one - God?s native land! Glory to our free Fatherland, The fraternal peoples of the age-old union, The ancestors of this wisdom of the people! Glory to the country! We proud of you! Wide scope for dreams and for life The coming years open to us. Our loyalty to the Fatherland gives us strength. So it was, it is, and it always will be! Glory to our free Fatherland, The fraternal peoples of the age-old union, The ancestors of this wisdom of the people! Glory to the country! We proud of you!')
bot.run(TOKEN)
