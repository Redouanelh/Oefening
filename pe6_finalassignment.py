print('Met de kleine onderstaande programma kunt u uw reiskosten berekenen, veel succes. \n')

def standaardprijs(afstandKM):
    if afstandKM <= 0:
        print('Dit is niet mogelijk.')
        prijs = 0
    elif afstandKM < 50:
        prijs = afstandKM * 0.80
    else:
        prijs = 15 + afstandKM * 0.60
    return prijs


Aantal_km = eval(input('Hoeveel kilometer bent u van plan af te gaan leggen?: '))

resultaat1 = standaardprijs(Aantal_km)
print(resultaat1, 'euro, dit is de standaard ritprijs. \n')


weekendrit = input('Is het een weekendrit?: ')
print('')

def ritprijs(leeftijd):
    if leeftijd > 12 and leeftijd < 65 and weekendrit == 'nee':
        prijs2 = resultaat1
    elif leeftijd > 12 and leeftijd < 65 and weekendrit == 'ja':
        prijs2 = resultaat1 * 0.60
    if leeftijd <= 12 and weekendrit == 'ja':
        prijs2 = resultaat1 * 0.65
    elif leeftijd >= 65 and weekendrit == 'ja':
        prijs2 = resultaat1 * 0.65
    elif leeftijd <= 12 and weekendrit == 'nee':
        prijs2 = resultaat1 * 0.70
    elif leeftijd >=65 and weekendrit == 'nee':
        prijs2 = resultaat1 * 0.70
    return prijs2


leeftijd1 = eval(input('Hoe oud bent u?: '))
print('')

resultaat2 = ritprijs(leeftijd1)
print(resultaat2, 'euro, dit is uw ritprijs.')

print('Nog een hele fijne reis!')










