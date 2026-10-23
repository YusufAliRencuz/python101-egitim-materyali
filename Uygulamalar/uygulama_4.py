## GÖREV: Kullanıcıdan aşağıdaki kurallara göre bir şifre alınız
# 1 - 8 karakter uzunluğunda olmalı
# 2 - En az bir sayı, bir küçük harf ve bir büyük harf olmalı
# 3 - Şifrenin başında veya sonunda boşluk olamaz

while True:
    sifre = input("Lütfen yeni şifrenizi girin: ")
    
    if len(sifre) != len(sifre.strip()):
        print("-> Hata: Şifrenin başında veya sonunda boşluk olamaz!\n")
        continue

    if len(sifre) < 8:
        print("-> Hata: Şifre en az 8 karakter olmalıdır!\n")
        continue

    # 3. Büyük Harf ve Rakam Kontrolü (Döngü ile)
    buyuk_harf_var_mi = False
    kucuk_harf_var_mi = False
    rakam_var_mi = False

    for karakter in sifre:
        if karakter.isupper():
            buyuk_harf_var_mi = True
        if karakter.islower():
            kucuk_harf_var_mi = True
        if karakter.isdigit():
            rakam_var_mi = True

    # Koşul Kontrolleri
    if not buyuk_harf_var_mi:
        print("-> Hata: Şifreniz en az bir büyük harf içermelidir!\n")
    elif not kucuk_harf_var_mi:
        print("-> Hata: Şifreniz en az bir küçük harf içermelidir!\n")
    elif not rakam_var_mi:
        print("-> Hata: Şifreniz en az bir rakam içermelidir!\n")
    else:
        print(f"\n Tebrikler! '{sifre}' güçlü bir şifre olarak kaydedildi.")
        break
