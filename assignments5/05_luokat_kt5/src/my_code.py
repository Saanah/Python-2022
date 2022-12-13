"""

KT5

MyCarStorage on Python- sovellus, joka ylläpitää tietoja omasta vintage-autojen kokoelmasta
sieltä luonnollisesti voidaan poistaa ja sinne  lisätä niitä)

Luokassa CarStorage määritetty koko uniikin autokokoelmani tiedot.

Luokassa Car on yhden hankitun auton tiedot (nimi (siis hellittelynimi rakkaalle autolle),
automalli, hankintapvm, huollot, hankintahinta ja hankintapaikka).

Luokassa CarModel auton  malli ja merkkitieto (merkki ja malli).

Luokassa Service autolle tehty huoltotieto (huoltopvm, toimenpide, hinta).

Yllä ei ole kerrottu millaisia tarkistuksia jäsenmuuttujien tiedoille pitää
settereissä tehdä ja mitä ovat niiden oletusarvoja.
Ne voit miettiä itse, Setterit ja getteri tulee luonnollisesti koodata

Pääohjelma on valmiiksi kirjoitettu, älä muokkaa sitä.

Alle esimerkkitulostus:

The list of my sweet cars:

Name:  Kauppakassi
Brand: Volvo Model: V70 Bought: 01.01.2020
Service history:
	Date: 11.01.2021 Operation: Renkaat vaihdettu Price: 300
	Date: 04.03.2019 Operation: Oljynvaihto Price: 234
Bought place:  Kuopion tori

Name:  Polle
Brand: Porsche Model: Cayanne Bought: 13.01.2021
Service history:
	Date: 11.03.2021 Operation: Renkaat vaihdettu Price: 1300
	Date: 04.12.2019 Operation: Jakopaan hihna vaihdettu Price: 2324
Bought place:  Ita-Auto, Helsinki

Name:  Amppeeri
Brand: Datsun Model: 100A Bought: 13.11.1991
Service history:
	Date: 11.03.1992 Operation: Renkaat vaihdettu Price: 400
	Date: 02.05.1995 Operation: Renkaat vaihdettu Price: 440
	Date: 04.12.2001 Operation: Jakopaan hihna vaihdettu Price: 500
	Date: 04.12.2019 Operation: Pakoputki vaihdettu Price: 324
Bought place:  Auli Autoilija, Pori
"""

import datetime

#Insert your classes here

class CarStorage:
    
    carList = []

    def addCar(self, car):
        self.carList.append(car)

    def deleteCar(self, car):
        self.carList.remove(car)

    def print(self):

        for car in self.carList:
            print(f"Name: {car.nimi}")
            formattedBoughtDate = car.hankintapvm.strftime("%d.%m.%Y")
            print(f"Brand: {car.automalli.merkki} Model: {car.automalli.malli} Bought: {formattedBoughtDate}")
            print(f"Service history: ")
            for service in car.serviceHistory:
                formattedOperationDate = service.huoltopvm.strftime("%d.%m.%Y")
                print(f"\t Date: {formattedOperationDate} Operation: {service.toimenpide} Price: {service.hinta}")
            print(F"Bought place: {car.hankintapaikka}")
            print("")

#CAR

class Car:

    serviceHistory = []

    def __init__(self, name, model, bought, price, boughtplace):
        self.nimi = name
        self.automalli = model
        if bought <= datetime.datetime.now():
            self.hankintapvm = bought
        if price >= 0:
            self.hankintahinta = price
        self.hankintapaikka = boughtplace

    def addService(self, service):
        self.serviceHistory.append(service)
    
    @property
    def name(self):
         return self._nimi
       
    @name.setter
    def name(self, name):
         self._nimi = name
       
    @property
    def model(self):
        return self._automalli
       
    @model.setter
    def model(self, model):
        self._automalli = model
        
    @property
    def bought(self):
         return self._hankintapvm 
       
    @bought.setter
    def name(self, bought):
        if bought <= datetime.datetime.now():
            self.hankintapvm = bought

    @property
    def price(self):
         return self._hankintahinta
       
    @price.setter
    def price(self, price):
          if price >= 0:
            self.hankintahinta = price
    
    @property
    def boughtplace(self):
         return self._hankintapaikka
       
    @boughtplace.setter
    def boughtplace(self, boughtplace):
         self._hankintapaikka = boughtplace
    
#CAR MODEL

class CarModel:
    def __init__(self, merkki, malli):
        self.merkki = merkki
        self.malli = malli

    @property
    def merkki(self):
        return self._merkki
       
    @merkki.setter
    def merkki(self, merkki):
         self._merkki = merkki

    @property
    def malli(self):
        return self._malli
       
    @malli.setter
    def malli(self, malli):
         self._malli = malli

#SERVICE

class Service:

    def __init__(self, date, operation, price):
        self.huoltopvm = date
        self.toimenpide = operation
        self.hinta = price
    
    @property
    def date(self):
        return self._huoltopvm
       
    @date.setter
    def date(self, date):
         self._huoltopvm = date
    
    @property
    def operation(self):
        return self._toimenpide
       
    @operation.setter
    def operation(self, operation):
         self._toimenpide = operation
    
    @property
    def price(self):
        return self._hinta
       
    @price.setter
    def price(self, price):
         self._hinta = price

if __name__ == '__main__':
    myCarStorage = CarStorage()

    volvo_v70 = CarModel("Volvo", "V70")
    porsche_cyaenne = CarModel("Porsche", "Cayanne")
    datsun_100a = CarModel("Datsun", "100A")

    car1 = Car(name="Kauppakassi",model=volvo_v70,
               bought=datetime.datetime(2020, 1,1),price= 1200, boughtplace="Kuopion tori")
    service1 = Service(date = datetime.datetime(2021,1,11),operation="Renkaat vaihdettu", price= 300 )
    service2 = Service(date = datetime.datetime(2019, 3,4),operation="Oljynvaihto", price = 234 )
    car1.addService(service1)
    car1.addService(service2)
    myCarStorage.addCar(car1)

    car2 = Car(name="Polle",model=porsche_cyaenne,
               bought=datetime.datetime(2021, 1,13),price= 11200, boughtplace="Ita-Auto, Helsinki")
    service1 = Service(date = datetime.datetime(2021,3,11),operation="Renkaat vaihdettu", price= 1300 )
    service2 = Service(date = datetime.datetime(2019, 12,4),operation="Jakopaan hihna vaihdettu", price = 2324 )
    car2.addService(service1)
    car2.addService(service2)
    myCarStorage.addCar(car2)

    car3 = Car(name="Amppeeri",model=datsun_100a,
               bought=datetime.datetime(1991, 11,13),price= 200, boughtplace="Auli Autoilija, Pori")
    service1 = Service(date = datetime.datetime(1992,3,11),operation="Renkaat vaihdettu", price= 400 )
    service2 = Service(date = datetime.datetime(1995,5,2),operation="Renkaat vaihdettu", price= 440 )
    service3 = Service(date = datetime.datetime(2001, 12,4),operation="Jakopaan hihna vaihdettu", price = 500 )
    service4 = Service(date = datetime.datetime(2019, 12,4),operation="Pakoputki vaihdettu", price = 324 )
    car3.addService(service1)
    car3.addService(service2)
    car3.addService(service3)
    car3.addService(service4)
    myCarStorage.addCar(car3)
    
    myCarStorage.print()
