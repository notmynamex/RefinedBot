import discord
from discord.ext import commands
import logging
from jikanpy import Jikan
import requests
#from pyosu import OsuApi

bot = commands.Bot(command_prefix="--")
jikan = Jikan()
#async def main():
#    api = OsuApi("")

class etc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.command()
    async def search(self, ctx, query: str):
        search = jikan.search("anime", query)
        results = search.get("results")
        top = results[0]
        embed = discord.Embed(
            color=0x1f13ee
        )
        embed.set_thumbnail(url=top.get("image_url"))
        embed.add_field(
            name="Title", 
            value=top.get("title"), 
            inline=False
        )
        embed.add_field(
            name="Link", 
            value=f'[MAL]({top.get("url")})', 
            inline=False
        )
        embed.add_field(
            name="Episodes", 
            value=top.get("episodes"), 
            inline=False
        )
        embed.add_field(
            name="Score", 
            value=top.get("score"), 
            inline=False
        )
        embed.add_field(
            name="Episodes",
            value=top.get("episodes"),
            inline=False
        )
        embed.add_field(
            name="Rated",
            value=top.get("rated"),
            inline=False
        )
        embed.add_field(
            name="Type",
            value=top.get("type"),
            inline=False
        )
        embed.add_field(
            name="Synopsis", 
            value=top.get("synopsis"), 
            inline=False
            )
        await ctx.send(embed=embed)

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

    @bot.command()
    async def invite(self, ctx):
        await ctx.send("https://discord.com/oauth2/authorize?client_id=814616270087520316&permissions=59462&scope=bot")

#    @bot.command()
#    async def osu(self, ctx, *, args = None):
#        user = await api.get_user(user = args)
#        if not user:
#            await ctx.send("nothing found you monke")
#            return
#        playcount = str(user.playcount)
#        pp_rank = str(user.pp_rank)
#        accuracy = str(user.accuracy)
#        image = 'http://s.ppy.sh/a/' + str(user.user_id)
#        embed=discord.Embed(
#            title="{}".format(args),
#            description="osu stats for given user",
#            color=0x1f13ee
#        )
#        embed.set_thumbnail(
#            url=image
#        )
#        embed.add_field(
#            name="Playcount:",
#            value=playcount,
#            inline=True 
#        )
#        embed.add_field(
#            name="Rank:",
#            value=pp_rank,
#            inline=True 
#        )
#        embed.add_field(
#            name="Accuracy:",
#            value=accuracy,
#            inline=True
#        )
#        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(etc(bot))
