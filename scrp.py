scrp.py

import bs4
import requests
from bs4 import BeautifulSoup
dizi=[]
url='https://www.nytimes.com/arsiv/2021-07-26'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')

def get_link_prostatkanseri(i):
    dizi=[]
    r = requests.get(i)
    soup = BeautifulSoup(r.content, 'html5lib')
    url = 'https://www.cumhuriyet.com.tr'
    for a in soup.find_all('a', href=True):
        link = a['href']
        result = link.startswith("https://www.gazeteduvar.com.tr/")
        if result == True:
            result2 = link.startswith("https://www.gazeteduvar.com.tr/arsiv?")
            if result2 == False:
                if len(link)>57:
                    with open("gazeteduvar_link_prostat_kanser.txt", 'a') as file:
                        file.write(link+'\n')
                        dizi.append(link)
    tarih = '09.02.2025'
    date = tarih.split('.')
    print(date[0])
    for i in date:
        print(i)
    return dizi
