## GÖREV: Verilen alışveriş listelerini kullanarak aşağıdaki problemleri çözünüz
# 1 - Kullanıcı mouse almaktan vazgeçti, sepetten çıkartın
# 2 - Kullanıcı "Kulaklık" almaya karar verdi. Fiyatı 200 TL
# 3 - Sistemde hata olmuş "Kvalye" kelimesini düzeltin
# 4 - Kullanıcının ödemesi gereken tutarı hesaplayın

sepet = ["Webcam", "Mouse", "Kvalye", "Monitör"]
fiyatlar = [200, 80, 350, 3000] #  Fiyatlar sırasıyla verilmiştir

# 1. problem
sepet.pop(1)
fiyatlar.pop(1)
print(sepet)  #  ['Webcam', 'Kvalye', 'Monitör']
print(fiyatlar)
print("---------------------------") 


# 2. problem
sepet.append("Kulaklık")
fiyatlar.append(200)
print(sepet)  #  ['Webcam', 'Kvalye', 'Monitör', 'Kulaklık']
print(fiyatlar)
print("---------------------------")

# 3. problem
sepet[1] = "Klavye"
print(sepet)  #  ['Webcam', 'Klavye', 'Monitör', 'Kulaklık']
print("---------------------------")


# 4. problem
print(sum(fiyatlar))  #  3750
