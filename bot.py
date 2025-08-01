# This example requires the 'message_content' intent.
import discord
from config import TOKEN
from main import base641
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot başlatıldı!")
@bot.command()
async def merhaba(ctx: commands.Context):
    await ctx.send(f"Merhaba, {ctx.author.name}. Ben ilginç fotoğraflar üreten bir botum")

@bot.command()
async def foto(ctx:commands.Context):
    return base641
bot.run(TOKEN)