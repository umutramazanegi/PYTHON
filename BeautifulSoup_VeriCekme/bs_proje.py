import requests
from bs4 import BeautifulSoup #Kutuphaneyi cagirdim
url = 'https://www.sondakika.com/' #web sitenin adini girdim
response = requests.get(url)
#print(requests.status_code) #200 dondu parçalayabiliriz.
content = response.content
soup = BeautifulSoup(content, 'lxml')

# links =soup.find_all('li', limit=10)
# for i in links:
#     print(i.a.text)
#Sondakikadaki haberlerin basliklerini cektim.
item = soup.find_all('div',class_ = 'news-row' )
for div in item:
    #print(div)
    try:
        baslik = div.div.text
        print("Haber baslıgi: ", baslik)
        link = div.a.get('href')
        #print(link)
        #
        response2 = requests.get('https://www.sondakika.com/' + link)
        content2 = response2.content
        soup2 = BeautifulSoup(content2, 'lxml')
        item2=soup2.find_all('div',class_ ='wrapper detay-v3_3 haber_metni pad-bot-20')
        for i in item2.find_all('p' or 'h3'):
            print("Haber icerikleri: ", i.text)



    except:
        pass