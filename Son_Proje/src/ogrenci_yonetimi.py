def ogrenci_ekle(liste, ogrenci_adi):
    # Listeye ekleme işlemi yapar]
    liste.append(ogrenci_adi)
    return liste

def ogrencileri_listele(liste):
    # for döngüsü ile listenin elemanları üzerinde sırayla geziniriz
    for ogrenci in liste:
        print("- " + ogrenci)