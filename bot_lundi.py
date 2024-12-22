#Import all necessary dependencies to make the bot run perfectly
#We import discord, obviously. Time, so the code cazn get the day's date. And then a few other dependencies for the discord roles and such
from email import message
import token
import discord
import time
from datetime import datetime
import os
from discord.ext import commands
from discord import Client
from discord import guild
#Here we set the intents of the bot. 
#It is CRUCIAL to set "intents.message_content" to True. 
#Otherwise the bot won't be able to interact with the content of a message and react according to what a message contains
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#We created a file containing the secret values, so I can make this project entirely public without risk. For more info, refer to the README file.
from secret_values import *
import secret_values

#Of course the token can't be given here, otherwise anyone would get MY token. 
#The token needs to be accessed form another file, at the beginning of the python code (not done yet)
token = secret_values.discord_token
print(token)

#Setting a variable name for the bot
new_username = "Bot"

#The role's ID on Discord. 
#To find the ID of the role you want to interact with, go in the server settings section, go to the desired role and click the 3 dots
#Then copy the role ID and store it somewhere
#secret_values.tester_role_ID
#secret_values.lol_role_ID
roleID = secret_values.tester_role_ID

#Getting the date, since the bot is supposed to send messages only on Mondays and Tuesdays
dt = datetime.now()
#print (dt.weekday())


# /!\ Work In Progress : the bot works but I need to set the day conditions now

#The client.event function checks various events within the Discord client itself.
@client.event
#The following event is triggered once the client is considered "ready"
async def on_ready():
#This is just a print test to see if the bot is connected. Since I launch the code in the background,
#I don't really get the print anymore, but I left it here in case you want to make your own tests
    print('We have logged in as {0.user}'.format(client))


#Once again, client.event to open a test
@client.event

#The event is triggered everytime a user sends a message. Far from optimal but this is a harmless Python program,
#and I'm not trying to learn how to optimize Python when C++ exists
async def on_message(message):
    #This test works. The bot simply fails to detect keywords so far
    print("message détecté")

#If the role with this ID is pinged, AND it's Monday, send the following message     
    #if "roleID" in msg.content and dt.weekday() == 0:
        #await msg.channel.send("C lundi et y a Dofus 3")

#If the role with this ID is pinged, AND it's not Monday, send the following message
    print("hehe")
    if message.content == "caca":
        print("caca détecté")
        await message.channel.send("Y a Dofus 3")


##The command is commented as long as I haven't implementing getting the token from another file.
##See lines 15 to 18
client.run(token)
