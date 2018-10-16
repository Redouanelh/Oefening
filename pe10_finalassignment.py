stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):
    while True:
        begin = input('Voer uw beginstation in: ').title()
        if begin not in stations:
            print('Voer een correcte stationsnaam in.')
        else:
            break
    return begin

def inlezen_eindstation(stations, begin):
    while True:
        eind = input('Voer uw eindstation in: ').title()
        if eind not in stations or stations.index(eind) < stations.index(begin):
            print('Voer een geldige stationsnaam in met een correct volgorde.')
        else:
            break
    return eind

def omroepen_reis(stations, beginstation, eindstation):
    shit = stations.index(beginstation) + 1
    print('Het beginstation', beginstation, 'is het', stations.index(beginstation), 'e station in het traject.')
    print('Het eindstation', eindstation, 'is het', stations.index(eindstation), 'e station in het traject.')
    print('De afstand bedraagt', stations.index(eindstation) - stations.index(beginstation), 'station(s).')
    print('De prijs van het kaartje is', 5 * (stations.index(eindstation) - stations.index(beginstation)), 'euro.')
    print(' ')
    print('Jij stapt in de trein in: ', beginstation, '-', stations[shit])
    print(' ')
    print('Jij stapt uit in: ', eindstation)

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
