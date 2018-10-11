import requests
import xmltodict
import datetime

vandaag = datetime.datetime.now()
datum = vandaag.strftime('%a %d %b %Y')
tijd = vandaag.strftime('%H:%M:%S')

print('{} , {}'.format(datum, tijd))

stad = input('Voer uw vertreklocatie in: ').title()
stad_eind = input('Voer uw eindbestemming in: ').title()

auth_details = ('redouan_school@outlook.com', '2SV3LsPcPB2SD5acBQ3omnyrhmyddwQwZUIHUzSF6C9kqvVG45juXQ')
api_url = 'http://webservices.ns.nl/ns-api-avt?station={}'.format(stad)

response = requests.get(api_url, auth=auth_details)

vertrekXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen: ')


for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']

    vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16]          # 18:36

    if eindbestemming == stad_eind:
        print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)
    else:
        pass

