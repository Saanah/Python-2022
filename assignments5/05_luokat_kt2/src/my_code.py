"""
KT2


Olet aloittanut osakesijoittamisen ja haluat arvioida sijoituksesi arvoa. Ohjelmalla (pääohjelmassa) on lista, johon käyttäjä voi lisätä Osake-olioita. Ohjelma kysyy käyttäjältä ”Lisätäänkö uusi osake (k/e)”.
Kun osakkeet on lisätty listaan, kysyy ohjelma käyttäjältä kuvitteellisen kasvuprosentin sekä ajanjakson vuosina.


Tee luokka Osake, jolla on jäsenmuuttujat:
- nimi
- ostohinta (>0, osakekohtainen ostohinta)
- maara (> 0, omistettujen osakkeiden lkm)



Osakkeella on metodit:

- tulosta_arvo, jonka parametreina on  kasvuprosentin ja ajanjakson vuosina (tässä järjestyksessä). tulosta_arvo-metodi kutsuu toista Osake-luokan  metodia laske_tuotto_yhdelle_vuodelle,
joka laskee vuosikohtaisen tuoton. tulosta_arvo kutsuu laske_tuotto_yhdelle_vuodelle-metodia vuosien lukumäärän verran. Siis, jos lasketaan tuottoa kolmelle vuodelle,
niin laske_tuotto_yhdelle_vuodelle kutsutaan kolme kertaa. Huomio "korkoa korolle". Valuutat tulostetaan kahden desimaalin tarkkuudella.

- laske_tuotto_yhdelle_vuodelle -metodi palauttaa tuoton yhdelle vuodelle. Metodi on staattinen ja saa parametrinaan kasvuprosentin ja hinnan vuoden alussa (tässä järjesyksessä).

Laske pääohjelmassa  myös koko osakepotin arvo(sama % ja samat vuodet) käymällä lista läpi eli 
joudut miettimään sitä, miten pääohjelmaan palautetaan tieto yhden osakkeen potin arvosta vuosien jälkeen.

Esimerkkiajo:


Anna osakkeen nimi: Nokia
Anna osakkeen ostohinta/kpl: 10
Anna ostettujen osakkeiden lukumäärä: 1000
Lisää osakkeita (k/e)? k

Anna osakkeen nimi: Fortum
Anna osakkeen ostohinta/kpl: 12
Anna ostettujen osakkeiden lukumäärä: 127
Lisää osakkeita (k/e)? e

Anna kasvuprosentti: 5
Anna vuodet: 3

Nokia 1000 10.0
Osakkeen potin arvo on 11576.25 ja tuotto 1576.25

Fortum 127 12.0
Osakkeen potin arvo on 1764.22 ja tuotto 240.22

Koko potin arvo on 13340.47
"""
#Write class and imports here!
class Osake:

    def __init__(self, nimi, ostohinta, maara):
        self.nimi = nimi
        if ostohinta <= 0:
            ostohinta = 1
        self.ostohinta = ostohinta
        if maara <= 0:
            maara = 1
        self.maara = maara

    def tulosta_arvo(self, kasvuprosentti, vuodet):

        tuottoVuosi = 0
        potinArvo = 0
        hintaVuodenAlussa = self.ostohinta

        for vuosi in range(vuodet):
            tuottoVuosi = self.laske_tuotto_yhdelle_vuodelle(kasvuprosentti, hintaVuodenAlussa)
            hintaVuodenAlussa = tuottoVuosi
        potinArvo = tuottoVuosi * self.maara
        tuotto = potinArvo - self.ostohinta * self.maara
        print(f"Osakkeen potin arvo on {potinArvo:.2f} ja tuotto {tuotto:.2f}")
        
        return potinArvo

    @staticmethod
    def laske_tuotto_yhdelle_vuodelle(kasvuprosentti, ostohinta):
        tuottovuosi = ostohinta
        tuottovuosi += ostohinta * (kasvuprosentti / 100)
        return tuottovuosi

if __name__ == "__main__":
    #Write main program here
    osakkeet = []
    kokoPotti = 0

    while True:
        
        nimi = input("Anna osakkeen nimi: ")
        ostohinta = float(input("Anna osakkeen ostohinta/kpl: "))
        maara = int(input("Anna ostettujen osakkaiden lukumäärä: "))
        osakkeet.append(Osake(nimi, ostohinta, maara))
        jatka = input("Lisää osakkeita (k/e)? ")
        if jatka == 'e':
            break

    kasvuprosentti = int(input("Anna kasvuprosentti: "))
    vuodet = int(input("Anna vuodet: "))

    for obj in osakkeet:
     print(obj.nimi, obj.ostohinta)
     potti = obj.tulosta_arvo(kasvuprosentti, vuodet)
     kokoPotti += potti
    print(f"Koko potin arvo on {kokoPotti:.2f}")
  
 
    
