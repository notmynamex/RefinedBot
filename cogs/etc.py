import discord
from discord.ext import commands
from mal import AnimeSearch
import logging
import requestss

bot = commands.Bot(command_prefix="--")

class etc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.command()
    async def search(self, ctx, arg=None):
        search = AnimeSearch(arg)
        logging.info("MAL search ran")
        return await ctx.send(search.results[0].url)

    @bot.command()
    async def mention(self, ctx):
        await ctx.send(ctx.author.mention)
        logging.info('oooooh someone got pinged via --mention') #this command is vital trust me


    @bot.command()
    async def ping(self, ctx):
        await ctx.send(f'uwu your ping is {round(bot.latency * 1000)}ms senpai uwu')
        logging.info(f'Ping is {round(bot.latency * 1000)}ms')


    @bot.command(aliases=["cabbie"])
    async def cabbage(self, ctx):
        await ctx.send("<@!539885184301137920>")
        logging.info('cabbo ping hehe')

    @bot.command()
    async def avatar(self, ctx, *, avamember: discord.Member):
        userAvatarUrl= avamember.avatar_url
        await ctx.send(userAvatarUrl)
        logging.info('avatar command ran ye')

def setup(bot):
    bot.add_cog(etc(bot))