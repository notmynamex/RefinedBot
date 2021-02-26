import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='--')

class mod_stuff(commands.Cog):
    def __init__(self, client):
        self.client = client

    @bot.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
            await ctx.channel.purge(limit=limit)
            print("the purge has begun")

def setup(bot):
    bot.add_cog(mod_stuff(bot))