import discord
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Enable member intents
intents = discord.Intents.default()
intents.members = True

# Create the bot client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_member_join(member):
    welcome_channel = discord.utils.get(member.guild.text_channels, name="welcome-channel")  # Change this to your welcome channel
    if welcome_channel:
        await welcome_channel.send(f"Welcome to the server, {member.mention}! 🎉")

# Run the bot
client.run(TOKEN)
