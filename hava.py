import sqlite3
import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import io
import discord
import locale

# Türkçe gün adları için locale ayarı
try:
    locale.setlocale(locale.LC_TIME, 'tr_TR.utf8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_TIME, 'turkish')
    except locale.Error:
        print("Uyarı: Türkçe yerel ayar ayarlanamadı. Gün adları İngilizce görünebilir.")


WEATHER_API_KEY = "05c503baacdde3186119ecc7bae81bcc"
CITY_NAME = "Istanbul"

def get_istanbul_temperature():
    """OpenWeatherMap API'den İstanbul'un anlık sıcaklığını çeker."""
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={WEATHER_API_KEY}&q={CITY_NAME}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data.get("cod") == 200:
        main_data = data["main"]
        temperature = main_data["temp"]
        return temperature
    else:
        print(f"Hava durumu verisi çekilirken hata oluştu: {data.get('message', 'Bilinmeyen Hata')}")
        return None

def create_database():
    """Veritabanı dosyasını ve tabloyu oluşturur (eğer yoksa)."""
    conn = sqlite3.connect("istanbul_hava_durumu.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS sicakliklar (
                 tarih TEXT PRIMARY KEY,
                 sicaklik REAL
                 )""")
    conn.commit()
    conn.close()

def save_daily_temperature(temperature):
    """Günlük sıcaklığı veritabanına kaydeder ve 7 günden eski veriyi siler."""
    create_database()
    conn = sqlite3.connect("istanbul_hava_durumu.db")
    c = conn.cursor()
    today = datetime.now().strftime("%Y-%m-%d")

    try:
        c.execute("INSERT INTO sicakliklar VALUES (?, ?)", (today, temperature))
        conn.commit()
        print(f"Yeni sıcaklık verisi kaydedildi: {today}, {temperature}°C")
        
        # 7 günden fazla veri varsa en eski veriyi sil
        c.execute("SELECT COUNT(*) FROM sicakliklar")
        row_count = c.fetchone()[0]

        if row_count > 7:
            c.execute("SELECT tarih FROM sicakliklar ORDER BY tarih ASC LIMIT 1")
            oldest_date = c.fetchone()[0]
            c.execute("DELETE FROM sicakliklar WHERE tarih = ?", (oldest_date,))
            conn.commit()
            print(f"Veritabanından en eski veri silindi: {oldest_date}")

        conn.close()
        return True

    except sqlite3.IntegrityError:
        print(f"Hata: {today} tarihine ait veri zaten var. Kayıt yapılmadı.")
        conn.close()
        return False

def get_weekly_data():
    """Veritabanından en son 7 günlük sıcaklık verisini çeker ve gün adlarını döndürür."""
    create_database()
    conn = sqlite3.connect("istanbul_hava_durumu.db")
    c = conn.cursor()
    
    # En son 7 kaydı tarihe göre azalan sırada çek
    c.execute("SELECT tarih, sicaklik FROM sicakliklar ORDER BY tarih DESC LIMIT 7")
    results = c.fetchall()
    
    x_verileri = []
    y_verileri = []
    
    # Verileri doğru sıraya getirmek için ters çevir
    for row in reversed(results):
        tarih, sicaklik = row
        day_name = datetime.strptime(tarih, "%Y-%m-%d").strftime("%A")
        x_verileri.append(day_name)
        y_verileri.append(sicaklik)

    conn.close()
    return x_verileri, y_verileri

def haftalik_sicaklik_grafigi_olustur():
    """Haftalık sıcaklık verilerini kullanarak sütun grafiği oluşturur."""
    grafik_adi = "İstanbul Haftalık Sıcaklık Değerleri"
    x_verileri, y_verileri = get_weekly_data()

    if not y_verileri:
        return "Hata: Veritabanında yeterli sıcaklık verisi bulunamadı."
        
    plt.rcParams['font.family'] = 'DejaVu Sans'
    plt.rcParams['font.sans-serif'] = ['Liberation Sans']
    
    plt.figure()
    plt.bar(x_verileri, y_verileri)
    plt.title(grafik_adi)
    plt.xlabel("Günler")
    plt.ylabel("Sıcaklık (°C)")
    plt.grid(True, axis='y')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf