# Gerekli kütüphaneleri içe aktar
import cv2
import sys
import numpy as np
import os

# Yüz tanıma için kullanılacak model dosyasının adı
haar_file = "haarcascade_frontalface_default.xml"

# Veri setinin kaydedildiği klasörün adı
datasets = "datasets"

# Veri setindeki kişilerin isimlerini ve etiketlerini tutan listeler
names = []
labels = []
images = []  # Veri setindeki yüz resimlerini tutan liste

# Veri setindeki tüm klasörleri gez
for (subdirs, dirs, files) in os.walk(datasets):
    # Her klasör için
    for subdir in dirs:
        # Klasör adını isim listesine ekle
        names.append(subdir)
        # Klasörün içindeki tüm dosyaları gez
        for filename in os.listdir(os.path.join(datasets, subdir)):
            # Dosyanın tam yolunu al
            path = os.path.join(datasets, subdir, filename)
            # Dosyayı gri tonlamalı olarak oku
            image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            # Resmi yeniden boyutlandır
            image = cv2.resize(image, (130, 100))
            # Resmi etiket listesine ekle
            labels.append(names.index(subdir))
            # Resmi images listesine ekle
            images.append(image)
            # Resmi göster (isteğe bağlı)
            cv2.imshow("Training...", image)
            cv2.waitKey(10)

# Listeleri numpy dizisine dönüştür
names = np.array(names)
labels = np.array(labels)
images = np.array(images)

# Yüz tanıma modelini yükle
face_cascade = cv2.CascadeClassifier(haar_file)

# Yüz tanıma modelini eğit
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

# Webcam'i aç
webcam = cv2.VideoCapture(0)

# Webcam'den gelen görüntüleri işlemeye başla
while True:
    # Webcam'den bir kare oku
    (_, im) = webcam.read()
    # Kareden gri tonlamalı bir görüntü elde et
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Gri görüntüde yüzleri algıla
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Algılanan her yüz için
    for (x, y, w, h) in faces:
        # Yüzün etrafına bir dikdörtgen çiz
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # Yüzü kare içinden kırparak al
        face = gray[y:y + h, x:x + w]
        # Yüzü yeniden boyutlandır
        face_resize = cv2.resize(face, (130, 100))
        # Yüzü tanımaya çalış
        prediction = model.predict(face_resize)
        # Tanıma sonucunu isim listesinden al
        name = names[prediction[0]]
        # Tanıma sonucunu ekrana yazdır
        cv2.putText(im, '%s - %.0f' % (name, prediction[1]), (x - 10, y - 10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

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