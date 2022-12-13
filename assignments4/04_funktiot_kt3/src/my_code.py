"""
KT3
Tee ohjelma, joka laskee mäkihyppääjän yhden kierroksen suorituspisteet. Ensin ohjelma kysyy hypyn pituuden (liukuluku 0.5 metrin välein) jonka jälkeen se kysyy viiden arvostelutuomarin tyylipisteet (0-20 välillä 0.5 välein eli esim. 16.5 tai 17.0 tai 18.5). Hyppääjän pisteet muodostuvat kaavasta.

pisteet = (hypyn pituus - kriittinen piste) * 1.8 + kolmen keskimmäisen tuomarin tyylipisteet + 60. 

Tyylipisteissä siis parhain ja huonoin pistemäärä tipahtaa pois.

Ohjelman hyppyrimäen kriittinen piste on 90 metrin kohdalla. Laita kriittinen piste globaaliin vakioon KR_PISTE. Tulosta lopuksi hypyn pituus ja hypyn pisteet. Käytä ohjelmassa funktioita:


KysyHypynPituus - Kysyy hypyn pituuden ja palauttaa sen reaalilukuna
KysyTuomareidenPisteet - Kysyy tuomareiden pisteet yksi kerrallaan. Palauttaa listan jossa on kunkin tuomarin antamat pisteet reaalilukuina. 
LaskeHypynPisteet - Saa ensimmäisenä parametrina hypyn pituuden sekä toisena parametrina listan joka sisältää kaikkien tuomareiden antamat tyylipisteet. Palauttaa hypyn pisteet lukuna.

 
"""
#Write functions and define global variables here!

KR_PISTE = 90

def KysyHypynPituus():

    pituus = float(input("Anna hypyn pituus: "))
    return round(pituus*2)/2
5
def KysyTuomareidenPisteet():

    tuomariPisteet = []

    for n in range(5):
        while True:
            piste = float(input("Anna pisteet väliltä 0-20: "))
            if (piste <= 20 and piste >= 0):
                tuomariPisteet.append(round(piste*2)/2)
                break
            else:
                print("Luku on virheellinen")
   
    return tuomariPisteet

def LaskeHypynPisteet(pituus, tuomariPisteet):

    lasketutPisteet = 0.0
    minimi = min(tuomariPisteet)
    maksimi = max(tuomariPisteet)
    tuomariPisteet.remove(minimi)
    tuomariPisteet.remove(maksimi)
    lasketutPisteet = ((pituus-KR_PISTE) * 1.8 + sum(tuomariPisteet) + 60)

    return lasketutPisteet

if __name__ == "__main__":
    #Write main program below this line
    pituus = KysyHypynPituus()
    tuomariPisteet = KysyTuomareidenPisteet()
    lasketutPisteet = LaskeHypynPisteet(pituus, tuomariPisteet)
    print(f'Hypyn pituus: {pituus} ja lasketut pisteet: {lasketutPisteet:.2f}')

