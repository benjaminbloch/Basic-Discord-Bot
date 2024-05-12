

# Import modules

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import requests
import time
import json
import random

#Enter your discord bot token & Prefix here
TOKEN = ''
prefix = "!"

#define your client
client = Bot(command_prefix=prefix)

# if you want to remove the deafult HELP command
client.remove_command('help')


#Its a event which will run when the bot is ready/online.
@client.event
async def on_ready():
    print("Logged in as " + client.user.name)
    print("I'm ready")

#Here you can add your cmds


@client.command(pass_context=True)
async def start(ctx):
    await client.say(f"Hello {ctx.message.author.mention}, welcome the exotic self service panel. If you are ready, please run !ready command.")

@client.command(pass_context=True)
async def ready(ctx):
    await client.say(f"1. What Are You Doing. Please Run !roles command if you are wanting to claim roles. Please run !purchase command if yoou want to buy.")

@client.command(pass_context=True)
async def purchase(ctx):
    await client.say(f"2. Commands: ```!socials - followers, likes ext``` ```!tokens - discord tokens``` ```!vip - get access to loads of  methods```")

@client.command(pass_context=True)
async def purchase(ctx):
    await client.say(f"1. What Are You Doing. Please Run !roles command if you are wanting to claim roles. Please run !purchase command if yoou want to buy.")

@client.command(pass_context=True)
async def roles(ctx):
    await client.say(f"2. To claim youtube subscriber role please run !sub. to do staff aplication please run !staff. To claim status/roles from outher server run !claim")

@client.command(pass_context=True)
async def claim(ctx):
    await client.say(f"3. Ok. Please wait for someone to assist you!")
    time.sleep(1)
    await client.say(f"<@1239162968780836906>")
    await client.say(f"/b0tlock")

@client.command(pass_context=True)
async def socials(ctx):
    await client.say(f"3. Ok. Please wait for someone to assist you!")
    time.sleep(1)
    await client.say(f"<@1239170316270567524>")
    await client.say(f"/b0tlock")

@client.command(pass_context=True)
async def vip(ctx):
    await client.say(f"3. Ok. Please wait for someone to assist you!")
    time.sleep(1)
    await client.say(f"<@1239170813773746247>")
    await client.say(f"/b0tlock")

@client.command(pass_context=True)
async def tokens(ctx):
    await client.say(f"3. Ok. Please wait for someone to assist you!")
    time.sleep(1)
    await client.say(f"<@1239170961287286834>")
    await client.say(f"/b0tlock")

@client.command(pass_context=True)
async def sub(ctx):
    await client.say(f"3. Ok. Please wait for someone to assist you!")
    time.sleep(1)
    await client.say(f"<@1239163603010064474>")
    await client.say(f"/b0tlock")

@client.command(pass_context=True)
async def sub(ctx):
    await client.say(f"3. Ok. Please wait for someone to assist you!")
    time.sleep(1)
    await client.say(f"<@1239164307896537189>")
    await client.say(f"/b0tlock")

#get info of server
@client.command(pass_context=True)
async def serverinfo(ctx):
    
    embed = discord.Embed(name=f"{ctx.message.server.name}'s info".format, color=0x00ff00)
    embed.set_author(name="Server Info")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.set_footer(text="Basic example of embed message!")
    
    await client.say(embed=embed)
    


# get info of any user
@client.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    
    embed = discord.Embed(title=f"{user.name}'s Info",color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined At", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text="Basic example of embed message!")
    
    await client.say(embed=embed)


#get avatar of any user
@client.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    
    embed=discord.Embed(title=f"Avater of {user}", color=0x1500ff)
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text="Basic example of embed message!")
                     
    await client.say(embed=embed)
    
# Run the bot with the token
client.run(TOKEN)
