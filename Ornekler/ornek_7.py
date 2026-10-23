def bilgi(ad, yas=18):
    print(ad, yas)
 
bilgi("Ali")              # Ali 18
bilgi(yas=20, ad="Ayşe")  # Ayşe 20
 
def topla(*sayilar):
    return sum(sayilar)
print(topla(1, 2, 3))     # 6
 
x = 10             # global
def f():
    x = 5          # local
    return x
print(f(), x)      # 5 10

 
y = 10             # global
def f2(y):
    y = 5          # local
    return y
print(f2(y), y)      # 5 10
 