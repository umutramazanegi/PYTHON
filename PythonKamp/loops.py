sehirler=["Ankara","İstanbul","İzmir"]
for sehir in sehirler:
    print(sehir)
for sayi in range(1,10,2):  #0 ile başlatsaydım çift sayileri yazacakti.
    print(sayi)

sayac=1
while sayac<10:
    print(sayac)
    sayac=sayac+1

isim=input("Adiniz")
print("isim: "+ isim)

sayi = int(input("Sayi :"))

#faktoriyel alma yap 3.45de devam et https://www.youtube.com/watch?v=6IWpowC2ryc&list=PLqG356ExoxZWbfIhu2C7b0dKIGHKeGKcM

sayi = int(input("Sayi gir :"))
faktoriyel=1
if sayi<0:
    print("Sayi 0 dan küçük girilmez")
elif sayi ==0:
    print("Sonuc: 1")
else:
    for i in range(1,sayi+1):
        faktoriyel=faktoriyel*i
        print("Sonuc: ", faktoriyel)