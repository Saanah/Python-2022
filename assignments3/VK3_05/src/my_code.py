# -*- coding: utf-8 -*-

"""
KT 5

Kirjoita Python-kielinen ohjelma, joka kysyy käyttäjän nimeä, kuitenkin enintään 18 merkkiä.
Merkeissä saa olla tyhjeitä. Jos merkkejä > 18, tulostuu teksti "Virhe!".
Ohjelma tulostaa nimen alla kuvatusti laskevana ja pituudesta riippumatta sivusuunnassa alkaen oikeasta reunasta.
Jotta teksti hahmottuisi riviksi, lisää kaksi välilyöntiä perättäisten merkkien väliin. Kirjoita tämä myös nimi.txt-tiedostoon samassa muodossa.

Esimerkkiajo:
Anna nimesi:Jukka
        a
      k
    k
  u
J

"""
nimi = " "

nimi = input("Anna nimesi:")
nimiLopustaAlkuun = nimi[::-1]
if len(nimi) > 18:
  print("Virhe!")
else:
  pituus = len(nimi)
  spacePituus = pituus-(len(nimi)-2)
  spaces = "  "
  wfile = open('nimi.txt', 'wt')
  for i in range(pituus):
    vali = i+1
    print(spaces * (pituus-vali) + nimiLopustaAlkuun[i])
    wfile.write(str(spaces * (pituus-vali)) + str(nimiLopustaAlkuun[i]) + "\n")
