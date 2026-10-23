class OyunKarakteri:
    def __init__(self, isim, rol, can):
        self.isim = isim  # self.isim -> "Bu objenin ismi = dışarıdan gelen isim"
        self.rol = rol
        self.can = can

    # Karakterin Yetenekleri (Metotlar)
    def saldir(self):
        print(f"{self.isim} silahını savurdu! Düşmana hasar verdi.")
        
    def durum_goster(self):
        print(f"Karakter: {self.isim} | Sınıf: {self.rol} | Kalan Can: {self.can}")


# -------------------------------------------------------------
# 2. KALIPTAN GERÇEK KARAKTERLER (OBJELER) ÜRETİYORUZ

karakter1 = OyunKarakteri("Arthur", "Savaşçı", 100)
karakter2 = OyunKarakteri("Merlin", "Büyücü", 80)

# 3. OBJELERİ KULLANMA
karakter1.durum_goster()  # Arthur'un bilgilerini yazar
karakter2.saldir()        # Merlin saldırı yapar