import datetime
import csv


bestand = 'testt.csv'

vandaag = datetime.datetime.now()
datum = vandaag.strftime('%a %d %b %Y')
tijd = vandaag.strftime('%H:%M')

list = []

with open('testt.csv', 'a', newline='') as csvv:
    writer = csv.writer(csvv, delimiter=';')


    while True:
        naam = input("Wat is je achternaam? ")
        if naam == 'einde':
            break
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        datum_actueel = [datum,' ', 'at',' ', tijd]
        a = ''.join(datum_actueel)

        list.extend([a, voorl, naam, gbdatum, email])

        writer.writerow(list)
        break


