import discord
import aiohttp
import io
import json
from discord.ext import commands

bot = commands.Bot(command_prefix='--')

async def image(link):
    print(f"image function ran with {link}")
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            json_data = json.loads(await resp.text())
            async with session.get(json_data["url"]) as resp:
                return io.BytesIO(await resp.read())

class neko(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.group(invoke_without_command=True)
    async def neko(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/neko"), "neko.png")) #also vital

    @neko.command()
    async def gif(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/ngif"), "neko.gif")) #def vital, without the bot wont run correctly

    @bot.command()
    async def fox(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/fox_girl"), "fox.png")) #also vital please believe me thanks

    @neko.group(invoke_without_command=True)
    async def lewd(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/lewd"), "neko_lewd.png")) #equally as vital
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @lewd.command(aliases=["gif"])
    async def lewd_gif(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/nsfw_neko_gif"), "neko_lewd_gif.gif")) #this too
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')


def setup(bot):
    bot.add_cog(neko(bot))