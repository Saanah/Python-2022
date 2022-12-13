# -*- coding: utf-8 -*-

"""
KT2
Lue käyttäjältä koenumero 4-10 väliltä. Jos käyttäjä syötti arvosanan väärin (ei väliltä 4-10) , niin tulosta "Et antanut arvosanaa annetulta väliltä". Muussa tapauksessa tulosta:

 Hyvä (jos arvosana oli 9 tai 10)

 Kelpo (jos 7 - 8)

 Tyydyttävä (jos 5 - 6)

 Heikko (jos 4)

 Toteuta ohjelma if-elif-else -rakenteella.

 Ole tarkka, että tulostat juuri sen tekstin, jota pyydettiin.

 
"""

numero = 0
numero = int(input("Anna arvosana 4-10: "))

if numero in range(4,11):
    if numero == 9 or numero == 10:
        print("Hyvä")
    elif numero == 7 or numero == 8:
        print("Kelpo")
    elif numero == 5 or numero == 6:
        print("Tyydyttävä")
    elif numero == 4:
        print("Heikko")
else:
    print("Et antanut arvosanaa annetulta väliltä")
