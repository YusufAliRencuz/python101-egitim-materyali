ogrenciler = ["Ahmet", "Ali", "Cenk", "Ayşe"]
for ogrenci in ogrenciler: #  Listedeki tüm öğrencileri döndürür
    print(f"Merhaba {ogrenci}")


for i in range(1,10): #  1-9 arası sayıları döndürür (10 dahil değil)
    print(i)


fiyatlar = [100, 200, 250, 150, 300] 
toplam = 0
for fiyat in fiyatlar:  #  200 TL üzerindeki fiyatları toplar
    if fiyat >= 200:
        toplam += fiyat
print(toplam)


ogrenciler = ["Ahmet", "Ali", "Cenk", "Ayşe"]
for index, ogrenci in enumerate(ogrenciler, start=1):  #  Öğrecilerin index bilgisini de kullanmak için enumerate kullandık. 
    print(f"{index}. öğrenci {ogrenci}")               # Index'i saymaya 1'den başlattık


fiyatlar = [100, 200, 250, 150, 300, 450, 500]
toplam = 0
for fiyat in fiyatlar: 
    if fiyat < 200: # 200'den küçükse sonrakine geç
        continue
    elif fiyat > 400: # 400'den büyükse sonrakine geç
        continue
    toplam += fiyat
print(toplam)


sayilar = [1, 3, 4, 5]
for i in sayilar:
    if i%2 == 0: # Çift sayı varsa döngüyü sonlandırır
        break
    print(i)