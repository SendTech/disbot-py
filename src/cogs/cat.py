from discord.ext import commands
import discord
import requests

class cat_command(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	@commands.command(
		name = "cats",
		usage = "",
		description = "Quieres ver datos curiosos de gatos usa este comando"
	)
	async def cat(self,ctx):
		embed2 = discord.Embed(
			title="Puede tardar un momento :alarm_clock:",
			color=discord.Color.red()
		)
		await ctx.send(embed = embed2)
		response = requests.get("https://the-cat-fact.herokuapp.com/api/randomfact")
		status = response.status_code
		if status == int(200):
			answer = response.json()
			api_status = answer['status']
			first_data = answer['data']
			data = first_data[0]
			fact = data['fact']
			message = answer['message']
			embed = discord.Embed(
				title=message,
				description=fact,
				color = 0x486F8C,
			)
			embed.set_footer(text=api_status)
			embed.set_author(
				name="Que lindo michi",
				icon_url="https://i.ibb.co/K5cR5jk/descarga.png"
			)
			await ctx.send(embed=embed)
def setup(bot):
	bot.add_cog(cat_command(bot))
