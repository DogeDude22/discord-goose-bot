# -*- coding: utf8 -*-

import os
import discord
import random
from dotenv import load_dotenv
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

client = discord.Client()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_member_join(self,member):
        await message.channel.send('Hi' + {member.name} + ', welcome to the soviet union!')


    async def on_message(self,message):
         #don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!honk':
            print('Hi')
            await message.channel.send(random.choice(hjonks))
        
    async def on_message(self,message):
         #don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!motherrussia':
            await message.channel.send('Russia is our sacred power, Russia is our beloved country. Mighty will, great glory - Your possession for all time! Glory to our free Fatherland, The fraternal peoples of the age-old union, The ancestors of this wisdom of the people! Glory to the country! We proud of you! From the southern seas to the polar region Spread our forests and fields. You alone in the world! You are the only one - God?s native land! Glory to our free Fatherland, The fraternal peoples of the age-old union, The ancestors of this wisdom of the people! Glory to the country! We proud of you! Wide scope for dreams and for life The coming years open to us. Our loyalty to the Fatherland gives us strength. So it was, it is, and it always will be! Glory to our free Fatherland, The fraternal peoples of the age-old union, The ancestors of this wisdom of the people! Glory to the country! We proud of you!')
client = MyClient()
client.run(TOKEN)
