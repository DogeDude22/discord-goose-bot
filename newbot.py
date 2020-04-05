# -*- coding: utf8 -*-
#pylint: disable=unused-variable

#Import all of our libraries
import os
import random
from dotenv import load_dotenv
from discord.ext import commands
import discord
import builtins
import varibles

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
        await ctx.send(random.choice(varibles.hjonks))
 
@bot.command()
async def respond(ctx):
    '''
    I like my custom emojis
    '''
    #Do the response 
    if toggle_commands.responsetoggle == False:
        return
    else:
        await ctx.message.add_reaction(random.choice(varibles.emojis))

@bot.command()
async def MeMe(ctx):
    '''
    Funny goose MeMe
    '''
    if toggle_commands.memetoggle == False:
        return
    else:
        await ctx.send(file=discord.File(random.choice(varibles.memes)))

@bot.command()
async def dadjoke(ctx):
    '''
    I'm not broken, I'm dad
    '''
    if toggle_commands.dadtoggle == False:
        return
    else:
        await ctx.send(random.choice(varibles.dadlist))

bot.run(TOKEN)