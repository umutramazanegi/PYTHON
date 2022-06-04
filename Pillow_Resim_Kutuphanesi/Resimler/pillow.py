from  PIL import Image #resim kütüphanesini cagirdik
resim = Image.open('resim.jpg')   # resim degiskenine resmi actiriyoruz
resim.save('kaydedilmis_resim.jpg') # resmi kaydediyoruz.
resim.save('uzantidegistiresim.png') #uzantisini degistirdik.
yeni_resim = resim.rotate(90)   #resmi 90 derece dondurduk
#yeni_resim.show()
yeni_resim.save('90derecedondurma.jpg')
#resim.rotate(45).show() #farkli dondurma islemi

# boyut =(475,290) #boyut belirledim.
# resim.thumbnail(boyut)
# resim.save('boyutlanmisresim.jpg')

# kordinatlar = (250,90,960,698)  #resmin kordinatlarini belirledim
# kesilmis_resim = resim.crop(kordinatlar)  #kesme islemini yaptim
# kesilmis_resim.show() #resmi gösterdim.
# kesilmis_resim.save('kesilmis_resim.jpg')

# from PIL import ImageGrab #ekran görüntüsü almak icin kutuphane
# sc=ImageGrab.grab()
# sc.save('sc.png')
# sc.show()

# img =Image.open('resim2.jpg') # normal resim
# yeni_img = img.convert(mode='L') #resmi griye cevrildi
# img.show()
# yeni_img.show()

#filitreleri uygulamak icin kutuphane yuklemek gerek
from  PIL import ImageFilter
new_resim =Image.open('resim.jpg')
#new_resim.show()
# new_resimm = new_resim.filter(ImageFilter.BLUR)
# new_resimm.show()
# new_resimm.save('blurluresim.jpg')

# new_resimm = new_resim.filter(ImageFilter.CONTOUR)
# new_resimm.show()
# new_resimm.save('contourresim.jpg')

# new_resimm = new_resim.filter(ImageFilter.DETAIL)
# new_resimm.show()
# new_resimm.save('detailresim.jpg')

# new_resimm = new_resim.filter(ImageFilter.EDGE_ENHANCE) #resmi guzellestirdi.
# new_resimm.show()
# new_resimm.save('edge_enhanceresim.jpg')

# new_resimm = new_resim.filter(ImageFilter.EDGE_ENHANCE_MORE)
# new_resimm.show()
# new_resimm.save('edge_enhance_moreresim.jpg')

# new_resimm = new_resim.filter(ImageFilter.EMBOSS)
# new_resimm.show()
# new_resimm.save('embossresim.jpg')

# new_resimm = new_resim.filter(ImageFilter.FIND_EDGES)
# new_resimm.show()
# new_resimm.save('Fınd_edgesceresim.jpg')

# new_resimm = new_resim.filter(ImageFilter.SMOOTH)
# new_resimm.show()
# new_resimm.save('smothresim.jpg')

# new_resimm = new_resim.filter(ImageFilter.SMOOTH_MORE)
# new_resimm.show()
# new_resimm.save('smothmoreresim.jpg')

new_resimm = new_resim.filter(ImageFilter.SHARPEN) #keskinlestirdi.
new_resimm.show()
new_resimm.save('sharpenresim.jpg')