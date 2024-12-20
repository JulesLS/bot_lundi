#Import all necessary dependencies to make the bot run perfectly
#We import discord, obviously. Time, so the code cazn get the day's date. And then a few other dependencies for the discord roles and such
import discord
import time
from datetime import datetime
import os
from discord.ext import commands
from discord import Client
from discord import guild


#We setup a "default" bot
client = discord.Client(intents=discord.Intents.default())

#Of course the token can't be given here, otherwise anyone would get MY token. 
#The token needs to be accessed form another file, at the beginning of the python code (not done yet)

#token = ""

#Setting a variable name for the bot
new_username = "Bot"

#The role's ID on Discord. You need to find it yourself, I don't remember how I got but I'll update it later
roleID = 572032048726933514

#Getting the date, since the bot is supposed to send messages only on Mondays and Tuesdays
dt = datetime.now()
#print (dt.weekday())


# /!\ Work In Progress : the bot is BROKEN at the moment

#The client.event function checks various events within the Discord client itself.
@client.event

#The following event is triggered once the client is considered "ready"
async def on_ready():

#This is just a print test to see if the bot is connected. Since I launch the code in the background,
#I don't really get the print anymore, but I left it here in case you want to make your own tests
    print('We have logged in as {0.user}'.format(client))

#We set the bot's username to "C lundi". This is a private joke and you should use whatever name you'd like.
    new_username = "C lundi"
    for guild in client.guilds :
        await guild.me.edit(nick=new_username)

#Once again, client.event to open a test
@client.event

#The event is triggered everytime a user sends a message. Far from optimal but this is a harmless Python program,
#and I'm not trying to learn how to optimize Python when C++ exists
async def on_message(msg):

#If the role with this ID is pinged, AND it's Monday, send the following message     
    if "roleID" in msg.content and dt.weekday() == 0:
        await msg.channel.send("C lundi et y a Dofus 3")

#If the role with this ID is pinged, AND it's not Monday, send the following message
    if "roleID" in msg.content and dt.weekday() != 0:
        await msg.channel.send("Y a Dofus 3")


#The command is commented as long as I haven't implementing getting the token from another file.
#See lines 15 to 18
#client.run(token)
