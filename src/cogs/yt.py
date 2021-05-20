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
        print("\n Youtube Cog has been loaded\n-----")

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
          description=f"",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
          embed.set_thumbnail(url="")
          
         
          
          embed.set_footer(text="Solicitado por: {}".format(ctx.author.display_name))
          embed.set_author(name="AlexanderG", icon_url="https://cdn.discordapp.com/avatars/809827305295314967/babea11271bbf5a89d5bf15220e7c278.webp?size=1024")
          await ctx.send(embed=embed)
          await ctx.send(url)
        
      except:
         embed = discord.Embed(title=f"<:NO:804625815685824514> Error 404, no hay resultados concretos para {args} ",color=discord.Color.red())
         await ctx.send(embed=embed)
        
      

        
	
        

def setup(bot):
    bot.add_cog(google(bot))

