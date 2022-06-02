import requests
from bs4 import BeautifulSoup
url= 'https://www.python.org/'
response = requests.get(url)
#print(response.status_code) #200 olursa web sitesini parçalayabilirim.
content = response.content
soup =BeautifulSoup(content, 'lxml')
#print(soup)
#print(soup.prettify()) #Daha düzenli geliyor.
#print(soup.title) #title nini öğrendik
#print(soup.title.text) #title yazısını etiketsiz çektik.
#print(soup.find('ul'))
#print(soup.find('ul').text)
#print(soup.find_all('ul'))
#for i in soup.find_all('ul'):
#    print(i)
#   print('/////////////////////////////////////////')
#for i in soup.find_all('div', class_ = 'top-bar do-not-print'):
 #   print(i)
#for links in soup.find_all('a'):
#    print(links)
#for links in soup.find_all('a'):
 #   print(links.text)

# Çoklu yorum satırı ctlr+ / ile yaparsın.
# for links in soup.find_all('a'):
#     print(links.get("href"))

# for links in soup.find_all('a', limit = 5):
#     print(links)

print(soup.find('ul').select('li:nth-of-type(3)'))