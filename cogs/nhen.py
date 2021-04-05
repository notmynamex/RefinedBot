import discord
import requests
import logging
from discord.ext import commands
from NHentai import NHentai
from hentai import Utils, Sort, Option, Tag, Hentai, Format

bot = commands.Bot(command_prefix='--')
nhentai = NHentai()



async def sauce_embed(sauce):
    print(sauce)
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

    @bot.group(invoke_without_command=True, aliases=["nh"])
    @commands.is_nsfw()
    async def nhentai(self, ctx, argument=None):
        logging.info("Ran nhentai in nsfw channel")
        if argument is None:
            sauce = nhentai.get_random()
            logging.info("random doujin sent")
            return await ctx.send(embed=await sauce_embed(sauce))
        if argument.isdigit():
            sauce = nhentai._get_doujin(id=argument)
            if sauce is None:
                return await ctx.send("wrong id you idiot <:RinKEK:802258335062949888>")
            logging.info(sauce)
            await ctx.send(embed=await sauce_embed(sauce))


    @nhentai.command()
    @commands.is_nsfw()
    async def search(self, ctx, argument=None, val=0):
        logging.info("Ran nhentai search in nsfw channel")
        if argument is None:
            logging.info("nothing provided lmao")
            return await ctx.send("i cant search for nothing wtf")
        if argument.isalpha():
            SearchPage = nhentai.search(query=argument, sort='popular', page=1)
            Doujin = getattr(SearchPage, "doujins")
            if not Doujin:
                logging.info("nothing found lmao what a dumbass")
                return await ctx.send("nothing found, please dont try again")
            await ctx.send(embed=await sauce_embed(nhentai._get_doujin(id=getattr(Doujin[int(val)], "id"))))


def setup(bot):
    bot.add_cog(nhen(bot))