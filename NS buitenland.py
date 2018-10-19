import requests
import xmltodict
import datetime

lijst = []

def station_lijst_buitenland():
    'Dit controleert of de ingevoerde station mogelijk is.'
    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-stations?_ga=2.144939316.1633515006.1539776820-574820872.1539172714'

    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)

    while True:
        station = input('Voer uw station in: ').title()
        for x in vertrekXML['stations']['station']:
            name = x['name']
            country = x['country']
            lijst.append(name)
            lijst.append(country)

        if station not in lijst:
            print('Voer een geldig station in.')
        else:
            index = lijst.index(station)
            land = index + 1
            if lijst[land] != 'NL':
                print('Alleen reizen plannen van Nederland naar het buitenland is van toepassing.')
            else:
                goed = station
                return goed

def station_lijst_buitenland_eind():
    'Dit controleert of de ingevoerde station mogelijk is.'
    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-stations?_ga=2.144939316.1633515006.1539776820-574820872.1539172714'

    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)

    while True:
        station_eind = input('Voer uw eindstation in: ').title()
        for x in vertrekXML['stations']['station']:
            name = x['name']
            country = x['country']
            lijst.append(name)
            lijst.append(country)
        if station_eind not in lijst:
            print('Voer een geldig eind station in.')
        else:
            index = lijst.index(station_eind)
            land = index + 1
            if lijst[land] == 'NL':
                print('Alleen reizen naar het buitenland is hier van toepassing.')
            else:
                goed1 = station_eind
                return goed1


def buitenland():
    'Dit is de optie waarvoor wordt gekozen als de gebruiker kiest voor het plannen van zijn/haar route.'
    stad = station_lijst_buitenland()
    stad_eind = station_lijst_buitenland_eind()

    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(stad)

    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)

    print('Dit zijn de vertrekkende treinen: ')

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]  # 18:36

        if stad_eind == eindbestemming:
            print('Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming)
        elif stad_eind in eindbestemming:
            print('Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming)
        else:
            pass

