## GÖREV_1: Kullanıcıdan vize ve final notlarını kullanarak ortalama hesaplayan bir fonksiyon yazınız. (Vize: %40, Final: %60)
## GÖREV_2: Hesaplanan ortalamayı kullanarak harf notu hesaplayan bir fonksiyon yazınız.

def ortalama_hesapla(vize,final):
    vize_yüzdelik = vize * 0.4
    final_yüzdelik = final * 0.6
    return vize_yüzdelik + final_yüzdelik

def harf_notu(ortalama):
    if ortalama >= 80:
        return "AA"
    elif ortalama >= 60:
        return "BB"
    elif ortalama >= 40:
        return "CC"
    else:
        return "FF"

## ------------------------------------

vize_notu = int(input("Lütfen vize notunuzu giriniz:\n"))
final_notu = int(input("Lütfen final notunuzu giriniz:\n"))

ortalama = ortalama_hesapla(vize_notu,final_notu)
sonuc = harf_notu(ortalama)
print(f"Harf notunuz: {sonuc}")