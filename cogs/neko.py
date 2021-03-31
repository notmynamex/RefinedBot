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

    @bot.command()
    async def feet(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/feet"), "feet.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def yuri(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/yuri"), "yuri.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def futa(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/futanari"), "futa.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def lewdkemo(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/lewdkemo"), "lewdkemo.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def feet_gif(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/feetg"), "feet.gif"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.group(invoke_without_command=True)
    async def cum(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/cum"), "cum.gif"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def erokemo(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/erokemo"), "erokemo.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def les(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/les"), "les.gif"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def lewdfox(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/lewdk"), "lewdk.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def eroyuri(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/eroyuri"), "eroyuri.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def eron(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/eron"), "eron.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @cum.command(aliases=["jpg"])
    async def cum_jpg(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/cum_jpg"), "cum.jpg"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def bj(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/bj"), "bj.gif"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def solo(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/solo"), "solo.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def kemo(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/kemonomimi"), "kemonomimi.png"))

    @bot.command()
    async def nsfw_avatar(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/nsfw_avatar"), "nsfw_avatar.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def anal(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/anal"), "anal.gif"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/hentai"), "hentai.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def erofeet(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/erofeet"), "erofeet.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def keta(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/keta"), "keta.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def blowjob(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/blowjob"), "blowjob.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.group(invoke_without_command=True)
    async def pussy(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/pussy"), "pussy.gif"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def tits(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/tits"), "tits.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def lizard(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/lizard"), "lizard.png"))

    @pussy.command(aliases=["jpg"])
    async def pussy_jpg(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/pussy_jpg"), "pussy.jpg"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def pwankg(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/pwankg"), "pwankg.gif"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def classic(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/classic"), "classic.gif"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def kuni(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/kuni"), "kuni.gif"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def femdom(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/femdom"), "femdom.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def ero_kitsune(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/erok"), "erok.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def fox_girl(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/fox_girl"), "fox_girl.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def boobs(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/boobs"), "boobs.gif"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def ero(self, ctx):
        if ctx.channel.is_nsfw() is True:
            await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/ero"), "ero.png"))
        if ctx.channel.is_nsfw() is False:
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

    @bot.command()
    async def smug(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/smug"), "smug.gif"))

    @bot.command()
    async def goose(self, ctx):
        await ctx.send(file=discord.File(await image("https://nekos.life/api/v2/img/goose"), "goose.png"))

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