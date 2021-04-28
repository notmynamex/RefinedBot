import discord
from discord.ext import commands
import rule34
import random
import logging
import asyncio

bot = commands.Bot(command_prefix='--')
rule34 = rule34.Rule34(bot.loop)

class r34(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.command(aliases=["r34"])
    @commands.is_nsfw()
    async def rule34(self, ctx, *, arguments=None):
        if arguments == None:
            logging.info("someone tried to search for nothing lmao")
            return await ctx.send("cant search for nothing dumbass")
        if "loli" in arguments:
            logging.info("another lolicon sent to horny jail")
            return await ctx.send("you can fuck right off back to france, no lolis here")
        async with ctx.typing():
            file = await rule34.getImages(arguments, randomPID=True)
            if not file:
                logging.info("some idiot tried to search but found nothing lmao")
                return await ctx.send("nothing found lmao")
            file = random.choice(file)
            url = file.file_url
            await ctx.send(url)
            logging.info("r34 ran")

def setup(bot):
    bot.add_cog(r34(bot))