import math

## YUVARLAMA İŞLEMLERİ
sonuc = None

sonuc = math.ceil(4.1) # 5 --- Tavana yuvarlar (Küsurat ne olursa olsun bir üst tam sayıya)
print(sonuc)

sonuc = math.floor(4.9) # 4 --- Tabana yuvarlar (Küsurat ne olursa olsun bir alt tam sayıya)
print(sonuc)

sonuc = math.trunc(4.9) # 4 --- Noktadan sonrasını kesip atar (Sadece tam kısmı alır)
print(sonuc)

sonuc = round(4.3) # 4 --- En yakın tam sayıya yuvarlar (Küsurat .5'ten küçük)
print(sonuc)


## TEMEL MATEMATİKSEL İŞLEMLER
sonuc = math.sqrt(16) # 4.0 --- Karekök alır (Float tipinde değer döndürür)
print(sonuc)

sonuc = math.pow(2, 3) # 8.0 --- Üs alma işlemi (2 üzeri 3)
print(sonuc)

sonuc = math.fabs(-15) # 15.0 --- Mutlak değer alır (Eksi işaretini kaldırır)
print(sonuc)

sonuc = math.factorial(5) # 120 --- Faktöriyel hesaplar (5 * 4 * 3 * 2 * 1)
print(sonuc)

sonuc = math.gcd(12, 18) # 6 --- En Büyük Ortak Bölen (EBOB) bulur
print(sonuc)


## MATEMATİKSEL SABİTLER (Fonksiyon değildir, parantez '()' kullanılmaz!)
sonuc = math.pi # 3.141592653589793 --- Pi sayısı
print(sonuc)

sonuc = math.e # 2.718281828459045 --- Euler sayısı
print(sonuc)