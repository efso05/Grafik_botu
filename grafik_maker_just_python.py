import matplotlib.pyplot as plt

def grafik_ayarlarini_al():
    """Kullanıcıdan grafik adını ve türünü alır ve geri döndürür."""
    grafik_adi = input("Grafiğinizin adını giriniz: ")
    grafik_tipi = input("Oluşturmak istediğiniz grafik türünü yazınız (örn: cizgi): ")
    return grafik_adi, grafik_tipi # İki değeri de geri döndür

def cizgi_grafik(grafik_adi):
    """Kullanıcıdan x ve y verilerini alarak bir çizgi grafiği çizer."""
    
    x_veri_string = input("Lütfen x ekseni verilerini virgülle ayırarak girin (örn: 1, 2, 3, 4): ")
    y_veri_string = input("Lütfen y ekseni verilerini virgülle ayırarak girin (örn: 10, 20, 15, 25): ")

    try:
        x_verileri = [float(s.strip()) for s in x_veri_string.split(',')]
        y_verileri = [float(s.strip()) for s in y_veri_string.split(',')]

        if len(x_verileri) != len(y_verileri):
            print("Hata: x ve y ekseni verilerinin sayısı eşit olmalıdır.")
            return

        plt.plot(x_verileri, y_verileri, marker='o')
        
        plt.title(grafik_adi) 
        plt.xlabel("X Ekseni")
        plt.ylabel("Y Ekseni")
        plt.grid(True)
        plt.show()

    except ValueError:
        print("Hata: Lütfen geçerli sayı formatında veriler girin.")

def sutun_grafik(grafik_adi):
    """Kullanıcıdan x (kategori) ve y (sayısal) verilerini alarak bir sütun grafiği çizer."""
    
    # Kullanıcıdan x ekseni (kategorik) verilerini al
    x_veri_string = input("Lütfen x ekseni verilerini virgülle ayırarak girin (örn: A, B, C, D): ")
    
    # Kullanıcıdan y ekseni (sayısal) verilerini al
    y_veri_string = input("Lütfen y ekseni verilerini virgülle ayırarak girin (örn: 10, 20, 15, 25): ")

    try:
        # Gelen string'leri virgüllere göre ayırarak listeye dönüştür
        x_verileri = [s.strip() for s in x_veri_string.split(',')]
        # Gelen string'leri sayıya (float) dönüştür
        y_verileri = [float(s.strip()) for s in y_veri_string.split(',')]

        # x ve y listelerinin aynı uzunlukta olup olmadığını kontrol et
        if len(x_verileri) != len(y_verileri):
            print("Hata: x ve y ekseni verilerinin sayısı eşit olmalıdır.")
            return

        # Sütun grafiği çiz
        plt.bar(x_verileri, y_verileri)

        # Başlık ve eksen etiketlerini ekle
        plt.title(grafik_adi) 
        plt.xlabel("Elemanların isimlerini giriniz (Kategoriler)")
        plt.ylabel("Y Ekseni (Değerler)")
        
        # Grid (ızgara) ekle
        plt.grid(True, axis='y') # Sadece y ekseninde ızgara göster

        # Grafiği göster
        plt.show()

    except ValueError:
        print("Hata: Lütfen geçerli sayı formatında veriler girin.")

# --- Ana Program ---

# grafik_ayarlarini_al() fonksiyonundan dönen iki değeri yakala
grafik_adi, grafik_tipi = grafik_ayarlarini_al()

# Gelen grafik tipine göre ilgili fonksiyonu çağır
if grafik_tipi == "cizgi":
    cizgi_grafik(grafik_adi)

elif grafik_tipi == "sütun":
    sutun_grafik(grafik_adi)

else:
    print(f"'{grafik_tipi}' türünde bir grafik oluşturulamıyor.")
