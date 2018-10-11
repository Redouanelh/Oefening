while True:
    try:
        aantal_reizigers = int(input('Met hoeveel zijn jullie? : '))
        if aantal_reizigers < 0:
            print('Geen negatief getal invoeren!')
            break
        prijs_per_persoon = print(4356 / aantal_reizigers)
    except ZeroDivisionError:
        print('Je kunt niet op reis gaan met 0 man!')
    except ValueError:
        print('Voer een cijfer in, geen woord!')
    except:
        print('Onjuiste invoer!')