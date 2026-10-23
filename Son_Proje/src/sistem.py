from src.ogrenci_yonetimi import ogrenci_ekle, ogrencileri_listele
from src.araclar import rastgele_sec, grup_sayisi_hesapla, ogrencileri_karistir

def uygulamayi_baslat():
    ogrenciler = ["Ahmet", "Ayşe", "Mehmet", "Zeynep", "Can"]
    calisiyor = True
    
    while calisiyor: # İşlem gerçekleşene kadar döngü devam eder
        print("\n--- KURA VE GRUP SİSTEMİ ---")
        print("1 - Öğrencileri Listele")
        print("2 - Yeni Öğrenci Ekle")
        print("3 - Şanslı Öğrenciyi Seç")
        print("4 - Grup Sayısı Hesapla")
        print("0 - Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == "0":
            print("Çıkış yapılıyor...")
            calisiyor = False
        elif secim == "1":
            print("Kayıtlı Öğrenciler:")
            ogrencileri_listele(ogrenciler)
        elif secim == "2":
            yeni_kisi = input("Eklenecek öğrencinin adı: ")
            ogrenci_ekle(ogrenciler, yeni_kisi)
            print(yeni_kisi + " listeye eklendi!") 
        elif secim == "3":
            if len(ogrenciler) > 0: # Liste uzunluğu kontrolü
                sansli = rastgele_sec(ogrenciler)
                print("Şanslı Öğrenci: " + sansli)
            else:
                print("Listede öğrenci yok!")
        elif secim == "4":
            kisi = len(ogrenciler)
            kapasite_metin = input("Bir grupta kaç kişi olacak? ")
            # Kullanıcıdan gelen metni integer (tam sayı) tipine çeviriyoru
            kapasite = int(kapasite_metin) 
            
            if kapasite > 0: # Belirli koşulun sağlanması durumu
                grup_sayisi = grup_sayisi_hesapla(kisi, kapasite)
                print("Gereken grup sayısı: " + str(grup_sayisi)) 
                print("Gruplama için karışık liste: ")
                ogrencileri_listele(ogrencileri_karistir(ogrenciler))
            else:
                print("Kapasite 0'dan büyük olmalıdır.")
        else:
            print("Hatalı seçim yaptınız.")