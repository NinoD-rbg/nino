import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
from asyncio import sleep
#import utils.json
#from utils.document import document



load_dotenv()

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
  print("Bot connected")

client.run(os.getenv("DISCORD_TOKEN"))