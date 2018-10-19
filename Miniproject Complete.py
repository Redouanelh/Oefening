import requests
import xmltodict
import datetime
from tkinter import *
import time

vandaag = datetime.datetime.now()
datum = vandaag.strftime('%a %d %b %Y')
tijd = vandaag.strftime('%H:%M')
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
                print('Reizen naar het buitenland is hier niet van toepassing.')
            else:
                goed = station
                return goed

def station_lijst_eind():
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
            if lijst[land] != 'NL':
                print('Reizen naar het buitenland is hier niet van toepassing.')
            else:
                goed1 = station_eind
                return goed1

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


def plannen():
    'Dit is de optie waarvoor wordt gekozen als de gebruiker kiest voor het plannen van zijn/haar route.'
    stad = station_lijst()
    stad_eind = station_lijst_eind()

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


def nu_weg():
    'Dit is de optie waarvoor wordt gekozen als de gebruiker kiest voor NU VERTREKKEN.'
    stad_eind = station_lijst_eind()

    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'

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

root = Tk()
'Dit is de interface'

root.title('NS Ticketmachine')
root.geometry('1920x1080+0+0')
root.configure(background='#ffac00')

heading = Label(root, text='Welcome to NS', background='#ffac00',  font=('Frutiger', 110, 'bold'), fg='#003373').pack()

label1 = Label(root, text='Please select your option', background='#ffac00', font=('Frutiger', 40, 'bold'), fg='#003373').pack()
label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 20, 'bold'), fg='#003373').place(x=10, y=10)


#logo = PhotoImage(file='NS1.png')
#label3 = Label(root, image=logo).pack()

knop1 = Button(root, text='Route Planner', width=15, height=6, bg='#ffac00', command=print('open scherm'), font=('Frutiger', 30, 'bold'), fg='#003373').place(x=250, y=500)
knop2 = Button(root, text='Leave Now', width=15, height=6, bg='#ffac00', command=print('open scherm'), font=('Frutiger', 30, 'bold'), fg='#003373').place(x=750, y=500)
knop3 = Button(root, text='Travel Abroad', width=15, height=6, bg='#ffac00', command=print('open scherm'), font=('Frutiger', 30, 'bold'), fg='#003373').place(x=1250, y=500)


def tick(time1=''):
    'Dit is onze klok.'
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock_frame.config(text=time2)
    clock_frame.after(200, tick)

clock_frame = Label(root, font=('Futiger', 25, 'bold'), bg='#ffac00', fg='#003373')
clock_frame.place(x=1750, y=10)
tick()
root.mainloop()

