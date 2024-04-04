# Gerekli kütüphaneleri içe aktar
import pygame  # Pygame kütüphanesini oyun geliştirmek için kullanacağız
import random  # Rastgele sayılar üretmek için kullanacağız

# Pygame'i başlat
pygame.init()  # Pygame'i başlatır ve gerekli modülleri yükler

# Ekran boyutlarını ve renklerini tanımla
ekran_genisligi = 800  # Ekranın genişliğini 800 piksel olarak ayarlar
ekran_yuksekligi = 600  # Ekranın yüksekliğini 600 piksel olarak ayarlar
ekran = pygame.display.set_mode((ekran_genisligi, ekran_yuksekligi))  # Ekranı oluşturur
pygame.display.set_caption("Yılan Oyunu")  # Pencerenin başlığını "Yılan Oyunu" olarak ayarlar

# Renkleri tanımla (RGB formatında)
siyah = (0, 0, 0)  # Siyah renk
beyaz = (255, 255, 255)  # Beyaz renk
kirmizi = (255, 0, 0)  # Kırmızı renk
yesil = (0, 255, 0)  # Yeşil renk

# Yılanın özelliklerini tanımla
yilan_boyutu = 20  # Yılanın her bir parçasının boyutu (piksel cinsinden)
yilan_hizi = 15  # Yılanın hareket hızı (saniyede kaç kare güncelleneceği)

# Yılanın başlangıç konumunu ve yönünü belirle
x1 = ekran_genisligi / 2  # Yılanın başlangıç x koordinatı (ekranın ortası)
y1 = ekran_yuksekligi / 2  # Yılanın başlangıç y koordinatı (ekranın ortası)
x1_degisim = 0  # Yılanın x yönündeki hareketi (başlangıçta hareket yok)
y1_degisim = 0  # Yılanın y yönündeki hareketi (başlangıçta hareket yok)

# Yılanın gövdesini temsil eden liste (her parça bir [x, y] koordinat listesi)
yilan_govdesi = []

# Yemin özelliklerini tanımla
# Yemin özelliklerini tanımla (tamsayı olarak)
yem_x = random.randrange(0, ekran_genisligi - yilan_boyutu)  # Yemin rastgele x koordinatı
yem_y = random.randrange(0, ekran_yuksekligi - yilan_boyutu)  # Yemin rastgele y koordinatı

# Oyunun çalışıp çalışmadığını kontrol eden değişken
oyun_devam = True  # Oyun başlangıçta çalışıyor

# Skor değişkeni
skor = 0  # Oyunun başında skor 0

# Yazı tipi tanımla (skor için kullanılacak)
font_style = pygame.font.SysFont("bahnschrift", 25)  # Yazı tipi ve boyutu

# Skoru ekrana yazdıran fonksiyon
def skor_goster(skor):
    value = font_style.render("Skor: " + str(skor), True, beyaz)  # Skoru beyaz renkte yazdır
    ekran.blit(value, [0, 0])  # Skoru ekranın sol üst köşesine yerleştir

# Yılanı ekrana çizen fonksiyon
def yilan_ciz(yilan_boyutu, yilan_govdesi):
    for x in yilan_govdesi:  # Yılanın her bir parçası için
        pygame.draw.rect(ekran, yesil, [x[0], x[1], yilan_boyutu, yilan_boyutu])  # Yeşil dikdörtgen çiz

# Yılanın hareketini kontrol eden fonksiyon
def yilan_hareket(x1, y1, x1_degisim, y1_degisim):
    x1 += x1_degisim  # Yılanın x koordinatını güncelle
    y1 += y1_degisim  # Yılanın y koordinatını güncelle
    return x1, y1  # Güncellenmiş koordinatları döndür

# Yem yendiğinde yılanın büyümesini sağlayan fonksiyon
def yem_kontrol(x1, y1, yem_x, yem_y):
    global skor
    # Yılanın kafasının yemle çarpışma kontrolü (yılanın boyutu hesaba katılarak)
    if x1 in range(yem_x, yem_x + yilan_boyutu) and y1 in range(yem_y, yem_y + yilan_boyutu):
        # Yeni yem koordinatlarını oluştur
        yem_x = random.randrange(0, ekran_genisligi - yilan_boyutu)
        yem_y = random.randrange(0, ekran_yuksekligi - yilan_boyutu)
        skor += 1  # Skoru artır
    return yem_x, yem_y  # Güncellenmiş (veya güncellenmemiş) yem koordinatlarını döndür

