import discord
import time
from datetime import datetime
import os
from discord.ext import commands
from discord import Client
from discord import guild

client = discord.Client(intents=discord.Intents.default())

#token = ""
new_username = "Bot"
LOLCMIEU = 572032048726933514

dt = datetime.now()
#print (dt.weekday())



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #if 0 <= dt.weekday() <= 6:
    new_username = "C lundi"
    for guild in client.guilds :
        await guild.me.edit(nick=new_username)
    #else:
    #    if dt.weekday() == 1:
    #        new_username = "C mardi"
    #        for guild in client.guilds :
    #            await guild.me.edit(nick=new_username)

@client.event
async def on_message(msg):
    if "572032048726933514" in msg.content and dt.weekday() == 0:
        await msg.channel.send("C lundi et y a Dofus 3")
    if "572032048726933514" in msg.content and dt.weekday() != 0:
        await msg.channel.send("Y a Dofus 3")

#    else:
#        if "572032048726933514" in msg.content and dt.weekday() == 1:
#            await msg.channel.send("Y a raid")

#
#    else:
#        if "572032048726933514" in msg.content and dt.weekday() != 0:
#            await msg.channel.send("Y a Dofus 3")

#client.run(token)
