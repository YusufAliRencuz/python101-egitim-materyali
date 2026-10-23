## DRY (Don't Repeat Yourself)

# Kötü: aynı iş tekrar ediliyor
print("Merhaba Ali")
print("Merhaba Ayşe")
print("Merhaba Can")
 
# İyi: fonksiyon + döngü
def selamla(isim):
    print("Merhaba " + isim)
 
for isim in ["Ali", "Ayşe", "Can"]:
    selamla(isim)



## KISS (Keep It Simple, Stupid)

sayi = 42
# Gereksiz karmaşıklık
sayi_metni = str(sayi)
son_rakam = sayi_metni[-1]

if son_rakam == "0" or son_rakam == "2" or son_rakam == "4" or son_rakam == "6" or son_rakam == "8":
    print("Çift sayıdır")

# En sade çözüm
if sayi % 2 == 0:
    print("Çift sayıdır")



## SRP (Single Responsibility Principle)

db_listesi = []
# Kötü
def siparis_isle(fiyat, musteri_adi):
    # 1. İş: İndirim hesapla
    indirimli_fiyat = fiyat * 0.90
    
    # 2. İş: Ekrana fatura yazdır
    print(f"Sayın {musteri_adi}, ödeyeceğiniz tutar: {indirimli_fiyat} TL")
    
    # 3. İş: Veritabanına kaydet (Simülasyon)
    db_listesi.append({"musteri": musteri_adi, "tutar": indirimli_fiyat})

# İyi
def indirim_hesapla(fiyat):
    return fiyat * 0.90

def fatura_yazdir(musteri_adi, tutar):
    print(f"Sayın {musteri_adi}, ödeyeceğiniz tutar: {tutar} TL")

def veritabanina_kaydet(musteri_adi, tutar):
    db_listesi.append({"musteri": musteri_adi, "tutar": tutar})



## YAGNI (You Aren't Gonna Need It)

# Kötü
def topla(a,b,kur_farki,birim): #  İlerde döviz işleri lazım olursa diye önden hazırlık 
    return a + b                # Sonuç = Gereksiz karmaşıklık

# İyi
def topla(a,b):     # Sade, anlaşılır ve gereksiz hiçbir şey yok
    return a + b    # Eğer ihtiyaç olursa ihtiyaç anında özellikler koda eklenir



## No Magic Numbers

# Kötü
def fatura_hesapla(tutar):
    # 0.18 nedir? Neden tutarla çarpıyoruz?
    kdvli_tutar = tutar + (tutar * 0.18)
    
    # Neden 60?
    if tutar > 60:
        print("Kargo bedava!")

# İyi
KDV_ORANI = 0.18
KARGO_BEDAVA_ALTI_LIMITI = 60  # Sabitler BÜYÜK_HARFLERLE isimlendirilir.

def fatura_hesapla(tutar):
    kdvli_tutar = tutar + (tutar * KDV_ORANI)
    
    if tutar > KARGO_BEDAVA_ALTI_LIMITI:
        print("Kargo bedava!")