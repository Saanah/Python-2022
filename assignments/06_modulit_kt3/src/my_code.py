"""
KT3

Tutustu omatoimisesti NymPy-kirjastoon. Käytä tutustumiseen vaikkapa w3schools-sivustoa. Tee yksi esimerkkiohjelma, jossa käytät ko kirjastoa sekä selitä se python-kommenteissa. Esimerkkisovellus on vapaavalintainen.




"""
#imports here
import numpy as np

class Pelaaja:

    def __init__(self, nimi, pisteet) :
        self.nimi = nimi
        self.pisteet = pisteet

    def lisaaPiste(self):
        self.pisteet += 1

    def arvoSilmaluvut(self):
        self.silmaluvut = np.random.randint(7, size = 3)  #Arvotaan kolme lukua väliltä 0-6

        self.summaaLuvut()
    
    def summaaLuvut(self):
        
        self.summa = np.sum(self.silmaluvut) #Summataan arrayssa olevat luvut

    def vertaa(self, arvaus, vertausLuku):

        if arvaus == 's' and self.summa > vertausLuku:
            return True
        elif arvaus == 'p' and self.summa < vertausLuku:
            return True
        else:
            return False


        

if __name__ == '__main__':

    #Turhan pitkä main aka syötetään pelaajat, arvotaan vertausluku ja kysytään onko tulevien heittojen summa suurempi vai pienempi
    #kuin arvottu vertausluku. Jos pelaaja arvaa oikein hän saa pisteen. Pelataan 3 kierrosta ja lasketaan pisteet.
    #Lopuksi verrataan, kumpi on voittaja.

    nimi = input("Anna pelaaja 1 nimi: ")
    p1 = Pelaaja(nimi, 0)
    nimi = input("Anna pelaaja 2 nimi: ")
    p2 = Pelaaja(nimi, 0)


    for kierros in range(3):
        print(f"\n[KIERROS {kierros+1}]\n")
        vertausLuku = np.random.randint(19, size = 1) #Arvotaan kirjastolla yksi kokonaisluku 0-18 väliltä

        #Pelaaja 1
        print("Pelaajan", p1.nimi, "vuoro")
        arvaus = input(f"Arvaa, onko heitettävien lukujen summa suurempi vai pienempi kuin {vertausLuku} (s/p): ")
        p1.arvoSilmaluvut()

        print("\nPelaaja", p1.nimi, "heitti luvut:", p1.silmaluvut)
        print("Lukujen summa on: ", p1.summa)
        if(p1.vertaa(arvaus, vertausLuku)):
            p1.lisaaPiste()
            print(f"Oikein! Pelaajan {p1.nimi} pisteet: {p1.pisteet}\n")
        else:
            print("Väärin! Ei pisteitä!\n")

        #Pelaaja 2
        print("Pelaajan", p2.nimi, "vuoro")
        arvaus = input(f"Arvaa, onko heitettävien lukujen summa suurempi vai pienempi kuin {vertausLuku} (s/p): ")
        p2.arvoSilmaluvut()

        print("\nPelaaja", p2.nimi, "heitti luvut:", p2.silmaluvut)
        print("Lukujen summa on: ", p2.summa)
        if(p2.vertaa(arvaus, vertausLuku)):
            p2.lisaaPiste()
            print(f"Oikein! Pelaajan {p2.nimi} pisteet: {p2.pisteet}")
        else:
             print("Väärin! Ei pisteitä!")

    if p1.pisteet > p2.pisteet:
        print(f"\nPelaaja {p1.nimi} voitti pistetilillä {p1.pisteet}! Onneksi olkoon!")
    elif p1.pisteet < p2.pisteet:
        print(f"\nPelaaja {p2.nimi} voitti pistetilillä {p2.pisteet}! Onneksi olkoon!")
    else:
        print("\nTasapeli!")

        



