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
		Quieren unirse a SENDERO TECNOLOGICO, 
en este server intentamos que tu, yo y todos aprendemos juntos con talleres, videos de youtube de la comunidad, entre otros. 

:computer:   https://senderotecnologico.gq/ :computer:
o solo  https://senderotecnologico.gq/

		"""
		embed = discord.Embed(
			title = "Invitados",
			description = description_content,
			color = discord.Color.random()
			)
		await ctx.send(embed=embed)
		
def setup(bot):
	bot.add_cog(invitacion_command(bot))
		