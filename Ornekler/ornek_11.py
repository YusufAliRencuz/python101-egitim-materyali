import random

## RASTGELE TAM SAYI ÜRETME
sonuc = None

sonuc = random.randint(1, 6) # 4 --- 1 ile 6 arasında rastgele tam sayı (1 ve 6 DAHİL)
print(sonuc)

sonuc = random.randrange(0, 100, 5) # 45 --- 0'dan 100'e kadar 5'in katı olan rastgele bir tam sayı
print(sonuc)


## RASTGELE ONDALIKLI (FLOAT) SAYI ÜRETME
sonuc = random.random() # 0.4729... --- 0.0 ile 1.0 arasında rastgele float sayı üretir
print(sonuc)

sonuc = random.uniform(1.5, 9.5) # 4.821... --- Belirtilen iki sınır arasında rastgele float sayı üretir
print(sonuc)


## LİSTE VE DİZİLERDEN SEÇİM YAPMA
meyveler = ["Elma", "Muz", "Çilek", "Karpuz"]

sonuc = random.choice(meyveler) # 'Çilek' --- Listeden tek bir rastgele eleman seçer
print(sonuc)

sonuc = random.sample(meyveler, 2) # ['Muz', 'Elma'] --- Listeden benzersiz (tekrarsız) 2 eleman seçer
print(sonuc)

sonuc = random.choices(meyveler, k=3) # ['Muz', 'Muz', 'Çilek'] --- Listeden tekrar edebilen k kadar eleman seçer
print(sonuc)


## LİSTE SIRASINI KARIŞTIRMA
iskambil_destesi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random.shuffle(iskambil_destesi) # Değer döndürmez, listenin kendi sırasını yerinde karıştırır
print(iskambil_destesi) # [3, 8, 1, 10, 2, 5, 7, 4, 9, 6] --- Karıştırılmış liste


## SABİT RASTGELELİK (TEST VE SİMÜLASYON İÇİN)
random.seed(42) # Rastgelelik çekirdeğini sabitleyerek her çalıştırmada aynı sonucun çıkmasını sağlar
sonuc = random.randint(1, 100) # Her bilgisayarda ve her çalıştırmada '82' verir
print(sonuc)