import requests
import xmltodict
import datetime
from tkinter import *
import time

vandaag = datetime.datetime.now()
datum = vandaag.strftime('%a %d %b %Y')
tijd = vandaag.strftime('%H:%M')
lijst = []
list = []

def station_lijst():
    'Dit controleert of de ingevoerde station in Nederland is, en of het wel bestaat.'
    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-stations?_ga=2.144939316.1633515006.1539776820-574820872.1539172714'

    response = requests.get(api_url, auth=auth_details)
    'API oproepen'

    vertrekXML = xmltodict.parse(response.text)

    while True:
        station = a
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
    'Dit controleert of de ingevoerde eindstation wel in Nederland is en of het wel bestaat.'
    veld2 = Entry(root, font=('Frutiger', 50, 'bold'), fg='#ffac00', background='#003373')
    veld2.place(x=550, y=700)
    veld2.focus_set()

    def get_entry():
        b = veld2.get()
        return b

    get_entry()

    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-stations?_ga=2.144939316.1633515006.1539776820-574820872.1539172714'

    response = requests.get(api_url, auth=auth_details)
    'API oproepen'

    vertrekXML = xmltodict.parse(response.text)

    while True:
        station_eind = b
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
    'Dit controleert of de ingevoerde station wel bestaat.'
    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-stations?_ga=2.144939316.1633515006.1539776820-574820872.1539172714'

    response = requests.get(api_url, auth=auth_details)
    'API oproepen'

    vertrekXML = xmltodict.parse(response.text)

    while True:
        station = c
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
    'Dit controleert of de ingevoerde station wel bestaat en zich in het buitenland bevind.'
    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-stations?_ga=2.144939316.1633515006.1539776820-574820872.1539172714'

    response = requests.get(api_url, auth=auth_details)
    'API oproepen'

    vertrekXML = xmltodict.parse(response.text)

    while True:
        station_eind = d
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
    'API oproepen'

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
    'API oproepen'

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
    'Dit is de optie waarvoor wordt gekozen als de gebruiker kiest voor het plannen van zijn/haar route naar het buitenland.'
    stad = station_lijst_buitenland()
    stad_eind = station_lijst_buitenland_eind()

    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(stad)

    response = requests.get(api_url, auth=auth_details)
    'API oproepen'

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

def interface_plannen():
    'Interface voor de optie plannen.'
    root = Tk()
    root.title('NS Ticketmachine')
    root.geometry('1920x1080+0+0')
    root.configure(background='#ffac00')

    heading = Label(root, text='Welcome to NS', background='#ffac00', font=('Frutiger', 110, 'bold'),
                    fg='#003373').pack()

    label1 = Label(root, text='Please insert the following : ', background='#ffac00', font=('Frutiger', 40, 'bold'),
                   fg='#003373').pack()
    label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 20, 'bold'),
                   fg='#003373').place(x=10, y=10)

    veld1 = Entry(root, font=('Frutiger',50, 'bold'), fg='#ffac00', background='#003373')
    veld1.place(x=550, y=400)
    veld1.focus_set()

    veld2 = Entry(root, font=('Frutiger',50, 'bold'), fg='#ffac00', background='#003373')
    veld2.place(x=550, y=700)
    veld2.focus_set()

    def get_entry():
        a = veld1.get()
        b = veld2.get()
        return a, b


    Enter = Button(root, text='Enter', width=15, height=13, bg='#ffac00', command=lambda: [plannen(), get_entry()], font=('Frutiger', 30, 'bold'), fg='#003373').place(x=1400, y=300)

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


def interface_nuweg():
    'Interface voor de optie nu weg.'
    root = Tk()
    root.title('NS Ticketmachine')
    root.geometry('1920x1080+0+0')
    root.configure(background='#ffac00')

    heading = Label(root, text='Welcome to NS', background='#ffac00', font=('Frutiger', 110, 'bold'),
                    fg='#003373').pack()

    label1 = Label(root, text='Please insert the following : ', background='#ffac00', font=('Frutiger', 40, 'bold'),
                   fg='#003373').pack()
    label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 20, 'bold'),
                   fg='#003373').place(x=10, y=10)

    veld2 = Entry(root, font=('Frutiger', 50, 'bold'), fg='#ffac00', background='#003373')
    veld2.place(x=550, y=700)
    veld2.focus_set()

    def get_entry():
        b = veld2.get()
        return b

    Enter = Button(root, text='Enter', width=15, height=13, bg='#ffac00', command=lambda:[get_entry(), nu_weg()], font=('Frutiger', 30, 'bold'), fg='#003373').place(x=1400, y=300)

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


def interface_buitenland():
    'Interface voor de optie buitenland.'
    root = Tk()
    root.title('NS Ticketmachine')
    root.geometry('1920x1080+0+0')
    root.configure(background='#ffac00')

    heading = Label(root, text='Welcome to NS', background='#ffac00', font=('Frutiger', 110, 'bold'),
                    fg='#003373').pack()

    label1 = Label(root, text='Please insert the following : ', background='#ffac00', font=('Frutiger', 40, 'bold'),
                   fg='#003373').pack()
    label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 20, 'bold'),
                   fg='#003373').place(x=10, y=10)

    veld1 = Entry(root, font=('Frutiger',50, 'bold'), fg='#ffac00', background='#003373')
    veld1.place(x=550, y=400)
    veld1.focus_set()

    veld2 = Entry(root, font=('Frutiger',50, 'bold'), fg='#ffac00', background='#003373')
    veld2.place(x=550, y=700)
    veld2.focus_set()

    def get_entry():
        c = veld1.get()
        d = veld2.get()
        return c, d

    Enter = Button(root, text='Enter', width=15, height=13, bg='#ffac00', command=lambda:[buitenland(), get_entry()], font=('Frutiger', 30, 'bold'), fg='#003373').place(x=1400, y=300)

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

root = Tk()
'Beginscherm interface.'

root.title('NS Ticketmachine')
root.geometry('1920x1080+0+0')
root.configure(background='#ffac00')

heading = Label(root, text='Welcome to NS', background='#ffac00',  font=('Frutiger', 110, 'bold'), fg='#003373').pack()

label1 = Label(root, text='Please select your option', background='#ffac00', font=('Frutiger', 40, 'bold'), fg='#003373').pack()
label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 20, 'bold'), fg='#003373').place(x=10, y=10)


#logo = PhotoImage(file='NS1.png')
#label3 = Label(root, image=logo).pack()

'buttons'
knop1 = Button(root, text='Route Planner', width=15, height=6, bg='#ffac00', command=interface_plannen, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=250, y=500)
knop2 = Button(root, text='Leave Now', width=15, height=6, bg='#ffac00', command=interface_nuweg, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=750, y=500)
knop3 = Button(root, text='Travel Abroad', width=15, height=6, bg='#ffac00', command=interface_buitenland, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=1250, y=500)


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


