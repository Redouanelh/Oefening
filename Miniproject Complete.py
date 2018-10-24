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
        station = a.title()
        for x in vertrekXML['stations']['station']:
            name = x['name']
            country = x['country']
            lijst.append(name)
            lijst.append(country)

        if station not in lijst:
            'Laat door middel van een pop-up zien dat het geen geldig station is.'
            root = Tk()
            root.title('NS Ticketmachine')
            root.geometry('800x600+500+250')
            root.configure(background='#003373')
            label = Label(root, text='The station you have entered is not valid.\n\nPlease try again.',
                          font=('Frutiger', 30, 'bold'), bg='#003373', fg='#ffac00').pack()
            ok = Button(root, text='Ok', width=7, height=2, bg='#ffac00', command=root.destroy,
                        font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)
            root.mainloop()
        else:
            index = lijst.index(station)
            land = index + 1
            if lijst[land] != 'NL':
                'Laat door middel van een pop-up zien dat het ingevoerde station niet buitenlands mag zijn.'
                root = Tk()
                root.title('NS Ticketmachine')
                root.geometry('800x600+500+250')
                root.configure(background='#003373')
                label = Label(root, text='The station you have entered is unknown in the Netherlands.\n\nPlease try again.',
                              font=('Frutiger', 30, 'bold'), bg='#003373', fg='#ffac00').pack()
                ok = Button(root, text='Ok', width=7, height=2, bg='#ffac00', command=root.destroy,
                            font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)
                root.mainloop()
            else:
                goed = station
                return goed

def station_lijst_eind():
    'Dit controleert of de ingevoerde eindstation wel in Nederland is en of het wel bestaat.'
    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-stations?_ga=2.144939316.1633515006.1539776820-574820872.1539172714'

    response = requests.get(api_url, auth=auth_details)
    'API oproepen'

    vertrekXML = xmltodict.parse(response.text)

    while True:
        station_eind = b.title()
        for x in vertrekXML['stations']['station']:
            name = x['name']
            country = x['country']
            lijst.append(name)
            lijst.append(country)
        if station_eind not in lijst:
            'Laat door middel van een pop-up zien dat het geen geldig station is.'
            root = Tk()
            root.title('NS Ticketmachine')
            root.geometry('800x600+500+250')
            root.configure(background='#003373')
            label = Label(root, text='The station you have entered is not valid.\n\nPlease try again.',font=('Frutiger', 30, 'bold'), bg='#003373', fg='#ffac00').pack()
            ok = Button(root, text='Ok', width=7, height=2, bg='#ffac00', command=root.destroy, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)
            root.mainloop()

        else:
            index = lijst.index(station_eind)
            land = index + 1
            if lijst[land] != 'NL':
                'Laat door middel van een pop-up zien dat het ingevoerde station niet buitenlands mag zijn.'
                root = Tk()
                root.title('NS Ticketmachine')
                root.geometry('800x600+500+250')
                root.configure(background='#003373')
                label = Label(root,
                              text='The station you have entered\n is unknown in the Netherlands.\n\nPlease try again.',
                              font=('Frutiger', 30, 'bold'), bg='#003373', fg='#ffac00').pack()
                ok = Button(root, text='Ok', width=7, height=2, bg='#ffac00', command=root.destroy,
                            font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)
                root.mainloop()
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
        station = c.title()
        for x in vertrekXML['stations']['station']:
            name = x['name']
            country = x['country']
            lijst.append(name)
            lijst.append(country)

        if station not in lijst:
            'Laat door middel van een pop-up zien dat het geen geldig station is.'
            root = Tk()
            root.title('NS Sprinter Ticketmachine')
            root.geometry('800x600+500+250')
            root.configure(background='#003373')
            label = Label(root, text='The station you have entered is not valid.\n\nPlease try again.',
                          font=('Frutiger', 30, 'bold'), bg='#003373', fg='#ffac00').pack()
            ok = Button(root, text='Ok', width=7, height=2, bg='#ffac00', command=root.destroy,
                        font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)
            root.mainloop()
        else:
            index = lijst.index(station)
            land = index + 1
            if lijst[land] != 'NL':
                'Laat door middel van een pop-up zien dat het ingevoerde station niet buitenlands mag zijn.'
                root = Tk()
                root.title('NS Sprinter Ticketmachine')
                root.geometry('800x600+500+250')
                root.configure(background='#003373')
                label = Label(root,
                              text='The station you have\n entered is unknown in the Netherlands.\n\nPlease try again.',
                              font=('Frutiger', 30, 'bold'), bg='#003373', fg='#ffac00').pack()
                ok = Button(root, text='Ok', width=7, height=2, bg='#ffac00', command=root.destroy,
                            font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)
                root.mainloop()
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
        station_eind = d.title()
        for x in vertrekXML['stations']['station']:
            name = x['name']
            country = x['country']
            lijst.append(name)
            lijst.append(country)
        if station_eind not in lijst:
            'Laat door middel van een pop-up zien dat het geen geldig station is.'
            root = Tk()
            root.title('NS Sprinter Ticketmachine')
            root.geometry('800x600+500+250')
            root.configure(background='#003373')
            label = Label(root, text='The station you have entered is not valid.\n\nPlease try again.',
                          font=('Frutiger', 30, 'bold'), bg='#003373', fg='#ffac00').pack()
            ok = Button(root, text='Ok', width=7, height=2, bg='#ffac00', command=root.destroy,
                        font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)
            root.mainloop()
        else:
            index = lijst.index(station_eind)
            land = index + 1
            if lijst[land] == 'NL':
                'Laat door middel van een pop-up zien dat het ingevoerde station alleen buitenlands mag zijn.'
                root = Tk()
                root.title('NS Sprinter Ticketmachine')
                root.geometry('800x600+500+250')
                root.configure(background='#003373')
                label = Label(root,
                              text='The station you have\n entered is known in the Netherlands.\nOnly foreign stations are allowed.\n\nPlease try again.',
                              font=('Frutiger', 30, 'bold'), bg='#003373', fg='#ffac00').pack()
                ok = Button(root, text='Ok', width=7, height=2, bg='#ffac00', command=root.destroy,
                            font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)
                root.mainloop()
            else:
                goed1 = station_eind
                return goed1


