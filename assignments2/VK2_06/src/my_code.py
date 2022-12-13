# -*- coding: utf-8 -*-

"""
KT6
Kysy käyttäjältä mitä hän haluaa seuraavista vaihtoehdoista (eli käyttäjä syöttää joko numeron 0, 1, 2 tai 3) :

   0 = Lopetus
   1 = Anna säde
   2 = Laske ympyrän piiri
   3 = Laske ympyrän pinta-ala

   Anna valintasi:

Tulosta kysymys edellä kuvatulla tavalla.

Muu kuin 0,1,2,3 vastaa nollaa eli päättää ohjelman toiminnan.

Vaihtoehto 0 päättää ohjelman

Vaihtoehto 1 kysyy ympyrän säteen.  Säteen oletusarvo on nolla (0.0)

Vaihtoehto 2 tulostaa ympyrän piirin (laskukaava on piiri = 2 * pii * säde)

Vaihtoehto 3 tulostaa ympyrän alan (laskukaava on  ala = pii * sade * sade) pinta-ala ja tulosta se.

Jos vaihtoehto on ollut 1,2,3, niin toimenpiteiden (syöttö/tulostus) jälkeen tulostetaan edellä kuvattu  vaihtoehtokysymys uudelleen

Hae piin arvo math moduulista (koodin alkuun import math ja sen jälkeen pii saadaan  math.pi muuttujasta)

Tulosta kaikki desimaaliluvut kahden desimalin tarkkuudella.

Esimerkkiajo ohessa

0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 1
Anna säde: 12


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 2
Piiri on 75.40


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 3
Ala on 452.39


0 = Lopetus
1 = Anna säde
2 = Laske ympyrän piiri
3 = Laske ympyrän pinta-ala
Anna valintasi: 0

"""
syotto = 4
valinta = 4
sade = 0.0
piiri = 0.0
pinta_ala = 0.0
pii = 3.14159265359

while valinta != 0:
   print('\n 0 = Lopetus \n 1 = Anna säde \n 2 = Laske ympyrän piiri \n 3 = Laske ympyrän pinta-ala')

   syotto = input("\n Anna valintasi: ")

   try:
      valinta = int(syotto)

   except:
      valinta = 0

   if valinta == 1:
      sade = float(input("\n säde: "))
   elif valinta == 2:
        piiri = 2 * pii * sade
        print(f'\n Piiri on {piiri:.2f}')
   elif valinta == 3:
      pinta_ala = pii * (sade ** 2)
      print(f'\n Ala on {round(pinta_ala, 2)}')
   else:
      valinta = 0
