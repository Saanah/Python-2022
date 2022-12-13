"""
KT4

Kirjoita funktio Tsekkaus, joka tulostaa ensin tiedon siitä, kuinka monta parametria funktioon tuli. Eli parametrien määrää ei ole rajattu. Jos ensimmäisen parametri oli "opettaja" niin funktio tulosta seuraavalle riville "Koita saada oppilaat oppimaan", jos se taas oli "opiskelija", niin funktio tulostaa "Koita opiskella ahkerasti". Jos parametri oli jotain muuta, niin funktio tulostaa "En ymmarra". Jos parametreja ei ole yhtään, niin funktio tulostaa "Virhe".

"""
#Write functions and define global variables here!

def Tsekkaus(*parametrit):
    
    maara = 0
    for parametri in parametrit:
        maara += 1
    print(maara)
    
    if(maara != 0):
        if(parametrit[0] == "opettaja"):
            print("Koita saada oppilaat oppimaan")
        elif(parametrit[0] == "opiskelija"):
            print("Koita opiskella ahkerasti")
        else:
         print("En ymmarra")
    else:
        print("Virhe")


if __name__ == "__main__":
    #Write main program below this line
    Tsekkaus("opettaja", "oppilas", "koditon")
