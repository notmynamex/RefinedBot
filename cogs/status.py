from random import getrandbits
from random import choice
import discord
from discord.ext import commands
from discord.ext import tasks
import logging

status_list = [
    "try --mention",
    "fuck everyone who is reading this",
    "you fucking suck",
    "try --help",
    "did you know you suck?",
    "please dont crash me i am friendly bot yes",
    "https://vndb.org/v4037",
    "astolfo best waifu",
    "pew pew you ded now haha",
    "sirspam not gay",
    "please use my commands please im kinda bored please use them",
    "some eroge",
    "osu!",
    "Beat Saber",
    "Azur Lane",
    "not genshin impact",
    "waiting for ghost of tsushima pc port"
]

watchlist = [
    "HELO die",
    "notmyname fail at life",
    "notmyname look at hentai",
    "notmyname fail at coding me",
    "sirspam help notmyname",
    "hentai",
    "A certain scientific Railgun",
    "A certain magical Index",
    "a slime do politics",
    "Dimension W",
    "hayasaka be perfect as fuck",
    "astolfo do astolfo things",
    "dead people get sent into elevators",
    "some guy teach magic to a carpet",
    "konosuba season 1 because season 2 was bad",
    "highschool dxd for the 64th time",
    "hololive",
    "some scottish guy kill a lot of people",
    "berserk 2016",
    "kansen sodom",
    "notmyname have shit luck in every gacha game ever"
]


class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @tasks.loop(minutes=5)
    async def status(self):
        await self.bot.wait_until_ready()
        if getrandbits(1) == 1:
            value = choice(status_list)
            await self.bot.change_presence(activity=discord.Game(name=value))
            logging.info(f"Status set to: playing {value}")
        else:
            value = choice(watchlist)
            await self.bot.change_presence(activity=discord.Activity(name=value, type=discord.ActivityType.watching))
            logging.info(f"Status set to: watching {value}")

    @commands.Cog.listener()
    async def on_ready(self):
        self.status.start()


def setup(bot):
    bot.add_cog(status(bot))
