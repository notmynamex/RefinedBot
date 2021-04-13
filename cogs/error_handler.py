import discord
import logging
from discord.ext import commands


class error_handler(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            logging.info("some idiot thought there was a command but there wasnt lmao")
            return await ctx.send('I dont know that fucking command?? <:RinThink:807264385856700446>')

        elif isinstance(error, commands.BadArgument):
            logging.info(f"Fucking dumbass doesn't know how to pass in arguments ({error})")
            return await ctx.send("You gave a bad argument you fucking dumbass")
        
        elif isinstance(error, commands.NSFWChannelRequired):
            logging.info("some idiot tried posting nsfw content in a sfw channel")
            return await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')

        elif isinstance(error, commands.CheckFailure):
            logging.info("some idiot thought they had perms to do mod stuff lmao")
            return await ctx.send('How about you get the perms to do that first?')
        
        else:
            logging.info(error)


def setup(bot):
    bot.add_cog(error_handler(bot))
