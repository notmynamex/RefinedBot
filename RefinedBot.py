import discord
import os
import logging
from discord.ext import commands
from discord.ext import tasks
from random import randint
from dotenv import load_dotenv
from utils import jskp
from random import getrandbits
from random import choice


load_dotenv(os.getcwd()+"/config.env")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='--', intents=intents)
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

watchlist = [
    "HELO die",
    "notmyname fail at life",
    "notmyname look at hentai",
    "notmyname fail at coding me",
    "sirspam help notmyname",
    "hentai",
    "A certain scientific Railgun",
    "A certain magical Index",
    "a slime do politics"
    "Dimension W",
    "hayasaka be perfect as fuck",
    "astolfo do astolfo things",
    "dead people get sent into elevators",
    "some guy teach magic to a carpet",
    "konosuba season 1 because season 2 was bad",
    "highschool dxd for the 64th time",
    "not hololive",
    "some scottish guy kill a lot of people",
    "berserk 2016",
    "kansen sodom"
]


initial_cogs = [
    "jishaku",
    "cogs.error_handler",
    "cogs.nhen",
    "cogs.neko",
    "cogs.gelb",
    "cogs.mod_stuff",
    "cogs.help",
    "cogs.etc"
]

for cog in initial_cogs:
    try:
        bot.load_extension(cog)
        logging.info(f"Successfully loaded {cog}")
    except Exception as e:
        logging.error(f"Failed to load cog {cog}: {e}")

@tasks.loop(minutes=10)
async def status(self):
    await self.bot.wait_until_ready()
    if getrandbits(1) == 1:
        value = choice(status_list)
        await self.bot.change_presence(activity=discord.Game(name=value))
        logging.info(f"Status set to: {value}")
    else:
        value = choice(watchlist)
        await self.bot.change_presence(activity=discord.Activity(name=value, type=discord.ActivityType.watching))
        logging.info(f"Status set to: {value}")

@bot.event
async def on_ready():
    logging.info('Logged in as {0.user}'.format(bot))
    status.start()

bot.run(os.getenv("TOKEN"))
