import matplotlib.pyplot as plt

def kullanicidan_veri_al(mesaj):
    while True:
        veri = input(mesaj)
        try:
            liste = [float(i.strip()) for i in veri.split(',')]
            return liste
        except ValueError:
            print("Hatalı giriş!")

def main():
    print("Çizgi Grafiği\n")

    x = kullanicidan_veri_al("X ekseni verilerini girin : ")
    y = kullanicidan_veri_al("Y ekseni verilerini girin : ")

    if len(x) != len(y):
        print("Hata: X ve Y verileri farklı uzunlukta olmalı!")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, marker='o', linestyle='-', linewidth=2)
    plt.title("Çizgi Grafiği")
    plt.xlabel("X Ekseni")
    plt.ylabel("Y Ekseni")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
