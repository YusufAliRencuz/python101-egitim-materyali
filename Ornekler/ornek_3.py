## ELEMANA ERİŞİM ve BİLGİ ALMA (Listelerdeki Mantığın Aynısı)
metin = "Python Programlama Dili"
sonuc = None

sonuc = len(metin) # 23 --- Karakter sayısını (uzunluğunu) verir
print(sonuc)

sonuc = metin[0] # 'P' --- İlk karakter
print(sonuc)

sonuc = metin[-1] # 'i' --- Son karakter
print(sonuc)

sonuc = metin[0:6:1] # 'Python' --- [başlangıç:bitiş:adım sayısı]
print(sonuc)

sonuc = metin[::-1] # 'iliD amalmargorP nohtyP' --- Metni tersten yazdırır
print(sonuc)

sonuc = metin.count("a") # 3 --- 'a' harfinin metinde kaç kere geçtiği
print(sonuc)

sonuc = metin.index("Programlama") # 7 --- Aranan kelimenin başladığı ilk index
print(sonuc)


## HARF DÖNÜŞÜMLERİ ve METİN TEMİZLEME
metin = "  python PROGRAMLAMA  "

sonuc = metin.upper() # "  PYTHON PROGRAMLAMA  " --- Tüm harfleri büyük yapar
print(sonuc)

sonuc = metin.lower() # "  python programlama  " --- Tüm harfleri küçük yapar
print(sonuc)

sonuc = metin.title() # "  Python Programlama  " --- Her kelimenin ilk harfini büyük yapar
print(sonuc)

sonuc = metin.strip() # "python PROGRAMLAMA" --- Baştaki ve sondaki gereksiz boşlukları temizler
print(sonuc)

sonuc = metin.replace("python", "Java") # "  Java PROGRAMLAMA  " --- Belirtilen metni yenisiyle değiştirir
print(sonuc)


## ARAMA ve KONTROL İŞLEMLERİ
dosya_adi = "rapor_2026.pdf"

sonuc = dosya_adi.startswith("rapor") # True --- Metin "rapor" ile mi başlıyor?
print(sonuc)

sonuc = dosya_adi.endswith(".pdf") # True --- Metin ".pdf" ile mi bitiyor?
print(sonuc)

sonuc = "2026" in dosya_adi # True --- Metnin içinde "2026" geçiyor mu? (Operatör kullanımı)
print(sonuc)


## BÖLME ve BİRLEŞTİRME (Koleksiyonlarla Kesişim Noktası)
kurslar = "Python,Data,Web,AI"

liste_hali = kurslar.split(",") # ['Python', 'Data', 'Web', 'AI']
                                 # Metni virgüle göre bölüp LİSTE yapar!
print(liste_hali)

birlestirilmis = " - ".join(liste_hali) # "Python - Data - Web - AI"
                                         # Listenin elemanlarını tire ile birleştirip STR yapar!
print(birlestirilmis)


## METİN BİÇİMLENDİRME (f-string)
ad = "Yusuf"
dil = "Python"

mesaj = f"Merhaba {ad}, {dil} dersine hoş geldin!" # Metin içine doğrudan değişken yerleştirir
print(mesaj)


# !!! ÖNEMLİ KURAL (IMMUTABILITY - DEĞİŞTİRİLEMEZLİK):
# String'ler değiştirilemez (immutable) yapılardır! Listelerdeki gibi 'metin[0] = "J"' yapılamaz (Hata verir).
# Bütün String metotları (upper, replace, strip vb.) mevcut metni DEĞİŞTİRMEZ, geriye YENİ bir metin döndürür.
# Bu yüzden sonuçları görmek için ya print() içine yazmalı ya da yeni bir değişkene atamalıyız!