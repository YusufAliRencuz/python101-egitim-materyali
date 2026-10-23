dogruluk = True
sayi = 0
while dogruluk:
    print(sayi)
    sayi += 1
    if sayi == 10:
        dogruluk = False  #  sayi 10'a varınca döngüyü sonlandır


sayi = 0
while True:
    print(sayi)
    sayi += 1
    if sayi == 10:
        break  #  sayi 10'a varınca döngüyü sonlandır


sayi = 0
while True:
    if sayi == 5:  #  sayi 5 ise atla 
        sayi += 1
        continue
    elif sayi == 10:  #  sayi 10'a varınca döngüyü sonlandır
        break
    else:
        print(sayi)
        sayi += 1