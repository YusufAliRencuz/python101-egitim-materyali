## GÖREV: Para yatırma, çekme ve bakiye sorgulama yapabilen BankaHesabi isimli bir sınıf oluşturun

class BankaHesabi:
    def __init__(self, hesap_sahibi, bakiye):
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye

    def para_cek(self, miktar=int):
        self.bakiye -= miktar
        print(f"Hesabınızdan {miktar} TL çekildi")

    def para_yatir(self, miktar=int):
        self.bakiye += miktar
        print(f"Hesabınıza {miktar} TL yatırıldı")

    def sorgula(self):
        print(f"Sayın {self.hesap_sahibi} hesabınızda {self.bakiye} TL vardır")


hesap1 = BankaHesabi("Ayşe", 5000)

hesap1.para_cek(2000)
hesap1.para_yatir(3000)
hesap1.sorgula()