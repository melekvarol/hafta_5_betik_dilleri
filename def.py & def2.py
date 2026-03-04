def.py
from def2 import *
for i in A :
    k1=(i.split(' '))
    w1=''
    for vord in range(len(k1)):
        if vord==0:
            pass
        else:
            w1+=k1[vord]+' '
    print(w1)
  
def2.py
A=[
    "15:26 Ateşkes umurların da mı?! Terörist İsrail ordusu Lübnan'a yine saldırı düzenledi!",
"15:25 Dem Parti’den çift taraflı İran açıklaması… Dışardan müdahale olmasın, içeriden rejim değiştirilsin!",
"15:01 Bakan Uraloğlu'ndan açıklama! Hürmüz Boğazı'ndaki Türk gemilerinin durumu belli oldu",
"14:37 Yaşadıkları hezi̇meti̇n görüntülenmesi̇ni̇ i̇stemi̇yorlar…. CNN Türk muhabi̇ri̇ ve kameramanı gözaltına alındı",
"14:36 Shamdasani: 'İran'da 153 öğrenci ve öğretmenin hayatını kaybettiği saldırıyla ilgili soruşturma çağrısında bulunuyoruz",
"14:23 Maneviyat herkesi heyecanlandırdı! Gaziantep'te 'Mukaddes Emanetler Sergisi' ziyarete açıldı",
"14:12 Hangi il kaç vekil çıkaracak! İl il milletvekili sayıları...Artan ve azalan iller",
"14:07 ABD dezenformasyon çabasında Bekayi, ABD Özel Temsilcisi Witkoffu yalanladı",
"12:46 47 yıldır ambargo altında ama attığı füzeler dünya gündeminde: ABD’den trilyonca dolarlık silah alan ülkelerin hali ise ibretlik!",
"12:40 Macron konuşma yapmaya 4 savaş uçağıyla gitti"
]
url ='https://www.milligazete.com.tr/arsiv/2021-07-'
arr=[]

for i in range(1,31,1):
    if i<10:
        print(url+'0'+str(i))
    else:
        print(url+str(i))
