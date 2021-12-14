import discord
from discord.ext import commands
import os

token = os.getenv("COLORBOTTOKEN")
client = commands.Bot(command_prefix="c ")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(filename, "cog loaded.")

client.run(token)