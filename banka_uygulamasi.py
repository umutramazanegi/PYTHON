kartSifresi = "1905"
bakiye = 1000
denemeHakki = 3
print("X Bankasina hos geldiniz")
kartislemDurumu = True
islemDurumu = True
while islemDurumu:
    girilenSifre = input("Kart sifrenizi giriniz: ")
    if girilenSifre != kartSifresi:
        print("Yanlis sifre giriniz. Tekrardan Deneyiniz. ")
        denemeHakki -= 1
        print(denemeHakki, "deneme hakkiniz kaldi")
        if denemeHakki ==0:
            print("Kartiniz bloklandi. Banka ile gorusunuz")
            islemDurumu = False
    else:
        print("Giris yapildi")
        print("""
            Yapilacak islemi Seciniz
            1- Para Cekme
            2- Para Yatirma
            3- Bakiye Sorgula
            4- Cikis
            """)
        while kartislemDurumu:
            islemNo = input("islem numarsi seciniz")
            if islemNo == "4":
                print("Cikis yapildi")
                islemDurumu = False
                kartislemDurumu = False
            elif islemNo == "3":
                print("Toplam Bakiye:",bakiye,"₺") #Alt Gr + T 
            elif islemNo == "2":
                yatirilacakMiktar = int(input("Yatirilacak Miktar giriniz: "))
                bakiye = bakiye + yatirilacakMiktar
                print("islem gerceklesmistir")
            elif islemNo == "1":
                cekilenMiktar = int(input("Cekikecek miktar giriniz:"))
                if cekilenMiktar > bakiye:
                    print("Yetersiz Bakiye..")
                else:
                    bakiye = bakiye - cekilenMiktar
                    print("islem gerceklesmistir")
