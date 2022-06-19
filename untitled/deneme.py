import cv2
import numpy as np
from matplotlib import pyplot as plt  #kütüphaneler
kamera = cv2.VideoCapture(0, cv2.CAP_DSHOW)  #kamerayı çalıştırma
kamera.set(cv2.CAP_PROP_FRAME_WIDTH,420)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT,500)  #kamera pencere ölçek ayarı
while True:
    _,frame = kamera.read()  #kamerayı okutma
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #kamerayı gri hale getirme
    edges =cv2.Canny(gray,30,100) #edges ile kenar bulma
    sobel_vertical = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5) #Kenarları tespit etmek için Sobel filtrelerini kullandım
    laplacian = cv2.Laplacian(frame, cv2.CV_64F) #Kenarları tespit etmek için laplacian filtrelerini kullandım
    cv2.imshow("edges ile kenar bulma kaydetmek icin e tusuna bas", edges)
    cv2.imshow("sobel ile kenar bulma(vertical)  kaydetmek icim s tusuna bas",sobel_vertical)  #Görüntüyü ekrana getirdim
    cv2.imshow("laplacian ile kenar bulma kaydetmek icin l tusuna bas ",laplacian)
    anahtar = cv2.waitKey(1)
    if anahtar == ord('q'):
        print("Programdan cıkıs")
        break
    elif anahtar == ord('e'):
        dosya_adi = 'resim/edges.png'
        cv2.imwrite(dosya_adi, edges)
    elif anahtar == ord('s'):
        dosya_adi= 'resim/sobel.png'
        cv2.imwrite(dosya_adi,sobel_vertical)
    elif anahtar == ord('l'):
        dosya_adi = 'resim/laplacion.png'
        cv2.imwrite(dosya_adi, laplacian)
kamera.release()
cv2.destroyAllWindows()