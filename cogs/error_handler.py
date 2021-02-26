import discord
from discord.ext import commands

class error_handler(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            print("some idiot thought there was a command but there wasnt lmao")
            return await ctx.send('I dont know that fucking command?? <:RinThink:807264385856700446>')
        elif isinstance(error, commands.CheckFailure):
            print("some idiot thought they had perms to do mod stuff lmao")
            return await ctx.send('How about you get the fucking perms to do that first?')

def setup(bot):
    bot.add_cog(error_handler(bot))