# Oyunun ana döngüsü
while oyun_devam:  # Oyun devam ettiği sürece
    # Olayları kontrol et (klavye, fare vb.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Pencere kapatılırsa
            oyun_devam = False  # Oyunu durdur
        if event.type == pygame.KEYDOWN:  # Bir tuşa basılırsa
            if event.key == pygame.K_LEFT and x1_degisim != yilan_boyutu:  # Sol ok tuşu ve yılan sağa gitmiyorsa
                x1_degisim = -yilan_boyutu  # Yılanı sola hareket ettir
                y1_degisim = 0  # Dikey hareketi durdur
            elif event.key == pygame.K_RIGHT and x1_degisim != -yilan_boyutu:  # Sağ ok tuşu ve yılan sola gitmiyorsa
                x1_degisim = yilan_boyutu  # Yılanı sağa hareket ettir
                y1_degisim = 0  # Dikey hareketi durdur
            elif event.key == pygame.K_UP and y1_degisim != yilan_boyutu:  # Yukarı ok tuşu ve yılan aşağı gitmiyorsa
                y1_degisim = -yilan_boyutu  # Yılanı yukarı hareket ettir
                x1_degisim = 0  # Yatay hareketi durdur
            elif event.key == pygame.K_DOWN and y1_degisim != -yilan_boyutu:  # Aşağı ok tuşu ve yılan yukarı gitmiyorsa
                y1_degisim = yilan_boyutu  # Yılanı aşağı hareket ettir
                x1_degisim = 0  # Yatay hareketi durdur

    # Yılanın ekran sınırlarını aşma kontrolü
    if x1 >= ekran_genisligi or x1 < 0 or y1 >= ekran_yuksekligi or y1 < 0:  # Yılan sınırlara çarptıysa
        oyun_devam = False  # Oyunu durdur

    # Yılanın kendi gövdesine çarpma kontrolü
    for x in yilan_govdesi[:-1]:  # Yılanın gövdesindeki her parça için (kafa hariç)
        if x == [x1, y1]:  # Yılanın kafası gövdeye çarptıysa
            oyun_devam = False  # Oyunu durdur

    # Yılanın hareketini ve yem kontrolünü gerçekleştir
    x1, y1 = yilan_hareket(x1, y1, x1_degisim, y1_degisim)  # Yılanı hareket ettir
    yem_x, yem_y = yem_kontrol(x1, y1, yem_x, yem_y)  # Yem kontrolü yap

    # Yılanın gövdesini güncelle
    yilan_kafa = []  # Yılanın yeni kafasını temsil eden liste
    yilan_kafa.append(x1)  # Yılanın yeni kafa x koordinatını ekle
    yilan_kafa.append(y1)  # Yılanın yeni kafa y koordinatını ekle
    yilan_govdesi.append(yilan_kafa)  # Yeni kafayı yılanın gövdesine ekle

    # Yılanın boyunu kontrol et ve gerekiyorsa kuyruğu kısalt
    if len(yilan_govdesi) > skor + 1:  # Yılanın boyu skordan büyükse
        del yilan_govdesi[0]  # Kuyruğu kısalt (ilk parçayı sil)

    # Ekranı temizle ve yeniden çiz
    ekran.fill(siyah)  # Ekranı siyahla doldur
    pygame.draw.rect(ekran, kirmizi, [yem_x, yem_y, yilan_boyutu, yilan_boyutu])  # Yemi kırmızı dikdörtgen olarak çiz
    yilan_ciz(yilan_boyutu, yilan_govdesi)  # Yılanı çiz
    skor_goster(skor)  # Skoru yazdır
    pygame.display.update()  # Ekranı güncelle

    # Oyun hızını ayarla (saniyede yilan_hizi kadar kare)
    pygame.time.Clock().tick(yilan_hizi)

# Pygame'i kapat
pygame.quit()  # Pygame'i kapat
quit()  # Programı sonlandır