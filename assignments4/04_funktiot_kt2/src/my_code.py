"""
KT2
Luo dictionary, jossa sinulla henkilöiden arvosanoja (0-5). Jos arvosana < 0, niin laitetaan nollaksi ja jos > 5, niin laitetaan viitoseksi. Henkilön nimi on avain ja arvosana arvo. Dictionaryyn ei luonnollisestikaan saa lisätä samannimistä henkilöä uudelleen. Nimiä/arvosanoja kysytään, kunnes nimeksi annetaan LOPPU. 

Jos hylättyjä ei ole, niin tulosta kaikkien arvosanojen tiedot (nimi + arvosana). Jos hylättyjä on, niin tulosta hylättyjen määrä näytölle ja sen lisäksi tulosta hylätyn saaneiden henkilöiden nimet.

Toteuta seuraavat funktiot:
LuoNimetJaArvosanat - Kysyy nimet ja arvosanat käyttäjältä ja palauttaa dictionaryn 
TulostaHylatyt - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden nimet
PalautaHylattyjenMaara - Saa parametrina dictionaryn ja tulostaa siitä nollan saaneiden henkilöiden lukumäärän
TulostaKaikki - Saa parametrina dictionaryn ja tulostaa siitä kaikkien henkilöiden nimet ja arvosanat

Huolehdi, että ohjelma ei kaadu, jos arvosanaksi annetaan muuta kuin numeroita 

"""

#Write functions here!

def LuoNimetJaArvosanat():

    arvosanat = { }
    nimi = ""
    arvosana = 0
    
    while True:

        nimi = input("Anna nimi: ")

        if(nimi == "LOPPU"):
            break

        while True:
            
            try:
                arvosana = int(input("Anna arvosana: "))
                break

            except:
                print("Virhe, syötä kokonaisluku")
        
        if(arvosana < 0):
            arvosana = 0
    
        if(arvosana > 5):
            arvosana = 5
    
        arvosanat[nimi] = arvosana
    return arvosanat

def TulostaHylatyt(kaikkiArvosanat):
    
    for key in kaikkiArvosanat:
        if (kaikkiArvosanat[key] == 0):
            print(key)
    

def PalautaHylattyjenMaara(kaikkiArvosanat):

    hylattyjenMaara = 0

    for key in kaikkiArvosanat:
        if (kaikkiArvosanat[key] == 0):
            hylattyjenMaara += 1
    print(hylattyjenMaara)

def TulostaKaikki(kaikkiArvosanat):

    for key in kaikkiArvosanat:
        print(key, kaikkiArvosanat[key])


if __name__ == "__main__":
    #Write main program below this line

    kaikkiArvosanat = LuoNimetJaArvosanat()
    TulostaHylatyt(kaikkiArvosanat)
    PalautaHylattyjenMaara(kaikkiArvosanat)
    TulostaKaikki(kaikkiArvosanat)

