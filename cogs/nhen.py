import discord
from discord.ext import commands
from NHentai import NHentai

bot = commands.Bot(command_prefix='--')
nhentai = NHentai()


async def sauce_embed(sauce):
    desc = "Tags: "
    for x in getattr(sauce, "tags"):
        desc = desc + x + ", "
    if "english" in getattr(sauce, "languages"):
        lang = "🇬🇧"
    elif "japanese" in getattr(sauce, "languages"):
        lang = "🇯🇵"
    elif "chinese" in getattr(sauce, "languages"):
        lang = "🇨🇳"
    else: 
        lang = "❔"
    embed = discord.Embed(
        title=f"{lang} "+getattr(sauce,"title"),
        url="https://nhentai.net/g/"+getattr(sauce,"id")+"/",
        description=desc,
        colour=0x1f13ee,
    )
    embed.set_footer(text=str(getattr(sauce,"total_pages"))+" total pages")
    embed.set_image(url=(getattr(sauce,"images"))[0])
    return embed

class nhen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.command(aliases=["nh"])
    async def nhentai(self, ctx, argument=None):
        if ctx.channel.is_nsfw() is True:
            print("Ran nhentai in nsfw channel")
            if argument is None:
                sauce = nhentai.get_random()
                return await ctx.send(embed=await sauce_embed(sauce))
            if argument.isdigit():
                sauce = nhentai._get_doujin(id=argument)
                if sauce is None:
                    return await ctx.send("wrong id you idiot <:RinKEK:802258335062949888>")
                await ctx.send(embed=await sauce_embed(sauce))
        if ctx.channel.is_nsfw() is False:
            print("Ran nhentai outside of nsfw channel")
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

def setup(bot):
    bot.add_cog(nhen(bot))