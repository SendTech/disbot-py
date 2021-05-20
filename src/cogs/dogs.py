import discord
import requests
from discord.ext import commands


class dogs_commands(commands.Cog):
    def __init_(self, bot):
        self.bot = bot

    @commands.command(
        name="dogs",
        usage="",
        description="Quieres conocer al mejor amigo del hombre usa este comando"
    )
    async def dogs(self, ctx):
        embed2 = discord.Embed(
            title="Puede tardar un momento :clock:",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed2)
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        status = response.status_code
        if status == int(200):
            answer = response.json()
            api_status = answer['status']
            image_link = answer['message']
            embed = discord.Embed(
                title="Ohhh, que lindo perrito",
                color = discord.Color.blue()
            )
            embed.set_image(url=image_link)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(dogs_commands(bot))
