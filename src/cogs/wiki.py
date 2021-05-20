import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re
from time import sleep
import random
import wikipedia
from keep_alive import live 

import os



class wiki(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

   

    @commands.Cog.listener()
    async def on_ready(self):
        print("\n Wikipedia Cog has been loaded\n-----")

    @commands.command()
    async  def  wiki(self,ctx,* ,args):
      try:
          print(args)
          wikipedia.set_lang("es")
          ny = wikipedia.page(args)
          embed = discord.Embed(title=f"Resultados para {ny.title}",
          description=f"{ny.title}",timestamp=datetime.datetime.utcnow(),color=discord.Color.random())
          embed.set_thumbnail(url="https://media.tenor.com/images/5630f15a78c91310d9d8d1ffcac7e124/tenor.gif")
          result = wikipedia.summary(args,sentences=3)
          embed.add_field(name="Contenido de busqueda", value=f"{result}", inline=True)
          url=f"{ny.url}"
          embed.set_image(url=f"{ny.images[0]}")
          await ctx.send(embed=embed)
          await ctx.send("Enlaces externos: " + url)
      except:
         embed = discord.Embed(
           title=f" Error 404, busca algo que exista para {args} ",
           color = discord.Color.blue()
           )
         await ctx.send(embed=embed)
        
      

        
	
        

def setup(bot):
    bot.add_cog(wiki(bot))

