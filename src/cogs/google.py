import discord
from discord.ext import commands
import datetime
from googlesearch import search





class google(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

   

    @commands.Cog.listener()
    async def on_ready(self):
        print("\n Google Cog has been loaded\n-----")

    @commands.command()
    async  def  google(self,ctx,* ,args):
      try:
          
          print(args)
          tld = "com"
          lang = "en" 
          num=1  
          start=0 
          stop=num 
          pause=2.0 
          results = search(args, tld=tld, lang=lang, num=num, start=start, stop=stop, pause=pause)
          
          embed = discord.Embed(title=f"Resultados para {args} desde google",
          description=f"",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
          embed.set_thumbnail(url="")
          
         
          
          embed.set_footer(text="Solicitado por: {}".format(ctx.author.display_name))
          embed.set_author(name="AlexanderG", icon_url="https://cdn.discordapp.com/avatars/809827305295314967/babea11271bbf5a89d5bf15220e7c278.webp?size=1024")
          await ctx.send(embed=embed)
          for r in results:
            await ctx.send(r)
      except:
         embed = discord.Embed(title=f"<:NO:804625815685824514> Error 404, no hay resultados concretos para {args} ",color=discord.Color.red())
         await ctx.send(embed=embed)
        
      

        
	
        

def setup(bot):
    bot.add_cog(google(bot))