def plannen():
    'Dit is de optie waarvoor wordt gekozen als de gebruiker kiest voor het plannen van zijn/haar route.'
    stad = station_lijst()
    stad_eind = station_lijst_eind()

    global q
    global w
    global interface_output

    interface_output = []

    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(stad)

    response = requests.get(api_url, auth=auth_details)
    'API oproepen'

    vertrekXML = xmltodict.parse(response.text)


    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]  # 18:36

        if stad_eind == eindbestemming:
            q = 'At ' + vertrektijd + ' leaves a train to ' + eindbestemming
            interface_output.append(q)
        elif stad_eind in eindbestemming:
            w = 'At ' + vertrektijd + ' leaves a train to ' + eindbestemming
            interface_output.append(w)
        else:
            pass


def nu_weg():
    'Dit is de optie waarvoor wordt gekozen als de gebruiker kiest voor NU VERTREKKEN.'
    stad_eind = station_lijst_eind()

    global q
    global w
    global interface_output

    interface_output = []


    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'

    response = requests.get(api_url, auth=auth_details)
    'API oproepen'

    vertrekXML = xmltodict.parse(response.text)

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]  # 18:36

        if stad_eind == eindbestemming:
            q = 'At ' + vertrektijd + ' leaves a train to ' + eindbestemming
            interface_output.append(q)
        elif stad_eind in eindbestemming:
            w = 'At ' + vertrektijd + ' leaves a train to ' + eindbestemming
            interface_output.append(w)
        else:
            pass



