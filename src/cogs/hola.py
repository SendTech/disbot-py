from discord.ext import commands
import discord

class hola_command(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.command(name="hola")
	async def hola(self,ctx):
		embed = discord.Embed(
			title="Hola ¿Que tal?, que estas haciendo?",
			description="Nota: Estoy Vivo :shushing_face: | Por suerte.",
			color = discord.Color.blue()
		)
		await ctx.send(embed=embed)
def setup(bot):
	bot.add_cog(hola_command(bot))
