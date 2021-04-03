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

    @bot.group(invoke_without_command=True)
    @commands.is_nsfw()
    async def feet(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/feet"), "feet.png"))

    @bot.command()
    @commands.is_nsfw()
    async def yuri(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/yuri"), "yuri.png"))

    @bot.command()
    @commands.is_nsfw()
    async def futa(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/futanari"), "futa.png"))

    @bot.command()
    @commands.is_nsfw()
    async def lewdkemo(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/lewdkemo"), "lewdkemo.png"))

    @feet.command(aliases=["gif"])
    @commands.is_nsfw()
    async def feet_gif(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/feetg"), "feet.gif"))

    @bot.group(invoke_without_command=True)
    @commands.is_nsfw()
    async def cum(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/cum"), "cum.gif"))

    @bot.command()
    @commands.is_nsfw()
    async def erokemo(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/erokemo"), "erokemo.png"))

    @bot.command()
    @commands.is_nsfw()
    async def les(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/les"), "les.gif"))

    @bot.command()
    @commands.is_nsfw()
    async def lewdfox(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/lewdk"), "lewdk.png"))

    @bot.command()
    @commands.is_nsfw()
    async def eroyuri(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/eroyuri"), "eroyuri.png"))

    @bot.command()
    @commands.is_nsfw()
    async def eron(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/eron"), "eron.png"))

    @cum.command(aliases=["jpg"])
    @commands.is_nsfw()
    async def cum_jpg(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/cum_jpg"), "cum.jpg"))

    @bot.command()
    @commands.is_nsfw()
    async def bj(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/bj"), "bj.gif"))

    @bot.command()
    @commands.is_nsfw()
    async def solo(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/solo"), "solo.png"))

    @bot.command()
    async def kemo(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/kemonomimi"), "kemonomimi.png"))

    @bot.command()
    @commands.is_nsfw()
    async def nsfw_avatar(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/nsfw_avatar"), "nsfw_avatar.png"))

    @bot.command()
    @commands.is_nsfw()
    async def anal(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/anal"), "anal.gif"))

    @bot.command()
    @commands.is_nsfw()
    async def hentai(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/hentai"), "hentai.png"))

    @bot.command()
    @commands.is_nsfw()
    async def erofeet(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/erofeet"), "erofeet.png"))

    @bot.command()
    @commands.is_nsfw()
    async def keta(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/keta"), "keta.png"))

    @bot.command()
    @commands.is_nsfw()
    async def blowjob(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/blowjob"), "blowjob.png"))

    @bot.group(invoke_without_command=True)
    @commands.is_nsfw()
    async def pussy(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/pussy"), "pussy.gif"))

    @bot.command()
    @commands.is_nsfw()
    async def tits(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/tits"), "tits.png"))

    @bot.command()
    async def lizard(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/lizard"), "lizard.png"))

    @pussy.command(aliases=["jpg"])
    @commands.is_nsfw()
    async def pussy_jpg(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/pussy_jpg"), "pussy.jpg"))

    @bot.command()
    @commands.is_nsfw()
    async def pwankg(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/pwankg"), "pwankg.gif"))

    @bot.command()
    @commands.is_nsfw()
    async def classic(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/classic"), "classic.gif"))

    @bot.command()
    @commands.is_nsfw()
    async def kuni(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/kuni"), "kuni.gif"))

    @bot.command()
    @commands.is_nsfw()
    async def femdom(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/femdom"), "femdom.png"))

    @bot.command()
    @commands.is_nsfw()
    async def ero_kitsune(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/erok"), "erok.png")) 

    @bot.command()
    @commands.is_nsfw()
    async def fox_girl(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/fox_girl"), "fox_girl.png"))

    @bot.command()
    @commands.is_nsfw()
    async def boobs(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/boobs"), "boobs.gif"))

    @bot.command()
    @commands.is_nsfw()
    async def ero(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/ero"), "ero.png"))
    
    @bot.command()
    async def smug(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/smug"), "smug.gif"))

    @bot.command()
    async def goose(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/goose"), "goose.png"))

    @bot.command()
    @commands.is_nsfw()
    async def trap(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/trap"), "trap.png"))

    @neko.group(invoke_without_command=True)
    @commands.is_nsfw()
    async def lewd(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/lewd"), "neko_lewd.png")) #equally as vital

    @lewd.command(aliases=["gif"])
    @commands.is_nsfw()
    async def lewd_gif(self, ctx):
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/nsfw_neko_gif"), "neko_lewd_gif.gif")) #this too

def setup(bot):
    bot.add_cog(neko(bot))