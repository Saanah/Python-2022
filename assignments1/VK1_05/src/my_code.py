# -*- coding: utf-8 -*-

"""

KT5

Esittele muuttuja pii, jolle annat alkuarvoksi piin likiarvon 6 desimaalin tarkkuudella.
Lue käyttäjältä ympyrän halkaisija ja tulosta ympyrän piiri ja pinta-ala kahden desimaalin tarkkuudella

Malli ohessa:

Anna ympyrän halkaisija: 12
Piiri on 37.70
Pinta-ala on 113.10

"""
pii = 3.141593

halkaisija = float(input("Anna ympyrän halkaisija: "))

piiri = pii * halkaisija
pinta_ala = (pii * (halkaisija ** 2))/4

print('Piiri on ' + format(piiri,'.2f'))
print('Pinta-ala on ' + format(pinta_ala,'.2f'))

