import discord
from config import TOKEN

from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot başlatıldı!")
@bot.command()
async def merhaba(ctx: commands.Context):
    await ctx.send(f"Merhaba, {ctx.author.name}. Ben grafik üreten bir botum")

@bot.command()
#Allahın izniyle bu kısım grafik üretecek elimde logic dosyası olmadığı için bu kısma bir şey yazamıyorum
async def start(ctx):
    pass

bot.run(TOKEN)
