import discord
from discord.ext import commands, tasks
import logic
import hava # Yeni dosyamızı import ediyoruz
import datetime

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yapıldı.')
    print('-------------------------')
    gunluk_veri_kaydetme.start()
    haftalik_grafik_gonder.start()

# --- Grafik Komutları (logic.py'den gelenler) ---

@bot.command()
async def cizgi(ctx, grafik_adi, x_verileri, y_verileri):
    """
    Çizgi grafiği oluşturur.
    Örnek kullanım: !cizgi "Başlık" "1,2,3" "10,20,30"
    """
    await ctx.send("Çizgi grafiğiniz oluşturuluyor...")
    result = logic.cizgi_grafik(grafik_adi, x_verileri, y_verileri)
    if isinstance(result, str):
        await ctx.send(result)
    else:
        file = discord.File(result, filename=f"{grafik_adi}.png")
        await ctx.send(file=file)

@cizgi.error
async def cizgi_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"⚠️ **Hata:** Lütfen tüm parametreleri girin.\nDoğru kullanım: `!cizgi \"Grafik Başlığı\" \"x,verileri\" \"y,verileri\"`")

@bot.command()
async def sutun(ctx, grafik_adi, x_verileri, y_verileri):
    """
    Sütun grafiği oluşturur.
    Örnek kullanım: !sutun "Satışlar" "A,B,C" "150,200,120"
    """
    await ctx.send("Sütun grafiğiniz oluşturuluyor...")
    result = logic.sutun_grafik(grafik_adi, x_verileri, y_verileri)
    if isinstance(result, str):
        await ctx.send(result)
    else:
        file = discord.File(result, filename=f"{grafik_adi}.png")
        await ctx.send(file=file)

@sutun.error
async def sutun_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"⚠️ **Hata:** Lütfen tüm parametreleri girin.\nDoğru kullanım: `!sutun \"Grafik Başlığı\" \"kategoriler\" \"değerler\"`")

@bot.command()
async def nokta(ctx, grafik_adi, x_verileri, y_verileri):
    """
    Nokta grafiği oluşturur.
    Örnek kullanım: !nokta "Korelasyon" "1,2,3" "10,20,30"
    """
    await ctx.send("Nokta grafiğiniz oluşturuluyor...")
    result = logic.nokta_grafik(grafik_adi, x_verileri, y_verileri)
    if isinstance(result, str):
        await ctx.send(result)
    else:
        file = discord.File(result, filename=f"{grafik_adi}.png")
        await ctx.send(file=file)

@nokta.error
async def nokta_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"⚠️ **Hata:** Lütfen tüm parametreleri girin.\nDoğru kullanım: `!nokta \"Grafik Başlığı\" \"x,verileri\" \"y,verileri\"`")

# --- Hava Durumu Komutları ve Görevleri (hava.py'den gelenler) ---

@tasks.loop(hours=24)
async def gunluk_veri_kaydetme():
    sicaklik = hava.get_istanbul_temperature()
    if sicaklik is not None:
        hava.save_daily_temperature(sicaklik)
        print(f"[{datetime.datetime.now()}] İstanbul sıcaklığı kaydedildi: {sicaklik}°C")

@tasks.loop(hours=168)
async def haftalik_grafik_gonder():
    # Buraya, grafiğin gönderileceği kanalın ID'sini girin
    channel_id = 1405505269793951856
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("Haftalık sıcaklık grafiği oluşturuluyor...")
        result = hava.haftalik_sicaklik_grafigi_olustur()
        if isinstance(result, str):
            await channel.send(result)
        else:
            file = discord.File(result, filename=f"haftalik_sicaklik_grafigi.png")
            await channel.send(file=file)
    else:
        print(f"Hata: {channel_id} ID'li kanal bulunamadı.")

@bot.command(name='haftalik')
async def haftalik_grafik(ctx):
    """
    Manuel olarak son 7 günlük sıcaklık grafiğini gösterir.
    Kullanım: !haftalik
    """
    await ctx.send("Haftalık sıcaklık grafiği oluşturuluyor...")
    result = hava.haftalik_sicaklik_grafigi_olustur()
    if isinstance(result, str):
        await ctx.send(result)
    else:
        file = discord.File(result, filename=f"haftalik_sicaklik_grafigi.png")
        await ctx.send(file=file)

# Bot tokeninizi buraya girin
BOT_TOKEN = "token"
bot.run(BOT_TOKEN)