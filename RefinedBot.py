import discord
import os
import logging
from discord.ext import commands
from discord.ext import tasks
from random import randint
from dotenv import load_dotenv
from utils import jskp
import firebase_admin
from firebase_admin import credentials, initialize_app


load_dotenv(os.getcwd()+"/config.env")

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "refinedbot-4db25",
    "private_key_id": "611bc81b6a22096b5cbd10b720340402365b20b0",
    "private_key": os.getenv("PRIVATE_KEY").replace("\\n", "\n"),
    "client_email": "firebase-adminsdk-s8iq9@refinedbot-4db25.iam.gserviceaccount.com",
    "client_id": "105407746496700508972",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-s8iq9%40refinedbot-4db25.iam.gserviceaccount.com"
})
default_app = initialize_app(cred)


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
    "cogs.r34",
    "cogs.reminder",
    "cogs.reminder2"
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
    #user2 = bot.get_user(257586333491527682)
    await user.send("yea i started haha lol you already fucking knew")
    #await user2.send("daily reminder that futa is gay and you're a fucking bitch to believe it isnt")

bot.run(os.getenv("TOKEN"))