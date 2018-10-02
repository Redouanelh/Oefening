def optelling():
    totaal = 0
    while True:
        getal = eval(input('Voer een getal in: '))
        if getal == 0:
            break
        totaal += getal
    print('Het totaal van alle ingevoerde getallen komt uit op',totaal,'.' )


optelling()