import discord
import os
import logging
from discord.ext import commands
from discord.ext import tasks
from random import randint
from dotenv import load_dotenv
from utils import jskp


load_dotenv(os.getcwd()+"/config.env")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='--', intents=intents)
bot.remove_command('help')
client = discord.Client()
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


initial_cogs = [
    "jishaku",
    "cogs.error_handler",
    "cogs.nhen",
    "cogs.neko",
    "cogs.gelb",
    "cogs.mod_stuff",
    "cogs.help",
    "cogs.etc",
    "cogs.status",
    "cogs.r34"
]

for cog in initial_cogs:
    try:
        bot.load_extension(cog)
        logging.info(f"Successfully loaded {cog}")
    except Exception as e:
        logging.error(f"Failed to load cog {cog}: {e}")

@bot.event
async def on_ready():
    logging.info('Logged in as {0.user}'.format(bot))
    user = bot.get_user(417605262426374166)
    await user.send("yea i started haha lol you already fucking knew")

bot.run(os.getenv("TOKEN"))