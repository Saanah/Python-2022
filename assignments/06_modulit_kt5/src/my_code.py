"""
KT5

Korjaa alla oleva funktio siten, että se palauttaa 'Olen antanut palautteen'

"""
#imports here
import re

def palautteen_tila():

    palaute= 'En ole antanut palautetta'
    for r in ( ("ole", ""), ("En", "Olen"),("palautetta", "palautteen")):
        palaute = palaute.replace(*r)                                       #Korvataan tietyt sanat
   
    palaute = re.sub(' +', ' ', palaute) #Regex sub, korvataan tupla spacet
    print(palaute)

    return palaute
