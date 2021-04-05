import discord
import os
import logging
from discord.ext import commands
from discord.ext import tasks
from random import randint
from dotenv import load_dotenv


load_dotenv(os.getcwd()+"/config.env")


bot = commands.Bot(command_prefix='--')
bot.remove_command('help')
client = discord.Client()
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


status_list = [
    "try --mention",
    "fuck everyone who is reading this",
    "you fucking suck",
    "try --help",
    "did you know you suck?",
    "please dont crash me i am friendly bot yes",
    "https://vndb.org/v4037",
    "astolfo best waifu",
    "pew pew you ded now haha",
    "sirspam not gay",
    "please use my commands please im kinda bored please use them"
]


initial_cogs = [
    "jishaku",
    "cogs.error_handler",
    "cogs.nhen",
    "cogs.neko",
    "cogs.gelb",
    "cogs.mod_stuff",
    "cogs.help"
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
    status.start()

@tasks.loop(minutes=10)
async def status():
    await bot.wait_until_ready()
    value = randint(0, len(status_list))
    value = value - 1
    await bot.change_presence(activity=discord.Game(name=status_list[value]))
    logging.info(f"Status set to: {status_list[value]}")

@bot.command()
async def mention(ctx):
    await ctx.send(ctx.author.mention)
    logging.info('oooooh someone got pinged via --mention') #this command is vital trust me


@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping is {round(bot.latency * 1000)}ms')
    logging.info(f'Ping is {round(bot.latency * 1000)}ms')


bot.run(os.getenv("TOKEN"))