import discord
from discord.ext import commands, tasks
from discord.utils import get
from random import randint

bot = commands.Bot(command_prefix='--')
bot.remove_command('help')
client = discord.Client()

status_list = [
    "try --mention",
    "fuck everyone who is reading this",
    "you fucking suck",
    "try --help",
    "did you know you suck?",
    "please dont crash me i am friendly bot yes",
    "https://vndb.org/v4037",
    "astolfo best waifu",
    "pew pew you ded now haha"
]

initial_cogs = [
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
        print(f"Successfully loaded {cog}")
    except Exception as e:
        print(f"Failed to load cog {cog}: {e}")

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    status.start()

@tasks.loop(minutes=10)
async def status():
    await bot.wait_until_ready()
    value = randint(0, len(status_list))
    value = value - 1
    await bot.change_presence(activity=discord.Game(name=status_list[value]))
    print(f"Status set to: {status_list[value]}")

@bot.command()
async def mention(ctx):
    await ctx.send(ctx.author.mention)
    print('oooooh someone got pinged via --mention') #this command is vital trust me

@bot.command()
async def ping(ctx):
    await ctx.send('uwu your ping is {0}ms senpai uwu'.format(round(bot.latency, 1000)))
    print('Response time: {0}ms'.format(round(bot.latency, 1000)))

@bot.event
async def on_join_guild(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send("Whats up dickheads, --help for help")
        break


bot.run('ODE0NjE2MjcwMDg3NTIwMzE2.YDgchQ.a0O-fbvzjcTvPXLBDK71MAfE8Oo')