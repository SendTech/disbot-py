from decouple import config
from discord.ext import commands
import discord
from keep_alive import live

# Add the token of the bot
DISCORD_TOKEN = config("BOT_TOKEN")

# Description and basic configuration
description = "Un Bot de Ayuda para la Comunidad de Sendero Tecnológico"
prefix = "!"
bot = commands.Bot(command_prefix=prefix, description=description, help_command=None)


# Bot initial config
@bot.event
async def on_ready():
    print(f"Initial as {bot.user}")

    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="SendTech Community| !help"))


# help
@bot.command()
async def help(ctx):
    miDescripcion = """
    ping: El bot te responde pong.
    avatar @user: Muestra el avatar de alguien mas o tuyo.
    hola: El bot te saluda.
    invitar: Muestra la invitacion de Sendero Tecnológico.
    cita: Muestra una cita célebre random.
    dogs: Muestra imagenes de lindos perritos.
    cats: Muestra anécdotas sobre gatos.
    wiki: Realiza una busqueda en la wikipedia.
    google: Realiza una busqueda en google.
    yt: Realiza una busqueda en youtube 
    joke: te cuenta un chistesito. 
    hecho por los configuradores de Sendero Tecnologico.
    """
    embed = discord.Embed(
      title = 'El comando de ayuda de este Hermoso bot',
      description = miDescripcion,
      color = discord.Color.blue(),
      footer=ctx.message.created_at
    )
    await ctx.send(embed = embed)


extensions = ['cogs.avatar', 'cogs.ping', 'cogs.hola','cogs.invitacion', 'cogs.quotes' ,'cogs.dogs', 'cogs.cat','cogs.wiki','cogs.joke','cogs.yt','cogs.google']

for i in extensions:
    try:
        bot.load_extension(i)
    except Exception as err:
        print(f'Ups a occurrido un error {err}')

live()

# Running the bot
bot.run(DISCORD_TOKEN)
