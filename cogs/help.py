import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='--')
bot.remove_command('help')

class helpClient(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.group(invoke_without_command=True)
    async def help(self, ctx):
        embed = discord.Embed(
            title="Help",
            description="Info: arg is an optional argument.",
            color=0x1f13ee
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/814616270087520316/f81351b151c5fcb6b382ffcaf4124b06.png?size=4096")
        embed.add_field(
            name="--help neko",
            value="Show commands and subcommands for neko",
            inline=False
        )
        embed.add_field(
            name="--help gelbooru",
            value="Show commands and subcommands for gelbooru",
            inline=False
        )
        embed.add_field(
            name="--ping", 
            value="Show latency", 
            inline=False
        )
        embed.add_field(
            name="--nhentai/--nh <arg>",
            value="Posts a random doujin or fetches a certain doujin if an ID is provided. Only works in NSFW channels",
            inline=False
        )
        await ctx.send(embed=embed)
        print('help embed sent')

    @help.command()
    async def neko(self, ctx):
        embed = discord.Embed(
            title="Help for Neko",
            description="These are the valid arguments for --neko",
            colour=0x1f13ee
        )
        #embed.set_thumbnail(url="https://i.imgur.com/7Whb3qK.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/754643335511015505/810691863610523668/unknown.png")
        embed.add_field(
            name="--neko",
            value="Posts an image of a neko",
            inline=False
        )
        embed.add_field(
            name="--neko gif",
            value="Posts a gif of a neko",
            inline=False
        )
        embed.add_field(
            name="--neko lewd",
            value="Posts a lewd image of a neko. Only works in an NSFW channel",
            inline=False
        )
        embed.add_field(
            name="--neko lewd gif",
            value="Posts a lewd gif of a neko. Only works in an NSFW channel",
            inline=False
        )
        await ctx.send(embed=embed)
        print('neko help embed sent')

    @help.command()
    async def gelbooru(self, ctx):
        embed=discord.Embed(
            title="Help for Gelbooru",
            description="These are the valid commands for --gelbooru",
            colour=0x1f13ee
        )
        embed.set_thumbnail(url="https://i.imgur.com/PcRxTmE.png")
        embed.add_field(
            name="--gelb rs <arg>",
            value="Posts a safe for work image in any channel, add tags as args to search for specific...tags.",
            inline=False
        )
        embed.add_field(
            name="--gelb rq <arg>",
            value="Posts a questionable image in any nsfw channel, add tags as args to search for specific...tags.",
            inline=False
        )
        embed.add_field(
            name="--gelb re <arg>",
            value="Posts an explicit image in any nsfw channel, add tags as args to search for specific...tags.",
            inline=False
        )
        await ctx.send(embed=embed)
        print('gelbooru help embed sent')

def setup(bot):
    bot.add_cog(helpClient(bot))