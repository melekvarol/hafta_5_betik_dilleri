kim.py

url ='https://www.milligazete.com.tr/arsiv/2021-07-'
def tarih_yaz(gun):
    for i in range(1+gun+1,1):
        if i<10:
        print(url+'0'+str(i))
    else:
        print(url+str(i))
tarih_yaz(28)
