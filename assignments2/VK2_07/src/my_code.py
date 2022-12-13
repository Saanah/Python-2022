# -*- coding: utf-8 -*-

"""
KT7

Toimeentulotukea maksetaan turvaamaan perustuslaissa tarkoitettu välttämätön toimeentuloa.
Tee ohjelma, joka laskee yksinäisen henkilön tai perheen saaman toimeentulotuen.
Ohjelma laskee tuen määrän käyttäjän syöttämälle määrälle päiviä ja tulostaa toimeentulotuen kokonaismäärän kahdella desimaalilla.
Ohjelma kysyy tuen laskemisessa tarvittavat tiedot yhdessä asumisesta ja lapsista.
Toimeentulotuen määrä lasketaan alla olevan taulukon mukaisesti kahden desimaalin tarkkuudella.
Toimeentulotuen laskemista voidaan toistaa niin monta kertaa kuin ohjelman käyttäjä haluaa. Alla on suuntaa antava esimerkki ohjelman toiminnasta.

Tuki lasketaan siis yhdelle henkilölle, ei esim avioparille


Tuen saaja

Euroa / päivä

Yksin asuva

16,18

Yksinhuoltaja

17,80

Avio- ja avopuolisot kumpikin

13,76

Jokainen 10-17-vuotias lapsi

11,33

Jokainen alle 10-vuotias lapsi

10,20



Tämä ohjelma laskee toimeentulotuen määrän. Alla esimerkkiajo ohjelmasta.

Koodin rakenteelle ei aseteta vaatimuksia muuten kuin, että syötteet annetaan esimerkin mukaisessa järjestyksessä ja ohjelma laskee (tulostaa) tuen määrän oikein. Esimerkkiajosta käy ilmi. että kysymyksiä luupataan eli ohjelma päättyy vasta kun  käyttäjä ei halua enää laskea toimeentulotukea uusilla tiedoilla.



Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): k

Asutko yksin (1) vai puolison kanssa (2) : 1

Onko sinulla/teillä alaikäisiä lapsia (k/e) : k

Kuinka monta alle 10-vuotiasta lasta : 1

Kuinka monta 10-17-vuotiasta lasta : 2

Kuinka monelle päivälle tuki lasketaan : 10



Saat toimeentulotukea 506.60 euroa

Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): e

"""
jatka = 'k'
valinta = ''
tuki = 0
paiva = 0
henkilo = '0'

tukiMaara = {'1': 16.18, '2' : 13.76, '3' : 10.20, '4' : 11.33, '5' : 17.80}

jatka = input("Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): ")

while jatka != 'e':

    henkilo = input("Asutko yksin (1) vai puolison kanssa (2) : ")
    
    if(henkilo == '1'):
        
        tuki += tukiMaara.get(henkilo)
    
    elif(henkilo == '2'):
        
         tuki += tukiMaara.get(henkilo)

    valinta = input("Onko sinulla/teillä alaikäisiä lapsia (k/e): ")
    
    if(valinta == 'k'):

        if(henkilo == '1'):
            tuki -= tukiMaara.get('1')
        
        valinta = int(input('Kuinka monta alle 10-vuotiasta lasta : '))
        tuki += valinta * tukiMaara.get('3')
        
        valinta = int(input('Kuinka monta 10-17-vuotiasta lasta : '))
        tuki += valinta * tukiMaara.get('4')

        if(henkilo == '1'):
    
            tuki += tukiMaara.get('5')
        
    
    elif(valinta == 'e'):
        
        print("")

    valinta = int(input('Kuinka monelle päivälle tuki lasketaan : '))
    tuki = valinta * tuki
    print(f'Saat toimeentulotukea {tuki:.2f} euroa')
    tuki = 0

    jatka = input("Haluatko laskea toimeentulotuen uusilla tiedoilla (k/e): ")