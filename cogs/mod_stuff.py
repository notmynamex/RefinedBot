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

    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, *, member:discord.User=None, reason =None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("why the fuck do you want to ban yourself??")
            print("wow the idiot tried to ban himself lmao")
            return
        if reason == None:
            reason = "begone thot"
            print("someone has been banned lmao")
        message = f"begone from {ctx.guild.name}, thou hast been banned for {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"{member} has been purged from the land of the refined")
        print("someone has been banned lmao")

def setup(bot):
    bot.add_cog(mod_stuff(bot))