def buitenland():
    'Dit is de optie waarvoor wordt gekozen als de gebruiker kiest voor het plannen van zijn/haar route naar het buitenland.'
    stad = station_lijst_buitenland()
    stad_eind = station_lijst_buitenland_eind()

    global q
    global w
    global interface_output

    interface_output = []

    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(stad)

    response = requests.get(api_url, auth=auth_details)
    'API oproepen'

    vertrekXML = xmltodict.parse(response.text)


    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]  # 18:36

        if stad_eind == eindbestemming:
            q = 'At ' + vertrektijd + ' leaves a train to ' + eindbestemming
            interface_output.append(q)
        elif stad_eind in eindbestemming:
            w = 'At ' + vertrektijd + ' leaves a train to ' + eindbestemming
            interface_output.append(w)
        else:
            pass

def interface_plannen():
    'Interface voor de optie plannen.'
    root = Tk()
    root.title('NS Sprinter Ticketmachine')
    root.geometry('1920x1080+0+0')
    root.configure(background='#ffac00')

    heading = Label(root, text='Route Planner', background='#ffac00', font=('Frutiger', 110, 'bold'),
                    fg='#003373').pack()

    label1 = Label(root, text='Please insert the following : ', background='#ffac00', font=('Frutiger', 40, 'bold'),
                   fg='#003373').pack()
    label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 30, 'bold'),
                   fg='#003373').place(x=10, y=10)
    label3 = Label(root, text='Sprinter', font=('Futiger', 25, 'bold'), bg='#ffac00', fg='#003373').place(x=90, y=55)
    label4 = Label(root, text='From :', background='#ffac00', font=('Frutiger', 50, 'bold'),
                   fg='#003373').place(x=550, y=300)
    label5 = Label(root, text='To :', background='#ffac00', font=('Frutiger', 50, 'bold'),
                   fg='#003373').place(x=550, y=610)
    return_button = Button(root, text='Return', width=7, height=2, bg='#ffac00', command=root.destroy,
                           font=('Frutiger', 30, 'bold'), fg='#003373').place(x=10, y=875)

    veld1 = Entry(root, font=('Frutiger',50, 'bold'), fg='#ffac00', background='#003373')
    veld1.place(x=550, y=400)
    veld1.focus_set()

    veld2 = Entry(root, font=('Frutiger',50, 'bold'), fg='#ffac00', background='#003373')
    veld2.place(x=550, y=700)
    veld2.focus_set()

    def get_entry():
        'Haalt de ingevoerde woord op uit de Entry balk.'
        global a
        global b
        a = veld1.get()
        b = veld2.get()
        return a, b

    def place_output():
        'Laat door middel van een pop-up de vertrektijden zien.'
        root = Tk()
        root.title('NS Sprinter Ticketmachine')
        root.geometry('800x600+500+250')
        root.configure(background='#003373')
        if len(interface_output) == 0:
            output = Label(root, text='Unfortunately, there are no trains\n heading towards your destination.\n\nPlease try again later.', bg='#003373', fg='#ffac00', font=('Frutiger', 25, 'bold')).pack()
        else:
            output = Label(root, text='\n\n'.join(interface_output), bg='#003373', fg='#ffac00', font=('Frutiger', 25, 'bold')).pack()
        ok = Button(root, text='Finish', width=7, height=2, bg='#ffac00', command=root.destroy, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)

        root.mainloop()


    Enter = Button(root, text='Enter', width=15, height=13, bg='#ffac00', command=lambda: [get_entry(), plannen(), root.destroy(), place_output()], font=('Frutiger', 30, 'bold'), fg='#003373').place(x=1400, y=300)

    def tick(time1=''):
        'Dit is onze digitale klok.'
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
    root.title('NS Sprinter Ticketmachine')
    root.geometry('1920x1080+0+0')
    root.configure(background='#ffac00')

    heading = Label(root, text='Leave Now', background='#ffac00', font=('Frutiger', 110, 'bold'),
                    fg='#003373').pack()

    label1 = Label(root, text='Please insert the following : ', background='#ffac00', font=('Frutiger', 40, 'bold'),
                   fg='#003373').pack()
    label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 30, 'bold'),
                   fg='#003373').place(x=10, y=10)
    label3 = Label(root, text='Sprinter', font=('Futiger', 25, 'bold'), bg='#ffac00', fg='#003373').place(x=90, y=55)
    label4 = Label(root, text='To :', background='#ffac00', font=('Frutiger', 50, 'bold'),
                   fg='#003373').place(x=550, y=610)
    return_button = Button(root, text='Return', width=7, height=2, bg='#ffac00', command=root.destroy, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=10, y=875)

    veld2 = Entry(root, font=('Frutiger', 50, 'bold'), fg='#ffac00', background='#003373')
    veld2.place(x=550, y=700)
    veld2.focus_set()

    def get_entry():
        'Haalt de ingevoerde woord op uit de Entry balk.'
        global b
        b = veld2.get()
        return b

    def place_output():
        'Laat door middel van een pop-up de vertrektijden zien.'
        root = Tk()
        root.title('NS Ticketmachine')
        root.geometry('800x600+500+250')
        root.configure(background='#003373')
        if len(interface_output) == 0:
            output = Label(root, text='Unfortunately, there are no trains\n heading towards your destination.\n\nPlease try again later.', bg='#003373', fg='#ffac00', font=('Frutiger', 25, 'bold')).pack()
        else:
            output = Label(root, text='\n\n'.join(interface_output), bg='#003373', fg='#ffac00', font=('Frutiger', 25, 'bold')).pack()
        ok = Button(root, text='Finish', width=7, height=2, bg='#ffac00', command=root.destroy, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)

        root.mainloop()

    Enter = Button(root, text='Enter', width=15, height=13, bg='#ffac00', command=lambda:[get_entry(), nu_weg(), root.destroy(), place_output()], font=('Frutiger', 30, 'bold'), fg='#003373').place(x=1400, y=300)

    def tick(time1=''):
        'Dit is onze digitale klok.'
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
    root.title('NS Sprinter Ticketmachine')
    root.geometry('1920x1080+0+0')
    root.configure(background='#ffac00')

    heading = Label(root, text='Travel Abroad', background='#ffac00', font=('Frutiger', 110, 'bold'),
                    fg='#003373').pack()

    label1 = Label(root, text='Please insert the following : ', background='#ffac00', font=('Frutiger', 40, 'bold'),
                   fg='#003373').pack()
    label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 30, 'bold'),
                   fg='#003373').place(x=10, y=10)
    label3 = Label(root, text='Sprinter', font=('Futiger', 25, 'bold'), bg='#ffac00', fg='#003373').place(x=90, y=55)
    label4 = Label(root, text='From :', background='#ffac00', font=('Frutiger', 50, 'bold'),
                   fg='#003373').place(x=550, y=300)
    label5 = Label(root, text='To :', background='#ffac00', font=('Frutiger', 50, 'bold'),
                   fg='#003373').place(x=550, y=610)
    return_button = Button(root, text='Return', width=7, height=2, bg='#ffac00', command=root.destroy,
                           font=('Frutiger', 30, 'bold'), fg='#003373').place(x=10, y=875)


    veld1 = Entry(root, font=('Frutiger',50, 'bold'), fg='#ffac00', background='#003373')
    veld1.place(x=550, y=400)
    veld1.focus_set()

    veld2 = Entry(root, font=('Frutiger',50, 'bold'), fg='#ffac00', background='#003373')
    veld2.place(x=550, y=700)
    veld2.focus_set()

    def get_entry():
        'Haalt de ingevoerde woord op uit de Entry balk.'
        global c, d
        c = veld1.get()
        d = veld2.get()
        return c, d

    def place_output():
        'Laat door middel van een pop-up de vertrektijden zien.'
        root = Tk()
        root.title('NS Ticketmachine')
        root.geometry('800x600+500+250')
        root.configure(background='#003373')
        if len(interface_output) == 0:
            output = Label(root, text='Unfortunately, there are no trains\n heading towards your destination.\n\nPlease try again later.', bg='#003373', fg='#ffac00', font=('Frutiger', 25, 'bold')).pack()
        else:
            output = Label(root, text='\n\n'.join(interface_output), bg='#003373', fg='#ffac00', font=('Frutiger', 25, 'bold')).pack()
        ok = Button(root, text='Finish', width=7, height=2, bg='#ffac00', command=root.destroy, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=315, y=450)

        root.mainloop()

    Enter = Button(root, text='Enter', width=15, height=13, bg='#ffac00', command=lambda:[get_entry(), buitenland(), root.destroy(), place_output()], font=('Frutiger', 30, 'bold'), fg='#003373').place(x=1400, y=300)

    def tick(time1=''):
        'Dit is onze digitale klok.'
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

