import datetime

vandaag = datetime.datetime.now()
datum = vandaag.strftime('%a %d %b %Y')
tijd = vandaag.strftime('%H:%M:%S')

while True:
    naam = input('Name: ')
    with open('hardlopers.txt', 'a') as a:
        a.write('{}, {}, {}\n'.format(datum, tijd, naam))
        print('{} , {}, {} Saved. '.format(datum, tijd, naam))
















