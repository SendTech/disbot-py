import time
from discord.ext import commands

class ping_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="ping",
        usage="",
        description="El bot responde pong"
    )
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send(":ping_pong: Pong !")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f":ping_pong: pong ! `{int(ping)} ms` ")
        await message.add_reaction('\U0001f525')

def setup(bot):
    bot.add_cog(ping_command(bot))