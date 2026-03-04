xyz.py
def duzgunlestir(arr):
    for i in arr:
        x=(i.split('-'))
        isim=''
        for parca in x:
            isim +=(parca.strip())#boşluk siler
        print('=====')
        print(isim)

  xyz2.py
from xyz import *
iller=['anka   -ra','istan  -bul', 'iz   -mir', 'bur  -sa']
duzgunlestir(iller)
for i in iller:
    print(i)
for i in iller:
    k=i.split('-')
    ayberk=''
    for j in k:
        ayberk+=j.strip()
        print(ayberk)
