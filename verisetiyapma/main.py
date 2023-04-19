# Gerekli kütüphaneleri içe aktar
import cv2
import sys
import os

# Yüz tanıma için kullanılacak model dosyasının adı
haar_file = "haarcascade_frontalface_default.xml"

# Veri setinin kaydedileceği klasörün adı
datasets = "datasets"

# Tanımak istediğiniz kişinin adı
sub_data = "mustafa"

# Veri setindeki kişiye ait klasörün yolu
path = os.path.join(datasets, sub_data)

# Eğer klasör yoksa oluştur
if not os.path.isdir(path):
    os.mkdir(path)

# Yüzleri yeniden boyutlandırmak için kullanılacak genişlik ve yükseklik değerleri
(width, height) = (130, 100)

# Yüz tanıma modelini yükle
face_cascade = cv2.CascadeClassifier(haar_file)

# Webcam'i aç
webcam = cv2.VideoCapture(0)

# Kaydedilecek resim sayısı
count = 1

# Kaydedilecek resim sayısı kadar döngüye gir
while count < 300:
    # Webcam'den bir kare oku
    (_, im) = webcam.read()
    # Kareden gri tonlamalı bir görüntü elde et
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Gri görüntüde yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, 1.3, 4)
    # Algılanan her yüz için
    for (x, y, w, h) in faces:
        # Yüzün etrafına bir dikdörtgen çiz
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Yüzü kare içinden kırparak al
        face = gray[y:y + h, x:x + w]
        # Yüzü yeniden boyutlandır
        face_resize = cv2.resize(face, (width, height))
        # Yüzü veri setindeki ilgili klasöre kaydet
        cv2.imwrite('%s/%s.png' % (path, count), face_resize)
        # Kaydedilen resim sayısını arttır
        count += 1

    # Kameradan gelen görüntüyü ekranda göster
    cv2.imshow('OpenCV', im)
    # Klavyeden bir tuşa basılırsa
    key = cv2.waitKey(10)
    # Eğer tuş ESC ise döngüden çık
    if key == 27:
        break

# Webcam'i kapat
webcam.release()
# Pencereyi kapat
cv2.destroyAllWindows()