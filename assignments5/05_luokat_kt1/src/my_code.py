"""
KT1

Luontojärjestö KuopionBongarit tarvitsee uuden rekisterin, johon kaikki lintuhavainnot rekisteröidään.

Tee julkinen luokka Havainto, jolla on ominaisuudet:
- lintulaji, teksti
- maara, kokonaisluku, jos <0 muutetaan nollaksi
- tyyppi, teksti (Eli oliko lintu esim paikallinen vai muuttava)
- havaintopvm, datetime, ei voi olla tulevaisuuteen
- paikka, teksti
- kuvaus, teksti
 
Tee luokalle muodostin, jossa annetaan arvot kaikille luokan attribuuteille yllä olevassa järjestyksessä.
Tee kaikille jäsenmuuttujille getterit ja setterit Python-tekniikalla,  jotta tietoja pääsee muokkaamaan ja lukemaan. Tulosta getterissä viesti "getter" ja vastaavasti setterissä viesti "setter".
Tee myös __str__-metodi.  
Testaa pääohjelmassa. Mitään sen kummempaa käyttöliittymää ei tarvitse tehdä. Riittää, että luot yhden Havainto olion ja tulostat sen tiedot hyödyntäen __str__ metodia.

"""
#Write class and imports here!
from datetime import datetime


class Havainto:
    _lintulaji = ""
    _maara = 0
    _tyyppi = ""
    _havaintopvm = datetime(1,1,1)
    _paikka = ""
    _kuvaus = ""
    
    def __init__(self, lintulaji, maara, tyyppi, havaintopvm, paikka, kuvaus):
        self.lintulaji = lintulaji
        if maara < 0:
            maara = 0
        self.maara = maara
        self.tyyppi = tyyppi
        if datetime.now() > havaintopvm:
            self.havaintopvm = havaintopvm
        self.paikka = paikka
        self.kuvaus = kuvaus
    
    def __str__(self):
        
        return 'Lintulaji = ' + self.lintulaji + ' , Maara = ' + str(self.maara) + ', Tyyppi = ' + self.tyyppi + ', Havaintopvm = ' + str(self.havaintopvm) + ', Paikka = ' + self.paikka + ', Kuvaus = ' + self.kuvaus



    @property
    def lintulaji(self):
        print("getter")
        return self._lintulaji
    
    @lintulaji.setter
    def lintulaji(self, lintulaji):
        print("setter")
        self._lintulaji = lintulaji

    @property
    def maara(self):
        print("getter")
        return self._maara

    @maara.setter
    def maara(self, maara):
        print("setter")
        if maara < 0:
            maara = 0
        self._maara = maara

    @property
    def tyyppi(self):
        print("getter")
        return self._tyyppi


    @tyyppi.setter
    def tyyppi(self, tyyppi):
        print("setter")
        self._tyyppi = tyyppi

    @property
    def havaintopvm(self):
        print("getter")
        return self._havaintopvm

    @havaintopvm.setter
    def havaintopvm(self, havaintopvm):
        print("setter")
        if datetime.now() > havaintopvm:
            self._havaintopvm = havaintopvm

    @property
    def paikka(self):
        print("getter")
        return self._paikka

    @paikka.setter
    def paikka(self, paikka):
        print("setter")
        self._paikka = paikka
    
    @property
    def kuvaus(self):
        print("getter")
        return self._kuvaus

    @kuvaus.setter
    def kuvaus(self, kuvaus):
        print("setter")
        self._kuvaus = kuvaus

if __name__ == "__main__":
    #Write main program below this line
    myObject = Havainto("Urpiainen", -2, "Paikallinen", datetime(2022,2,12), "Tervola", "Havaittu takapihalla")
    print(myObject.__str__())