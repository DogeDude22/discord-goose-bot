from discord.ext import commands
from builtins import bot

honktoggle = True
responsetoggle = True
memetoggle = True
dadtoggle = True

@bot.group()
async def toggle(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("I can't toggle that!")

@toggle.command()
async def h(ctx):
    '''
    Toggles the $honk command
    '''
    global honktoggle
    if honktoggle == True:
        honktoggle = not honktoggle
        await ctx.send("Toggled OFF $honk command")
        return
    if honktoggle == False:
        honktoggle = not honktoggle
        await ctx.send("Toggled ON $honk command")
        return

@toggle.command()
async def r(ctx):
    '''
    Toggles the $response command
    '''
    global responsetoggle
    if responsetoggle == True:
        responsetoggle = not responsetoggle
        await ctx.send("Toggled OFF $response command")
        return
    if responsetoggle == False:
        responsetoggle = not responsetoggle
        await ctx.send("Toggled ON $response command")
        return

@toggle.command()
async def m(ctx):
    '''
    Toggles the $MeMe command
    '''
    global memetoggle
    if memetoggle == True:
        memetoggle = not memetoggle
        await ctx.send("Toggled OFF $MeMe command")
        return
    if memetoggle == False:
        memetoggle = not memetoggle
        await ctx.send("Toggled ON $MeMe command")
        return

@toggle.command()
async def d(ctx):
    '''
    Toggles the $dadjoke command
    '''
    global dadtoggle
    if dadtoggle == True:
        dadtoggle = not dadtoggle
        await ctx.send("Toggled OFF $dadjoke command")
        return
    if dadtoggle == False:
        dadtoggle = not dadtoggle
        await ctx.send("Toggled ON $dadjoke command")
        return