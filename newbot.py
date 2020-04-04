# -*- coding: utf8 -*-
#pylint: disable=unused-variable

#Import all of our 
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord
import builtins

#List of all of our honks
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

#A list of our emojis
emojis = [
    '<:takebell:694682279087439995>',
    '<:goosebadge:694682278613221397>'
]

dadjokeslist = [
    'Today, my son asked "Can I have a book mark?" and I burst into tears. 11 years old and he still doesnt know my name is Brian.',
    'My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right.',
    'I bought some shoes from a drug dealer. I dont know what he laced them with, but I was tripping all day!',
    'Did you know the first French fries werent actually cooked in France? They were cooked in Greece.',
    'If a child refuses to sleep during nap time, are they guilty of resisting a rest?',
    'The secret service isnt allowed to yell '"Get down!"' anymore when the president is about to be attacked. Now they have to yell "Donald, duck!'
]

#Get our bots token from a file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Set our bot's prefix to !
bot = commands.Bot(command_prefix='$')
builtins.bot = bot

import toggle_commands

#Show that we have logged on.
@bot.event
async def on_ready():
    print('Logged on!')

#Create a command
@bot.command()
#Name it honk
async def honk(ctx):
    #Set the !help text
    '''
    Honk! hjonk! HonK!1!11
    '''
    #Say the line
    if toggle_commands.honktoggle == False:
        return
    else:
        await ctx.send(random.choice(hjonks))
 
@bot.command()
async def respond(ctx):
    '''
    I like my custom emojis
    '''
    #Do the response 
    if toggle_commands.responsetoggle == False:
        return
    else:
        await ctx.message.add_reaction(random.choice(emojis))

@bot.command()
async def MeMe(ctx):
    '''
    Funny goose MeMe
    '''
    if toggle_commands.memetoggle == False:
        return
    else:
        await ctx.send(file=discord.File(r'C:\Users\jackk\Downloads\takebell.png'))

@bot.command()
async def dadjoke(ctx):
    '''
    I'm not broken, I'm dad
    '''
    if toggle_commands.dadtoggle
        return
    else:
        await ctx.send(random.choice(dadjokeslist))

bot.run(TOKEN)