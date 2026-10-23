## GÖREV: Verilen kirli veriyi isim ve email olarak ikiye ayırın. Bunları temiz bir formata sokun ve ekrana yazdırın.

girilen_veri = "   yUsUf aLi ; yusuf.ali@GMAIL.com   "

veri_listesi = girilen_veri.split(";") # ['   yUsUf aLi ', ' yusuf.ali@GMAIL.com   ']  !! list olarak döner

ham_isim = veri_listesi[0].strip()
ham_email = veri_listesi[1].strip()

temiz_isim = ham_isim.title()      # "Yusuf Ali"
temiz_email = ham_email.lower()    # "yusuf.ali@gmail.com"

print(f"Kullanıcı Adı: {temiz_isim} | İletişim: {temiz_email}")