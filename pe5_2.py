naam = input('Wat is uw naam?')

leeftijd = eval(input('Noteer uw leeftijd: '))

paspoort = input('Beschikt u over een paspoort? ')

if leeftijd >= 18 and paspoort == 'Ja' or 'ja':
    print('Gefeliciteerd' + '' + naam + ',je mag stemmen!')

else:
    print('Helaas, je mag niet stemmen.')