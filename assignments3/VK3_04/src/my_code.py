# -*- coding: utf-8 -*-

"""
KT 4

Kysy käyttäjältä lukujjen määrä ja arvo annettu  kplmäärä  liukulukuja väliltä 1 – 100.
Arvo luku seuraavasti:
    random_decimal = random.randint(100, 10000) / 100
Tulosta arvottu luku käyttäjälle (samalle riville kuin edellinen välilyönnillä erotettuna) ja kirjoita se arvot.txt tiedostoon allekkain.
Jos syötetty luku on < 1, ei ohjelma päättyy ja tulostuu "Virhe!".

Jos tiedosto on jo olemassa, vanhat tiedot menetetään
Älä käytä listaa tms tässä vaiheessa vaan vie luku tiedostoon heti, kun se on arvottu.
Sen jälkeen lue arvot tiedostosta listaan ja lajittele se. Tämän jälkeen tulosta listan  arvot sekä vie
lukujen kplmäärä, summa, keskiarvo, minimiarvo ja maksimiarvo tulokset.txt -tiedostoon
oheisen mallin mukaisesti kahdella desimaalilla (pl kpl):
Kpl: 2
Sum:5.00
Ka: 2.50
Min: 1.00
Max:4.00

Ohessa ajoesimerkki:

Montako lukua arvotaan? 3
Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt:
75.41 12.84 17.27
Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt:
12.84 17.27 75.41
Ja lopuksi  tiedostosta tulokset.txt löytyy seuraavat tiedot:
Lkm: 3
Sum: 105.52
Ka: 35.17
Min: 12.84
Max: 75.41

Ole taas huolellinen tulostusten kanssa!

"""
from pdb import line_prefix
import random

lukujenMaara = 0
arvotutLuvut = ""
luetutLuvut = []
luetutLuvutLajiteltu = []
summa = 0
keskiarvo = 0
minimi = 0
maximi = 0

lukujenMaara = int(input("Montako lukua arvotaan? "))

if lukujenMaara < 1:
    print("Virhe!")
else:
    file_object = open('arvot.txt','wt')
    for arvo in range(lukujenMaara):
        random_decimal = str(random.randint(100, 10000) / 100)
        file_object.write(random_decimal + "\n")
        arvotutLuvut += random_decimal + " "
    file_object.close()

    print("Arvottiin seuraavat luvut ja talletetaan tiedostoon arvot.txt: ")
    print(arvotutLuvut)

    rfile_object = open('arvot.txt', 'rt')
    lines = rfile_object.readlines()
    for line in lines:
        luetutLuvut.append(float(line.strip('\n')))
    rfile_object.close()

    print("Luettiin seuraavat luvut (lajiteltuna) tiedostosta arvot.txt: ")
    luetutLuvut = sorted(luetutLuvut, key = float)
    print(*luetutLuvut, sep = " ")

    """
    arvojen laskeminen:
    """

    for luku in luetutLuvut:
        summa += luku
    
    keskiarvo = summa/lukujenMaara

    minimi = min(luetutLuvut)
    maximi = max(luetutLuvut)

    file_object_tulokset = open('tulokset.txt','wt')
    file_object_tulokset.write("Lkm: " + str(lukujenMaara) + "\n")
    file_object_tulokset.write("Summa: " + "{:.2f}".format(summa)+ "\n")
    file_object_tulokset.write("Ka: " + "{:.2f}".format(keskiarvo) + "\n")
    file_object_tulokset.write("Min: " + "{:.2f}".format(minimi) + "\n")
    file_object_tulokset.write("Max: " + "{:.2f}".format(maximi) + "\n")

    file_object_tulokset.close()

print("Ja lopuksi  tiedostosta tulokset.txt löytyy seuraavat tiedot: ")
rfile_object = open('tulokset.txt', 'rt')
lines = rfile_object.readlines()
for line in lines:
    print(line.strip("\n"))
rfile_object.close()
   