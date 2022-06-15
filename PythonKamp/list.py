urunler=["laptop","mause","klavye"]
print(urunler)
urunler.append("Telefon")
print(urunler)

ogrenciler1=["Mehmet","Murat","Sabri"]
ogrenciler2=["Ali","Mehmet","Ayşe"]
ogrenciler1 = ogrenciler2
ogrenciler2[0]= "Engin"
print(ogrenciler1[0])

sayi1=10
sayi2=20
sayi1=sayi2
sayi2 =60
print(sayi2)  #60 sonucu verdi
print(sayi1)  #20 sonucunu verdi.