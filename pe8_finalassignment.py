def toon_aantal_kluizen():   # Het aantal beschikbare kluizen.
    with open('kluisnummers.txt', 'r') as f:
        bezet = len(f.readlines())
        beschikbaar = 12 - bezet
        print('Er zijn {} kluizen beschikbaar'.format(beschikbaar))

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
        kluisnummer = lijst[0]
        with open('kluisnummers.txt', 'a') as f:
            combinatie = '{};{}\n'.format(kluisnummer, code)
            f.write(combinatie)
        print('Uw kluisnummer is: {}'.format(kluisnummer))
    else:
        print('Er zijn momenteel geen kluizen beschikbaar. Probeer het later opnieuw!')

def kluis_openen():
    'Eigen kluis openen.'
    ingevoerde_kluis_nummer = input('Voer uw kluisnummer in: ')
    ingevoerde_kluis_code = input('Voer uw kluiscode in: ')
    goede_code = False
    goede_kluis = False

    with open('kluisnummers.txt', 'r') as f:
        for regel in f:
            stripped = regel.strip()
            splitted = stripped.split(';')
            kluisnummer = splitted[0]
            kluiscode = splitted[1]

            if ingevoerde_kluis_nummer == kluisnummer:
                goede_kluis = True
                if ingevoerde_kluis_code == kluiscode:
                    goede_code = True
                    break
                else:
                    goede_code = False
            else:
                goede_kluis = False

    if goede_code == True and goede_kluis == True:
        print('U heeft nu toegang tot uw kluis.')
    else:
        print('Uw kluisnummer en code combinatie is onjuist, probeer het opnieuw. \nAls dit probleem blijft bestaan, vraag dan om assistentie.')


while True:
    print('Welkom! Toets in welke optie voor u van toepassing is.\n')
    print('1: Ik wil weten hoeveel kluizen nog vrij zijn. \n2: Ik wil een nieuwe kluis. \n3: Ik wil even iets uit mijn kluis halen. \n4: Ik geef mijn kluis terug.')

    while True:
        try:
            optie = int(input('Optie: '))
            if 0 < optie <= 4:
                break
            print('Voer één van de bovenstaande getallen in.')
        except:
            print('Voer één van de bovenstaande getallen in.')


    if optie == 1:     # Optie 1
        toon_aantal_kluizen()
    elif optie == 2:     # Optie 2
        nieuwe_kluis()
    elif optie == 3:  # Optie 3
        kluis_openen()

