import math
from random import randint, shuffle

def rastgele_sec(liste):
    # Listenin uzunluğuna göre rastgele bir indeks seçer
    maksimum_indeks = len(liste) - 1
    secilen_indeks = randint(0, maksimum_indeks)
    return liste[secilen_indeks]

def grup_sayisi_hesapla(kisi_sayisi, grup_kapasitesi):
    # Kişi sayısını kapasiteye bölüp math.ceil ile yukarı yuvarlar
    bolum = kisi_sayisi / grup_kapasitesi
    return math.ceil(bolum)

def ogrencileri_karistir(liste):
    # Orijinal listeyi korumak için kopya alınıyor
    kopya_liste = liste.copy() 
    
    # Sadece kopya liste karıştırılıyor
    shuffle(kopya_liste) 
    return kopya_liste