## GÖREV: Kullanıcıyı selamlayıp doğduğu yılı isteyin. Bilgiyi kullanarak yaşını hesaplayıp yazdırın

print("Hoş Geldiniz!")

dogum_yili = input("Lütfen doğduğunuz yılı giriniz:")

print("Yaşınız hesaplanıyor...")

# print(type(dogum_yili))

dogum_yili = int(dogum_yili)

# print(type(dogum_yili))

yas = 2026 - dogum_yili

print(f"Yaşınız: {yas}")
