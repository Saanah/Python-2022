"""
KT4

Tutustu omatoimisesti Pandas-kirjastoon. Käytä tutustumiseen vaikkapa w3schools-sivustoa. Tee yksi esimerkkiohjelma, jossa käytät ko kirjastoa sekä selitä se python-kommenteissa.  Esimerkkisovellus on vapaavalintainen.


"""
#imports here
import pandas as pd
import numpy as np


if __name__ == '__main__':

    #Arvosanat Series ja niiden keskiarvo + DataFramejen testausta

    filepath = "./tilaukset.json"
    arvosanat = { }
    nimet = ["Elli", "Kalle", "Johannes", "Saana", "Liisa", "Bob", "Ari", "George", "Kati", "Alisa"]
    opiskelijaTiedot = {
        "Nimi" : ["Elli", "Kalle", "Johannes", "Saana"],                                             
        "Arvosana" : [4, 2, 5, 3],
        "Opiskelijanumero" : ["4561", "1441", "6812", "2711"]
    }
  
    koulunHenkilosto = {
            "opettajat": ["Mr. Batman", "Maija Poppanen", "Jukka Kinnunen"],
            "erityisopettajat": ["Pauliina Perhonen", "Veke Vetskari", "Alex Virtanen"],
            "keittäjät" : ["Paavo Pesusieni", "Gordon Ramsay"],
            "Siivoojat" : ["Tupu Ankka", "Lupu Ankka", "Hupu Ankka"]
            }
    

    for i in range(10):
        arvosana = np.random.randint(0,6) #Arvotaan arvosana 1-5 käyttäen Numpy-kirjastoa
        if arvosana == 0:                 #Jos arvosana on 0, asetetaan se NaN, "missing data", -arvoksi
            arvosana = np.nan
        arvosanat.update({nimet[i]: arvosana})
        
    arvosanaData = pd.Series(arvosanat) #Syötetään arvosanat yksiulotteiseen Panda Series ndArrayhin
    keskiarvo = arvosanaData.mean(skipna = True)  #Lasketaan sarjan keskiarvo ja hypätään tyhjien yli
    print(f'Opiskelijoiden arvosanat:\n{arvosanaData}')
    print(f'Arvosanojen keskiarvo on {round(keskiarvo, 2)}\n')
    
    #Moniulotteinen Panda DataFrame

    opiskelijaData = pd.DataFrame(opiskelijaTiedot)
    henkilistoData = pd.DataFrame.from_dict(koulunHenkilosto, orient = 'index') #Jos eripituisia rivejä, laitetaan index sarakkeiden alkuun errorin välttämiseksi
    print(f'Opiskelijatiedot:\n{opiskelijaData}\n')
    print(f'Koulun henkilöstö:\n{henkilistoData}\n')

    #Tiettyjen datasarakkeiden valinta DataFramesta
    opiskelijaNumerot = opiskelijaData["Opiskelijanumero"]
    print(f'Opiskelijanumerot:\n{opiskelijaNumerot}\n')
    print(f'Opiskelijan Saana opiskelijanumero: {opiskelijaNumerot[1]}\n')

    #Indeksin muuttaminen haluttuun muotoon
    tiedotOmallaIndeksillä = pd.DataFrame({"Nimi" : ["Maija", "Roope", "Jeesus", "Maria"],
                              "Ikä" : [15, 32, 2022, 46],
                              "Ammatti" : ["Opiskelija", "Patologi", "Jumalan poika", "Kotiäiti"]
                              },
                              index = ["nainen", "mies", "yhden kromosomin ihme", "nainen"])
    print(f'Dataa satunnaisesta otoksesta:\n{tiedotOmallaIndeksillä}\n')

    #Tietyllä indeksillä haetut tiedot
    indeksinData = tiedotOmallaIndeksillä.loc['nainen', :]
    print(f'Otoksen naiset:\n{indeksinData}\n')

    #Json-tiedoston lukeminen
    tilaukset = pd.read_json(filepath)
    print(f'Json-tiedostosta:\n{tilaukset.to_string()}')