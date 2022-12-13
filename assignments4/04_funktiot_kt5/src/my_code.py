"""
KT5

Dictionarya käytetään autojen rekisteröintietietojen tallentamiseen. Kirjoita seuraavat funktiot:

LueAutot - Lukee näppäimistöltä ensin auton rekisterinumeron ja sitten rekisteröintipäivämäärän ja tallentaa tiedot dictionaryyn. Tätä toistetaan niin kauan kunnes rekisterinumeroksi syötetään LOPPU. Päivämäärät tallennetaan datetime-tyyppisinä. Funktio palauttaa täytetyn dictionaryn. datetime-tyypin käyttö on opiskeltava omatoimisesti. Päivämäärä syötetään muodossa dd.mm.yyyy, siis esimerkiksi 14.1.2022. Rekisteröintipäivämäärä pyydetään syöttämään uudestaan mikäli päivämäärä on väärässä muodossa.

TalletaTiedostoon - Saa parametrina edellisen dictionaryn ja tallenta sen sisällön tekstitiedostoon autot.txt. Tiedostossa päivämäärät eivät sisällä kellonaikaa. Tiedoston kukin rivi sisältää auton rekisterinumeron ja rekisteröintipäivämäärän '\t'-merkillä erotettuna

LueTiedostosta - Lukee autot.txt:n dictionaryyn ja palauttaa sen.

TulostaTiedot - Saa parametrinaan dictionaryn joka sisältää rekisteröintitiedot. Funktio tulostaa autojen rekisterinumerot ja rekisteröintipäivämäärät.

Kirjoita tarvittaessa testiohjelma funktioiden testaamiseksi.

VINKKI: Jos luet tiedostoa f rakenteella

for line in f:
   ...

niin muuttuja line sisältää myös rivinvaihdon. Sen voit poistaa str.strip()-metodilla.

"""
#Write functions, define global variables, and import modules here!
import datetime


def LueAutot():
   autoTiedot = {}
   rekisteriNum = ""
   key = ""
   i = 1

   while True:
      rekisteriNum = input("Anna rekisterinumero: ")
      if rekisteriNum == "LOPPU":
         break
      key = "rekisterinumero" + str(i)
      autoTiedot[key] = rekisteriNum
      while True:
         rekisteriPaiva = input("Anna rekisteröintipäivämäärä muodossa dd.mm.yyyy: ")
         paiva, kuukausi, vuosi = rekisteriPaiva.split('.')
         try:
            """rekisteriPvm = datetime.datetime.strptime(rekisteriPaiva, "%d.%m.%Y")"""
            rekisteriPvm = datetime.datetime(int(vuosi),int(kuukausi),int(paiva))
            key = "rekisteripvm" + str(i)
            autoTiedot[key] = rekisteriPvm
            i += 1
            break
         except:
            print("Väärä päivämäärä")
   return autoTiedot
   
def TalletaTiedostoon(autoTiedot):

   "Rukoilen Jumalaa ettei kukaa kato tän tiedoston sisään, mun ratkaisut on top notch unnecessarily complicated"

   counter = 1

   tiedosto = open('autot.txt', 'w')
   for key, value in autoTiedot.items():
      if counter % 2 == 0:
         suomiPvm = value.strftime("%d.%m.%Y")
         value = suomiPvm
      tiedosto.write('%s\t' % value)
      if counter % 2 == 0:
          tiedosto.write('\n')
      counter += 1
   tiedosto.close()


def LueTiedostosta():
   luetutAutoTiedot = {}
   i = 1
   tiedosto = open('autot.txt', 'r')
   for line in tiedosto:
      key = str(i)
      line_strip = line.strip().replace("\t", " ")
      luetutAutoTiedot[key] = line_strip
      i += 1
   tiedosto.close()
   return luetutAutoTiedot
      
def TulostaTiedot(luetutAutoTiedot):
   for key, value in luetutAutoTiedot.items():
      print(value)

if __name__ == "__main__":
    #Write main program below this line
   autoTiedot = LueAutot()
   TalletaTiedostoon(autoTiedot)
   luetutAutoTiedot = LueTiedostosta()
   TulostaTiedot(luetutAutoTiedot)
   
    


