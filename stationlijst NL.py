import xmltodict
import requests
lijst = []


def station_lijst():
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
                print('Reizen naar het buitenland is momenteel niet mogelijk.')
            else:
                break

station_lijst()




