import matplotlib.pyplot as plt
import io
import discord

def cizgi_grafik(grafik_adi, x_veri_string, y_veri_string):
    """Verilen x ve y verileriyle bir çizgi grafiği oluşturur ve bayt olarak döndürür."""
    try:
        x_verileri = [float(s.strip()) for s in x_veri_string.split(',')]
        y_verileri = [float(s.strip()) for s in y_veri_string.split(',')]

        if len(x_verileri) != len(y_verileri):
            return "Hata: x ve y ekseni verilerinin sayısı eşit olmalıdır."

        plt.figure()
        plt.plot(x_verileri, y_verileri, marker='o')
        plt.title(grafik_adi)
        plt.xlabel("X Ekseni")
        plt.ylabel("Y Ekseni")
        plt.grid(True)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        return buf

    except ValueError:
        return "Hata: Lütfen geçerli sayı formatında veriler girin."

def sutun_grafik(grafik_adi, x_veri_string, y_veri_string):
    """Verilen x ve y verileriyle bir sütun grafiği oluşturur ve bayt olarak döndürür."""
    try:
        x_verileri = [s.strip() for s in x_veri_string.split(',')]
        y_verileri = [float(s.strip()) for s in y_veri_string.split(',')]

        if len(x_verileri) != len(y_verileri):
            return "Hata: x ve y ekseni verilerinin sayısı eşit olmalıdır."

        plt.figure()
        plt.bar(x_verileri, y_verileri)
        plt.title(grafik_adi)
        plt.xlabel("Kategoriler")
        plt.ylabel("Değerler")
        plt.grid(True, axis='y')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        return buf

    except ValueError:
        return "Hata: Lütfen geçerli sayı formatında veriler girin."

def nokta_grafik(grafik_adi, x_veri_string, y_veri_string):
    """Verilen x ve y verileriyle bir nokta grafiği oluşturur ve bayt olarak döndürür."""
    try:
        x_verileri = [float(s.strip()) for s in x_veri_string.split(',')]
        y_verileri = [float(s.strip()) for s in y_veri_string.split(',')]

        if len(x_verileri) != len(y_verileri):
            return "Hata: x ve y ekseni verilerinin sayısı eşit olmalıdır."

        plt.figure()
        plt.scatter(x_verileri, y_verileri)
        plt.title(grafik_adi)
        plt.xlabel("X Ekseni")
        plt.ylabel("Y Ekseni")
        plt.grid(True)

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        return buf

    except ValueError:
        return "Hata: Lütfen geçerli sayı formatında veriler girin."