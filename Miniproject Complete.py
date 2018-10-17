import requests
import xmltodict
import datetime
from tkinter import *
import time

vandaag = datetime.datetime.now()
datum = vandaag.strftime('%a %d %b %Y')
tijd = vandaag.strftime('%H:%M')
lijst = []


def plannen():
    'Dit is de optie waarvoor wordt gekozen als de gebruiker kiest voor het plannen van zijn/haar route.'
    stad = input('Voer uw vertreklocatie in: ').title()
    stad_eind = input('Voer uw eindbestemming in: ').title()

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
    stad_eind = input('Voer uw eindbestemming in: ').title()

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





#DIT IS DE INTERFACE.
root = Tk()

root.title('NS Ticketmachine')
root.geometry('1920x1080+0+0')
root.configure(background='#ffac00')

heading = Label(root, text='Welcome to NS', background='#ffac00',  font=('Frutiger', 110, 'bold'), fg='#003373').pack()

label1 = Label(root, text='Please choose your option', background='#ffac00', font=('Frutiger', 40, 'bold'), fg='#003373').pack()
label2 = Label(root, text='Utrecht Centraal', background='#ffac00', font=('Frutiger', 20, 'bold'), fg='#003373').place(x=10, y=10)

root.title("Transparency")

frame = Frame(root)
frame.pack()

canvas = Canvas(frame, bg="black", width=500, height=500)
canvas.pack()

photoimage = ImageTk.PhotoImage(file="NS1.png")
canvas.create_image(150, 150, image=photoimage)


#logo = PhotoImage(file='NS1.png')
#label3 = Label(root, image=logo).pack()


#knop1 = Button(root, text='Route Planner', width=50, height=20, bg='#ffac00', commando=print('sjit')).place(x=250, y=500)
#knop2 = Button(root, text='Leave Now', width=50, height=20, bg='#ffac00', commando=print('sjit')).place(x=750, y=500)
#knop3 = Button(root, text='Route Planner', width=50, height=20, bg='#ffac00', commando=print('sjit')).place(x=1250, y=500)
#tkFont.Font(family='Helvetica', size=36, weight='bold') lettertype


class klok:
    def __init__(self):
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')

        self.watch = Label(text=self.time2, background='#ffac00', font=('Times New Roman',25,'bold'), fg='#003373')
        self.watch.place(x=1700, y=10)

        self.changeLabel()

    def changeLabel(self):
        self.time2 = time.strftime('%H:%M:%S')
        self.watch.configure(text=self.time2)
klok()
root.mainloop()

print('NS reisplanner')
print('1: Route Planner ')
print('2: Leave Now')
print('3: Travel Abroad')

while True:
    try:
       invoer = int(input(' '))
       if invoer <= 0:
           raise ValueError
       break
    except ValueError:
       print("error voer juiste optie in.")
       continue
if invoer == 1:
    plannen()
elif invoer == 2:
    nu_weg()
elif invoer == 3:
    print('Reizen naar het buitenland is momenteel niet mogelijk.')
