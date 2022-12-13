# -*- coding: utf-8 -*-

"""
KT3

Kysy käyttäjältä ensin kieli (Suomi = 0/ Englanti =1). Oletuskieli on suomi, eli muu kuin 0/1 tarkoittaa suomenkielistä tulostusta.
Määrittele koodissa viikonpäivien(ma, ti ke..) tekstit yhteen listaan, jossa on alkio/päivä eli siis molempien kielien viikonpäivänimet (esim Maanatai/Monday].
Kyse on siis rakenteesta lista listassa.

Ota käyttöön muuttuja (dictonary-tyyppinen), johon voit tallentaa maanantain ja perjantain välisenä aikana neljä mittaustulosta
jokaiselta päivältä (mittaustulos on sademäärä milleinä). Lue käyttäjältä nämä mittaustulokset ja
laske vasta lopuksi ja tulosta jokaisen päivän mittaustulosten keskiarvo yhdellä desimaalilla seuraavan esimerkin mukaisesti :

Maanantai:      12.0 mm
Tiistai:        0.0 mm
Keskiviikko:    1.9 mm
Torstai:        22.8 mm
Perjantai:      0.9 mmål

Esimerkkiajo ohessa:
Millä kielellä /Please choose language (0 = suomi, 1 = english): 1
Monday 1. : 3
Monday 2. : 2
Monday 3. : 4
... Säästetty tilaa...
Friday 2. : 6
Friday 3. : 5
Friday 4. : 3

Monday 3.5 mm
Tuesday 3.2 mm
Wednesday 4.0 mm
Thursday 4.2 mm
Friday 4.8 mm

Syötteiden järkevyydestä ei tarvitse välittää!

Ole taas huolellinen tulostusten kanssa!

"""

viikonpaivat = [['Maanantai', 'Monday'], ['Tiistai', 'Tuesday'], ['Keskiviikko', 'Wednesday'], ['Torstai', 'Thursday'], ['Perjantai', 'Friday'], ['Lauantai', 'Saturday'], ['Sunnuntai', 'Sunday']]
sademaarat = {}
sadePerPaiva = 0.0
summa = 0.0
keskiarvo = 0.0
kieli = 0
paivanNimi = ''

kieli = int(input("Millä kielellä /Please choose language (0 = suomi, 1 = english): "))

if(kieli == 0 or kieli == 1):
    kieli = kieli
else:
    kieli = 0

for paivat in range(5):
        for paiva in range(4):
            paivanNimi = viikonpaivat[paivat][kieli] + ' ' + str(paiva+1) + "."
            sadePerPaiva = float(input(f'{paivanNimi} : '))
            sademaarat[paivanNimi] = sadePerPaiva

for paivienKeskiarvo in range(5):
    for paiva in range(4):
            paivanNimi = viikonpaivat[paivienKeskiarvo][kieli] + ' ' + str(paiva+1) + "."
            summa += sademaarat.get(paivanNimi)
    keskiarvo = summa / 4.0
    print(f"{viikonpaivat[paivienKeskiarvo][kieli]} {round(keskiarvo, 1)} mm")
    keskiarvo = 0.0
    summa = 0.0
    