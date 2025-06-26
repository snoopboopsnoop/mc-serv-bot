import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands

from mcstatus import JavaServer

load_dotenv()

TOKEN = os.getenv('DISC_BOT_TOKEN')
IP = os.getenv('SERVER_IP')
GUILD_ID = os.getenv('DISC_SERVER_ID')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents = intents)

server=JavaServer.lookup(IP)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"Synced {len(synced)} command(s)")

@bot.tree.command(name="gtnh", description="bobr", guild=discord.Object(id=GUILD_ID))
async def gtnh(interaction: discord.Interaction):
    status = server.status()
    await interaction.response.send_message(f"{status.players.online} player(s) on rn ({round(status.latency, 2)} ms)")

bot.run(TOKEN)