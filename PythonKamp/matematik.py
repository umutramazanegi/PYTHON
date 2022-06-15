class Matematik:
    def __init__(self,sayi1,sayi2): #uygulama calısırkenki blog construction (yapıcı blog) degerleri ilk defa olustururken yapilandirmak icin kullaniriz
        self.s1 = sayi1
        self.s2 = sayi2
    def topla(self):
        return self.s1 + self.s2
    def cıkar(self):
        return self.s1 - self.s2
    def bol(self):
        return self.s1 / self.s2
    def carp(self):
        return self.s1 * self.s2

matematik=Matematik()
sonuc=matematik.topla(3,5)
print("Sonuc: "+ str(sonuc))

class Istatistik(Matematik):  #inheritance
    def __init__(self,sayi1,sayi2):
        super().__init__(sayi1,sayi2) #base baz alıyor demek.
    def varyansHesapla(self):
        return self.s1 * self.s2
istatistik =Istatistik()
