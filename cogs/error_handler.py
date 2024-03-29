import logging
from discord.ext import commands
from discord.ext.commands.errors import PartialEmojiConversionFailure


class error_handler(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        logging.info("on_command_error triggered")
        
        if isinstance (error, commands.MissingRequiredArgument):
            logging.info(f"Some absolute imbecile didn't give a required argument ({error.param.name})")
            return await ctx.send("You absolute imbecile, you didn't provide a required argument")
        
        elif isinstance(error, commands.BadArgument):
            logging.info(f"Fucking dumbass doesn't know how to pass in arguments ({error})")
            return await ctx.send("You gave a bad argument you fucking dumbass")
        
        elif isinstance(error, commands.CommandNotFound):
            logging.info("some idiot thought there was a command but there wasnt lmao")
            return await ctx.send('I dont know that fucking command?? <:RinThink:807264385856700446>')
        
        elif isinstance(error, commands.NSFWChannelRequired):
            logging.info("some idiot tried posting nsfw content in a sfw channel")
            await ctx.send('go to a nsfw channel you fucking idiot <:RinKEK:802258335062949888>')
            return await ctx.send('https://i.imgur.com/g1fYdLn.png')

        elif isinstance(error, commands.CheckFailure):
            logging.info("some idiot thought they had perms to do mod stuff lmao")
            return await ctx.send('How about you get the perms to do that first?')
        
        else:
            logging.info(error)


def setup(bot):
    bot.add_cog(error_handler(bot))
