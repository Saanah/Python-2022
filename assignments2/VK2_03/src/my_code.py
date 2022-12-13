# -*- coding: utf-8 -*-

"""
KT3

Tee ohjelma, joka pyytää käyttäjää syöttämään lampotila -nimiseen muuttujaan jonkin mielivaltainen lämpötilan arvon (mieti tyyppi tarkasti kun ensin katsot alla olevaa...). Ohjelman tulee siis hyväksyä esim lämpötila 22.5.

Ohjelma tulostaa sitten seuraavasti, kun lämpötila on:

>39 tulostuu : Liian kuuma
<=39 ja >10 tulostuu : Lämmintä
<=10 ja >=0 tulostuu : Haaleaa
<0 ja >-30 tulostuu : Pakkasta
<=-30 tulostuu : Liian kylmää

Toteuta ohjelma if-elif-else -rakenteella.

Ole tarkka, että tulostat juuri sen tekstin, jota pyydettiin!
"""

lampotila = 0.0

lampotila = float(input("Anna lämpötila ilman celsiusta: "))

if lampotila > 39.0:
    print("Liian kuuma")
elif 10.0 < lampotila <= 39.0:
    print("Lämmintä")
elif 0.0 <= lampotila <= 10.0:
    print("Haaleaa")
elif -30.0 < lampotila < 0.0:
    print("Pakkasta")
elif lampotila <= -30.0:
    print("Liian kylmää")