import discord
from discord.ext import commands
import datetime
import urllib.request
import re




class google(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

   

    @commands.Cog.listener()
    async def on_ready(self):
        print("Youtube Cog has been loaded\n-----")

    @commands.command()
    async  def  yt(self,ctx,* ,args):
      try:
          
          vide=args
          video=vide.replace(" ", "+")
          html=urllib.request.urlopen("https://www.youtube.com/results?search_query="+video)
          video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
          url = f"https://www.youtube.com/watch?v={video_ids[0]}"
          print(url)
          
          embed = discord.Embed(title=f"Resultados para {args} desde youtube",
          description=f"",timestamp=datetime.datetime.utcnow(),
          color = 0x486F8C )
          embed.set_thumbnail(url="")
          
         
          
          embed.set_footer(text="by {}".format(ctx.author.display_name))
          embed.set_author(name="SendTech", icon_url="https://cdn.discordapp.com/avatars/805234023550156840/b337be9357f3aac1e498fad42634816d.png?size=128")
          await ctx.send(embed=embed)
          await ctx.send(url)
        
      except:
         embed = discord.Embed(
           title=f"\u26A0\uFE0F Error 404, no hay buenos resultados para {args}",
           description="PD: Intenta buscar otra cosa",
         color=discord.Color.red())
         await ctx.send(embed=embed)
        
      

        
	
        

def setup(bot):
    bot.add_cog(google(bot))

