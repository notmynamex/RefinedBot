import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='--')
bot.remove_command('help')
client = discord.Client()

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

@bot.command()
async def mention(ctx):
    await ctx.send(ctx.author.mention)
    print('oooooh someone got pinged via --mention') #this command is vital trust me

@bot.command()
async def ping(ctx):
    await ctx.send('uwu your ping is {0}ms senpai uwu'.format(round(bot.latency, 1)))
    print('Response time: {0}ms'.format(round(bot.latency, 1)))

bot.run('ODE0NjE2MjcwMDg3NTIwMzE2.YDgchQ.a0O-fbvzjcTvPXLBDK71MAfE8Oo')