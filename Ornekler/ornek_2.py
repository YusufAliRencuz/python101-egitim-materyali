## ELEMANA ERİŞİM ve BİLGİ ALMA
liste = ["Ali", "Ahmet", "Cemile", "Kerem", "Selin", "Elif", "Haydar"]
sonuc = None

sonuc = len(liste) #  7
print(sonuc)

sonuc = liste[1:4:1] #  ["Ahmet", "Cemile", "Kerem"] --- list[başlangıç:bitiş:adım sayısı]
print(sonuc)

sonuc = liste.count("Ali") #  1 --- Ali'nin listede kaç kere geçtiği
print(sonuc)

sonuc = liste.index("Selin") #  4 --- Selin'in listede ilk defa geçtiği index
print(sonuc)

## ELEMAN EKLEME, SİLME ve GÜNCELLEME
liste = ["Ali", "Ahmet", "Cemile", "Kerem", "Selin", "Elif", "Haydar"]


liste.append("Osman") # Listenin sonuna Osman eklenir
print(liste)

liste.insert(2, "Yusuf") #  Listenin 2. indexine Yusuf eklenir
print(liste)

liste[3] = "Eftelya" #  3. indexteki Cemile yerine Eftelya yazıldı
print(liste)

silinen = liste.pop() #  Son elemanı siler (Osman) ve bunu silinen değişkenine atar
print(silinen)
silinen = liste.pop(5) #  5. indexteki elemanı siler (Selin) ve bunu silinen değişkenine atar
print(silinen)
print(liste)


## SIRALAMA
liste = ["Ali", "Ahmet", "Cemile", "Kerem", "Selin", "Elif", "Haydar"]

liste.sort() #  Listeyi küçükten büyüğe sıralar
print(liste)

liste.reverse() # Listeyi tersine çevirir
print(liste)

yeni_liste = liste.copy() # Listenin bir kopyasını oluşturur
                          # !! "=" ile oluşturulmasından farklı olarak bellekteki referansı farklı bir liste oluşturur.
                          # Bu sayede birbirlerini etkilemeyen iki farklı liste elde ederiz


## MATEMATİKSEL İŞLEMLER
sayilar = [1, 2, 3, 4, 5]
sonuc = 0

sonuc = max(sayilar) # Sayısal elemanlardan en büyüğünü bulur. Stringleri alfabetik olarak kıyaslardı
print(sonuc)

sonuc = min(sayilar) # Sayısal elemanlardan en küçüğünü bulur.
print(sonuc)

sonuc = sum(sayilar) # Sayısal koleksiyon elemanlarının toplamını hesaplar.
print(sonuc)


# !!! Doğrudan liste üzerinde değişiklik yapan işlemlerle değişkene atama yapılamaz, sadece mevut liste değiştirilir.
# Örneğin: append, sort...
