# -*- coding: utf-8 -*-

#
# KT2
#
# Kysy käyttäjältä, montako lukua arvotaan.Jos käyttäjä syöttää arvon < 1, tulostuu "Virhe!"
# Tee lista ja arvo siihen em määrä lukuja  väliltä 0-20.
# Vain parilliset luvut sallitaan.
# Jos arvottiin pariton luku niin sen tilalle on arvottava uusi luku.
# Tulosta luvuista suurin ja pienein samalle riville
# Ja lopuksi tulosta arvotut luvut yhdelle riville pilkulla erotettuna
# Huomaa, että viimeisen luvun jälkeen ei tule pilkkua
#
# Esimerkkiajo ohessa
#
# Montako lukua arvotaan: 3
# Suurin: 6 ja pienin: 0
# 4,0,6
#

import random

amount = 0
lista = []
flag = True

amount = int(input("Kuinka montalukua arvotaan: "))

if(amount < 1):
    print("Virhe!")
else:
    for x in range(amount):
        flag = True
        while flag:
            aLuku = random.randrange(0,21)
            if(aLuku % 2 == 0):
                lista.append(aLuku)
                flag = False       
    
print(f'Suurin: {max(lista)} ja pienin: {min(lista)}')
print(*lista, sep = ",") 
