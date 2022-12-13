"""
KT1

Tee kaksi lambda-funktiota:
* summa saa parametrinaan kaksi lukua ja palauttaa niiden summan
* tulo saa parametrinaan kaksi lukua ja palauttaa niiden tulon

Tee laske-funktio, joka saa parametrinaan funktion ja listan lukuja. Funktio palauttaa listassa olevien lukujen tulon tai summan riippuen kumpaa em lambda-funktiota käytettiin funktion kutsussa. Jos luvut-lista on tyhjä, niin palautetaan 0 ja jos luvut sisältää vain yhden alkion, niin palautetaan tämä alkio.

VIHJE: Jos lista=[1, 2, 3], niin voit laskea alkioiden summan, s,  summa-funktion avulla näin:

s=summa(summa(1, 2), 3) .

Vastaava pätäee myös tuloon.


Pääohjelma on valmiina, älä muokkaa sitä.

Esimerkkitulostus:
1320
28
4
4
0
0

"""
#Write lambdas and laske here

summa = lambda x, y: x+y
tulo = lambda x, y: x*y

def laske(function, luvut):
   
    tulos = 0                                           #Returning zero if the array is empty

    if function == summa and luvut:                     #Checking the lambda function and if luvut is not empty        

        for luku in range(0,len(luvut)):
            tulos = function(tulos, luvut[luku])        #A bit too complicated and clunky answer, but works. Takes the most recent tulos and adds the next number to it.

    if function == tulo and luvut:                      

        tulos = 1                                       #Making sure the first number isn't multiplied with zero

        for luku in range(0,len(luvut)):
            tulos = function(tulos, luvut[luku])        #Multiplies the numbers in the array

    return tulos


#Don't touche lines below
if __name__ == "__main__":
    luvut = [1,5,8,11,3]
    print(laske(tulo, luvut))
    print(laske(summa, luvut))

    luvut = [4]
    print(laske(tulo, luvut))
    print(laske(summa, luvut))

    luvut = []
    print(laske(tulo, luvut))
    print(laske(summa, luvut))