root.title('NS Sprinter Ticketmachine')
root.geometry('1920x1080+0+0')
root.configure(background='#ffac00')

heading = Label(root, text='Welcome to NS', background='#ffac00',  font=('Frutiger', 110, 'bold'), fg='#003373').pack()

label1 = Label(root, text='Please select your option', background='#ffac00', font=('Frutiger', 40, 'bold'), fg='#003373').pack()
label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 30, 'bold'), fg='#003373').place(x=10, y=10)
label3 = Label(root, text='Sprinter', font=('Futiger', 25, 'bold'), bg='#ffac00', fg='#003373').place(x=90, y=55)

#NS logo
canvas = Canvas(width=300, height=200, bg='#ffac00', highlightthickness=0)
canvas.pack(expand=YES, fill=BOTH)
gif1 = PhotoImage(file='ns20.png')
canvas.create_image(700, 0, image=gif1, anchor=NW)

def stationXML():
    'Dit wordt gebruikt om als gebruiker een lijst met namen van de stations te zien die volgens NS mogelijk zijn. Telkens als je op de return knop klikt en opnieuw de stationlijst start, worden er nieuwe stations op het scherm toegevoegd. Het is ons niet gelukt dit te fixen.'
    auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
    api_url = 'http://webservices.ns.nl/ns-api-stations?_ga=2.144939316.1633515006.1539776820-574820872.1539172714'
    final_list = []

    response = requests.get(api_url, auth=auth_details)
    'API oproepen'

    vertrekXML = xmltodict.parse(response.text)

    for x in vertrekXML['stations']['station']:
        name = x['name']
        final_list.append(name)


    root = Tk()
    root.title('NS Sprinter Ticketmachine')
    root.geometry('1920x1080+0+0')
    root.configure(background='#003373')
    labeltje = Label(root, text=', '.join(final_list), wraplength=1920, bg='#003373', fg='#ffac00', font=('Frutiger', 9, 'bold')).pack()
    return1 = Button(root, text='Return', width=15, height=2, bg='#ffac00', command=root.destroy, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=10, y=875)


#Buttons
knop1 = Button(root, text='Route Planner', width=15, height=6, bg='#ffac00', command=interface_plannen, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=250, y=500)
knop2 = Button(root, text='Leave Now', width=15, height=6, bg='#ffac00', command=interface_nuweg, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=750, y=500)
knop3 = Button(root, text='Travel Abroad', width=15, height=6, bg='#ffac00', command=interface_buitenland, font=('Frutiger', 30, 'bold'), fg='#003373').place(x=1250, y=500)
knop4 = Button(root, text='Available Stations', width=15, height=2, bg='#ffac00', command=stationXML,font=('Frutiger', 30, 'bold'), fg='#003373').place(x=10, y=875)


def tick(time1=''):
    'Dit is de digitale klok'
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock_frame.config(text=time2)
    clock_frame.after(200, tick)

clock_frame = Label(root, font=('Futiger', 25, 'bold'), bg='#ffac00', fg='#003373')
clock_frame.place(x=1750, y=10)
tick()

root.mainloop()
