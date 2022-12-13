"""
KT4

Pääset suunnittelemaan Tuote-sovellusta suuren kauppaketjun tuotekehitysosastolla. Tehtävänäsi on suunnitella luokkarakenne, jolla voidaan hallinnoida yrityksen tuotteita. Kaikilla tuotteilla on samat yhteiset ominaisuudet: nimi, hinta, hyllypaikka sekä koodi. Nämä esitellään tuote-luokassa, jonka aliluokat perivät. Aliluokkia on kolme, joilla on omia ominaisuuksia:

a.                         vaate: koko, materiaali
b.                         ruoka: maa, paivays
c.                         kodinkone: takuu, paino 

Tee yksinkertainen ohjelma, jolla voit syöttää tuotteita yhdelle tuotelistalle sekä tulostaa koko listan sisällön.
Luokkien jäsenmuuttujien tyyppejä ei ole määritelty eli saat päättää ne itse. (Testi ei päästä läpi kuin string :( möh )) Ohjelmassa ensin valitaan minkä tyyppistä tuotetta ollaan syöttämässä, jonka jälkeen tiedot täytetään. Miten lopetat syötön on sinun päätettävissä. Tietysti lopuksi lista tulostetaan.

Ohessa esimerkkiajo:

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: 1
Anna tuotteen nimi: Sokeri
Anna hinta: 2.45
Anna hyllypaikka: Ruoka 11
Anna koodi: 111-222-333-22
Ruuan alkuperämaa: Tanska
Päiväys: 1.3.2024

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: 2
Anna tuotteen nimi: Paita
Anna hinta: 22.10
Anna hyllypaikka: Vaate 3
Anna koodi: 222-122-232-11
Vaatteen koko: M
Vaatteen materiaali: Puuvilla

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: 3
Anna tuotteen nimi: Pakastin
Anna hinta: 320.00
Anna hyllypaikka: Varasto 12
Anna koodi: 543-234-232-22
Kodinkoneen takuu: 1 vuosi
Kodinkoneen paino: 100kg

Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus: l

Nimi:       Sokeri
Hinta:      2.45
Hylly:      Ruoka 11
Koodi:      111-222-333-22
Alkuperä:   Tanska
Päiväys:    1.3.2024

Nimi:       Paita
Hinta:      22.10
Hylly:      Vaate 3
Koodi:      222-122-232-11
Koko:       M
Materiaali: Puuvilla

Nimi:       Pakastin
Hinta:      320.00
Hylly:      Varasto 12
Koodi:      543-234-232-22
Takuu:      1 vuosi
Paino:      100kg

"""

from datetime import datetime
#Write class and imports here!


class tuote:
   
    def __init__(self, nimi, hinta, hyllypaikka, koodi):
        self.nimi = nimi
        self.hinta = hinta
        self.hyllypaikka = hyllypaikka
        self.koodi = koodi

class vaate(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, koko, materiaali):
        super().__init__(nimi, hinta, hyllypaikka, koodi)
        self.koko = koko
        self.materiaali = materiaali
        
class ruoka(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, maa, paivays):
        super().__init__(nimi, hinta, hyllypaikka, koodi)
        self.maa = maa
        self.paivays = paivays
    
class kodinkone(tuote):
    def __init__(self, nimi, hinta, hyllypaikka, koodi, takuu, paino):
        super().__init__(nimi, hinta, hyllypaikka, koodi)
        self.takuu = takuu
        self.paino = paino


if __name__ == "__main__":

    tuoteLista = []

    while True:

        tuoteInput = input("Mikä tuote lisätään listaan (1 = Ruoka, 2 = Vaate, 3 = Kodinkone, muu = Lopetus ")

        if not(tuoteInput == '1' or tuoteInput == '2' or tuoteInput == '3'):
            break

        nimi = input("Anna tuotteen nimi: ")
        hinta = input("Anna hinta: ")
        hyllypaikka = input("Anna hyllypaikka: ")
        koodi = input("Anna koodi: ")

        if tuoteInput == '1':

            maa = input("Ruuan alkuperämaa: ")
            paivays = input("Päiväys: ")
         
            tuoteLista.append(ruoka(nimi, hinta, hyllypaikka, koodi, maa, paivays))

        elif tuoteInput == '2':
       
            koko = input("Vaatteen koko: ")
            materiaali = input("Vaatteen materiaali: ")

            tuoteLista.append(vaate(nimi, hinta, hyllypaikka, koodi, koko, materiaali))


        elif tuoteInput == '3':
              
            takuu = input("Kodinkoneen takuu: ")
            paino = input("Kodinkoneen paino: ")

            tuoteLista.append(ruoka(nimi, hinta, hyllypaikka, koodi, takuu, paino))
  
    for t in tuoteLista:
        if isinstance(t, tuote):
            print("Nimi: \t" + t.nimi)
            print("Hinta: \t" , t.hinta)
            print("Hylly: \t" + t.hyllypaikka)
            print("Koodi: \t" + t.koodi)
            if isinstance(t, vaate):
                print("Koko: \t" + t.koko)
                print("Materiaali: \t" + t.materiaali)
            elif isinstance(t, ruoka):
                print("Alkuperä: \t" + t.maa)
                print("Päiväys: \t" + t.paivays)
            elif isinstance(t, kodinkone):
                print("Takuu: \t" + t.takuu)
                print("Paino: \t" + t.paino)