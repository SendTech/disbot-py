from decouple import config
from discord.ext import commands
import discord
from discord.utils import *

# Add the token of the bot
DISCORD_TOKEN = config("BOT_TOKEN")

# Description and basic configuration
description = "Un Bot de Ayuda para quien lo Necesite"
prefix = "!"
bot = commands.Bot(command_prefix=prefix, description=description)


# Bot initial config
@bot.event
async def on_ready():
    print(f"Initial as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" www.github.com/TeoDev1611"))

@bot.event
async def on_member_join(member,ctx):
    guild = member.guild
    mention = member.mention
    channel = get(guild.channels, name='bienvenida')
    integrantes = format(guild.member_count)
    await channel.send(f'Hey {mention} se ha unido al servidor somos {integrantes}')

@bot.event
async def on_member_remove(member,ctx):
    guild = member.guild
    mention = member.mention
    channel = get(guild.channels, name='bienvenida')
    integrantes = format(guild.member_count)
    await channel.send(f'{mention} ha salido del servidor somos :C {integrantes}')


bot. load_extension("cogs.ping")
bot. load_extension("cogs.avatar")
bot. load_extension("cogs.quotes")
bot. load_extension("cogs.cat_facts")
bot. load_extension("cogs.dogs")
bot.load_extension("cogs.invitacion")
bot.load_extension("cogs.hola")
bot.load_extension("cogs.play_music")
# Running the bot
bot.run(DISCORD_TOKEN)
