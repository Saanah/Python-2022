"""

KT2

Tee luokka Tilaus, jolla on kolme jäsenmuuttujaa: tilausnumero, tuotekoodi ja maara.

Toteuta lisäksi funktiot hae_tilaukset, talleta_tilaukset sekä tulosta_tilaukset. Käytä tiedostonnimenä globaalin muuttujan filename arvoa. Käytä talletukseen JSON-formaattia.

Pääohjelma on valmiina, älä muokkaa sitä. Alla esimerkki ohjelman ajosta:


Lisataanko tilaustuote (k/e): k
Tilausnumero: a329847
Tuotekoodi: 22323
Maara: 283
Lisataanko tilaustuote (k/e): k
Tilausnumero: 383838b
Tuotekoodi: 234
Maara: 11
Lisataanko tilaustuote (k/e): e
{'tilausnumero': 'a329847', 'tuotekoodi': '22323', 'maara': 283}
{'tilausnumero': '383838b', 'tuotekoodi': '234', 'maara': 11}

"""

import json

filename="./tilaukset.json"


#Replace pass-lines with your code

class Tilaus(dict):
    def __init__(self, nro, code, amount):
        dict.__init__(self, tilausnumero = nro, tuotekoodi = code, maara = amount)
        self.__dict__ = self

def hae_tilaukset():
    tilaukset = open(filename, 'rt')
    dict_tilaukset = json.load(tilaukset)
    tilaukset.close
    return dict_tilaukset

def talleta_tilaukset(tilaukset):
    jsonTilaukset = json.dumps(tilaukset)
    wFile = open(filename, "wt")
    wFile.write(jsonTilaukset)
    wFile.close

def tulosta_tilaukset(tilaukset):
    for i in tilaukset:
        print(i)

if __name__ == '__main__':

    tilaukset = list()

    while(True):
        vast=input("Lisataanko tilaustuote (k/e): ")
        if (vast.upper() != "K"):
            break
        tilausnumero=input("Tilausnumero: ")
        tuotekoodi=input("Tuotekoodi: ")
        maara=int(input("Maara: "))
        tilaus=Tilaus(tilausnumero,tuotekoodi,maara)
        tilaukset.append(vars(tilaus))

    talleta_tilaukset(tilaukset)
    del tilaukset

    #Read JSON structure
    t_list=hae_tilaukset()
    #Print JSON structure
    tulosta_tilaukset(t_list)



