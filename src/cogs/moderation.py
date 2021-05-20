import discord
from discord.ext import commands


class moderation_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="ban"
    )  # uses command decorators, in this case inside a cog
    @commands.has_permissions(ban_members=True)  # only people that have permissions to ban users can use this command
    async def ban(self, ctx, user: discord.Member, *,
                  reason):
        await ctx.guild.ban(user, reason=reason)  # Bans the user.
        embed = discord.Embed(
            title=f'El usuario {user} ha sido baneado',
            description=f'Por la siguiente razon **{reason}**',
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

    @commands.command(
        name="kick"
    )  # uses command decorators, in this case inside a cog
    @commands.has_permissions(kick_members=True)  # only people that have permissions to ban users can use this command
    async def kick(self, ctx, user: discord.Member, *,
                   reason):
        await ctx.guild.kick(user, reason=reason, delete_message_days=0)  # Bans the user.
        embed = discord.Embed(
            title=f'El usuario {user} ha sido kickeado',
            description=f'Por la siguiente razon **{reason}**',
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    
    # Clear Command 
    @commands.command(
        name = "clear"
    )
    @commands.has_permissions(delete_messages=True)
    async def clear (self,ctx,amount):
        await ctx.channel.purge(limit)


def setup(bot):
    bot.add_cog(moderation_commands(bot))
