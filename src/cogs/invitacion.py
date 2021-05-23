from discord.ext import commands
import discord

class invitacion_command(commands.Cog):
	def __init__(self,bot):
		self.bot = bot

	@commands.command(
		name="invitar",
		usage="",
		description="Muestra la invitacion del servidor"
		)
	async def invitar(self,ctx):
		description_content = """
  Somos programadores o aprendizes queriendo enseñar lo que sabemos y aprender de los que enseñan.

  https://discord.gg/4FUtbhatAg

		"""
		embed = discord.Embed(
			title = "Invitacion a SendTech Community",
			description = description_content,
			color = 0x486F8C
			)
		await ctx.send(embed=embed)
		
def setup(bot):
	bot.add_cog(invitacion_command(bot))
		