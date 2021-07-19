import discord
import logging
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
            name="--help misc",
            value="Show commands and subcommands related to the nekos.life API",
            inline=False
        )
        embed.add_field(
            name="--help moderation",
            value="Show commands and subcommands for moderation purposes"
        )
        embed.add_field(
            name="--ping", 
            value="Show latency, broken rn cant be asked to fix", 
            inline=False
        )
        embed.add_field(
            name="--nhentai/--nh <arg>",
            value="Posts a random doujin or fetches a certain doujin if an ID is provided. Only works in NSFW channels",
            inline=False
        )
        embed.add_field(
            name="--nhentai search [tag/character/whatever the fuck you want]/--nh search [tag/character/whatever the fuck you want]",
            value="Posts a search result of the tag/character/whatever the fuck you searched for. More info for how to search at https://nhentai.net/info/. Excluding tags does not yet work.",
            inline=False #thank you spam for , very cool
        )
        embed.add_field(
            name="--avatar @[user]",
            value="Returns the mentioned users avatar",
            inline=False
        )
        embed.add_field(
            name="--search [name of anime]",
            value="Gives the best result for the query from the MAL database. WIP.",
            inline=False
        )
        embed.add_field(
            name="--invite",
            value="Posts a link to invite the bot.",
            inline=False
        )
        embed.add_field(
            name="--rule34 [something to search for]/--r34 [something to search for]",
            value="Works similar to how the gelbooru commands work, just this time you need to put a _ between words. No lolis! You should be able to search for multiple tags, just put a space between them.",
            inline=False
        )
        embed.add_field(
            name="--reminder [title of reminder, time when you wanna be reminded]",
                value="Creates a reminder to remind you of something you want.\n Use -m [number] to set a reminder in [number] minutes,\n -d [number] to set a reminder in [number] days,\n -h [number] to set a reminder in [number] hours,\n -w [number] to set a reminder in [number] weeks.\n IMPORTANT! The title of your reminder needs to be in quotation marks!",
            inline=False
        )
        await ctx.send(embed=embed)
        logging.info('help embed sent')

    @help.command()
    async def neko(self, ctx):
        embed = discord.Embed(
            title="Help for Neko",
            description="These are the valid arguments for --neko",
            colour=0x1f13ee
        )
        embed.set_thumbnail(url="https://i.imgur.com/7Whb3qK.png")
        #embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/754643335511015505/810691863610523668/unknown.png")
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
        logging.info('neko help embed sent')

    @help.command(aliases=["gelb"])
    async def gelbooru(self, ctx):
        embed=discord.Embed(
            title="Help for Gelbooru",
            description="These are the valid commands for --gelbooru",
            colour=0x1f13ee
        )
        embed.set_thumbnail(url="https://i.imgur.com/PcRxTmE.png")
        embed.add_field(
            name="--gelb rs+<arg>",
            value="Posts a safe for work image in any channel, add tags as args to search for specific...tags. No loli! You have to put a + or a / in between tags.",
            inline=False
        )
        embed.add_field(
            name="--gelb rq+<arg>",
            value="Posts a questionable image in any nsfw channel, add tags as args to search for specific...tags. No loli! You have to put a + or a / in between tags.",
            inline=False
        )
        embed.add_field(
            name="--gelb re+<arg>",
            value="Posts an explicit image in any nsfw channel, add tags as args to search for specific...tags. No loli! You have to put a + or a / in between tags.",
            inline=False
        )
        await ctx.send(embed=embed)
        logging.info('gelbooru help embed sent')

    @help.command()
    async def misc(self, ctx):
        embed=discord.Embed(
            title="Help for every command related to the nekos.life API",
            description="These commands all use the nekos.life API, the same way anything in --help neko does.",
            colour=0x1f13ee
        )
        embed.set_thumbnail(url="https://i.imgur.com/MjGFq8P.png")
        embed.add_field(
            name="--fox",
            value="Posts an image of a foxgirl in any channel.",
            inline=False
        )
        embed.add_field(
            name="--feet",
            value="Posts an image of feet in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--yuri",
            value="Posts an image of yuri in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--futa",
            value="Posts an image of futa in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--lewdkemo",
            value="Posts an image of a lewd kemonomimi in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--feet gif",
            value="Posts a gif of feet in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--cum",
            value="Posts a gif with cum in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--erokemo",
            value="Posts an image of an erotic-looking kemonomimi in any channel.",
            inline=False
        )
        embed.add_field(
            name="--les",
            value="tbh I have no idea what this tag is supposed to be but its hot trust me",
            inline=False
        )
        embed.add_field(
            name="--lewdfox",
            value="Posts an image of a lewd foxgirl in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--eroyuri",
            value="Posts an image of yuri but better I guess in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--eron",
            value="Posts an image of an erotic-looking neko in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--cum jpg",
            value="Posts an image with cum in any channel.",
            inline=False
        )
        embed.add_field(
            name="--bj",
            value="Posts a gif of a blowjob in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--solo",
            value="Posts an image of a solo femail in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--kemo",
            value="Posts an image of a kemonomimi in any channel.",
            inline=False
        )
        embed.add_field(
            name="--nsfw_avatar",
            value="Posts a nsfw avatar in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--anal",
            value="Posts a gif of anal in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--hentai",
            value="Posts an image of just general hentai in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--erofeet",
            value="Posts an image of erotic-looking feet in any channel.",
            inline=False
        )
        embed.add_field(
            name="--keta",
            value="I am also not quite sure what this tag is but I suppose its pretty nice.",
            inline=False
        )
        embed.add_field(
            name="--blowjob",
            value="Posts an image of a blowjob in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--pussy",
            value="Posts a gif of a pussy in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--tits",
            value="Posts an image of a pair of tits in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--lizard",
            value="Posts an image of a lizard in any channel.",
            inline=False
        )
        embed.add_field(
            name="--pussy jpg",
            value="Posts an image of a pussy in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--pwankg",
            value="I also have no idea what this is but its also very hot yes yes",
            inline=False
        )
        embed.add_field(
            name="--classic",
            value="Posts a gif of some classics in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--kuni",
            value="Yea also no clue what this is but also good",
            inline=False
        )
        embed.add_field(
            name="--femdom",
            value="Posts an image of some nice femdom in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--ero_kitsune",
            value="Posts an image of a erotic-looking foxgirl in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--fox_girl",
            value="Also posts an image of a foxgirl in any channel.",
            inline=False
        )
        embed.add_field(
            name="--boobs",
            value="Posts a gif of a nice pair of boobs in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--ero",
            value="Posts an erotic-looking image in any nsfw channel.",
            inline=False
        )
        embed.add_field(
            name="--smug",
            value="Posts an gif of smug face in any channel.",
            inline=False
        )
        embed.add_field(
            name="--goose",
            value="Posts an image of a goose in any channel.",
            inline=False
        )
        embed.add_field(
            name="--trap",
            value="Posts an image of a trap in any nsfw channel.",
            inline=False
        )
        await ctx.send(embed=embed)
        logging.info('misc help embed sent')

    @help.command()
    async def moderation(self, ctx):
        embed=discord.Embed(
            title="Help for moderator commands",
            description="These commands can only be used by those with the perms to do so.",
            colour=0x1f13ee
        )
        embed.add_field(
            name="--purge [number]",
            value="Purges the amount of messages specified. Only useable by Administrators",
            inline=False
        )
        embed.add_field(
            name="--ban [person] [optional reason]",
            value="Bans the person mentioned for the reason specified. If no reason is provided, the direct message to the banned member will just state 'begone thot'. Only useable by those with the 'Ban members' permission.",
            inline=False
        )
        await ctx.send(embed=embed)
        logging.info('Moderation help embed sent')

def setup(bot):
    bot.add_cog(helpClient(bot))