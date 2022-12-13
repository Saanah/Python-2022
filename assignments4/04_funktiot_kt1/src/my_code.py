"""
KT1


Tee ohjelma, jossa kysytään KysyJaTestaaLuku() nimisessä funktiossa  käyttäjältä kokonaisluku. 

Funktio palauttaa kokonaislukuarvon seuraavasti:

 

1, jos syötetty luku on positiivinen.
0, jos syötetty luku on nolla.

-1, jos syötetty luku on negatiivinen. 

 

Tulosta näiden paluuarvojen perusteella pääohjelmassa ilmoitus ruudulle.


”Luku oli positiivinen”, jos paluuarvo oli 1.
”Luku oli nolla”, jos paluuarvo oli 0
”Luku oli negatiivinen”, jos paluuarvo oli -1.

"""

#Write KysyJaTestaaLuku function here!
def KysyJaTestaaLuku():

    palautettavaLuku = 0
    luku = int(input("Anna kokonaisluku: "))

    if(luku > 0):
        palautettavaLuku = 1
        return palautettavaLuku
    elif(luku == 0):
        return palautettavaLuku
    elif(luku < 0):
        palautettavaLuku = -1
        return palautettavaLuku


if __name__ == "__main__":
    #Write main program below this line
    saatuLuku = KysyJaTestaaLuku()
    if(saatuLuku == 1):
        print("Luku oli positiivinen")
    elif(saatuLuku == -1):
        print("Luku oli negatiivinen")
    elif(saatuLuku == 0):
        print("Luku oli nolla")
