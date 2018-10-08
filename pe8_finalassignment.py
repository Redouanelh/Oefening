print('Welkom! Toets in welke optie voor u van toepassing is.\n')
print('1: Ik wil weten hoeveel kluizen nog vrij zijn. \n2: Ik wil een nieuwe kluis. \n3: Ik wil even iets uit mijn kluis halen. \n4: Ik geef mijn kluis terug.')

while True:
    optie = int(input('Optie: '))
    if 0 < optie <= 4:
        break
    print('Voer één van de bovenstaande getallen in.')


def toon_aantal_kluizen():   # Het aantal beschikbare kluizen.
    with open('kluisnummers.txt', 'r') as f:
        bezet = len(f.readlines())
        beschikbaar = 12 - bezet
        print('Er zijn {} kluizen beschikbaar'.format(beschikbaar))

if optie == 1:     # Optie 1
    print(toon_aantal_kluizen())

def nieuwe_kluis():    # Een nieuwe kluis opvragen.
    lijst = []
    for a in range(1,13):
        lijst.append(a)
    with open('kluisnummers.txt', 'r') as f:
        for regel in f:
            regel = regel.split(';')
            kluisnummer = int(regel[0])
            if kluisnummer in lijst:
                lijst.remove(kluisnummer)
        code = input('Voer uw code in: ')
    if len(lijst) > 0:
        lijst.sort()
        kluisnummer = lijst[0]
        with open('kluisnummers.txt', 'a') as f:
            combinatie = '{};{}\n'.format(kluisnummer, code)
            f.write(combinatie)
        print('Uw kluisnummer is: {}'.format(kluisnummer))
    else:
        print('Er zijn momenteel geen kluizen beschikbaar. Probeer het later opnieuw!')

if optie == 2:     # Optie 2
    print(nieuwe_kluis())


def kluis_openen():  # Eigen kluis openen.
    kluis_nummer = input('Voer uw kluisnummer in: ')
    kluis_code = input('Voer uw kluiscode in: ')
    goede_code = False
    goede_kluis = False

    with open('kluisnummers.txt', 'r') as f:
        for regel in f:
            stripped = regel.strip()
            splitted = stripped.split(';')
            kluisnummer = splitted[0]
            kluiscode = splitted[1]

            if kluis_nummer in kluisnummer:
                goede_kluis = True
                if kluis_code == kluiscode:
                    goede_code = True
                    break
                else:
                    goede_kluis = False
            elif kluis_nummer not in kluisnummer:
                goede_kluis = False

    if goede_code == True and goede_kluis == True:
        print('U heeft nu toegang tot uw kluis.')
    elif goede_code == False and goede_kluis == False:
        print('Uw kluisnummer en code combinatie is onjuist, probeer het opnieuw. \nAls dit probleem blijft bestaan, vraag dan om assistentie.')

if optie == 3:  # Optie 3
    print(kluis_openen())

if optie == 4:    # Optie 4
    print('Hier zal de docent me vast mee willen helpen :)')

