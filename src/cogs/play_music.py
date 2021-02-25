from discord.ext import commands
from urllib import parse,request
import re
import discord
import youtube_dl 

class play_music(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(
        name="search",
        description="Reproduce canciones de youtube"
    )
    async def youtube(self,ctx,bot,*,search):
        # search in youtube
        query = parse.urlencode({"search_query":search})
        html_content = request.urlopen("https://www.youtube.com/results?"+query)
        search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())
        print(search_results)
        clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
        embed = discord.Embed(
            title="Estos son los resultados de tu busqueda",
            description = clip2,
            color = discord.Color.random()
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(play_music(bot))