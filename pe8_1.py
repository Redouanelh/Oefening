maandnummer = eval(input('Voer uw maandnummer in. '))

def seizoen(maand):
    if 3 <= maandnummer <= 5:
        print('Het is nu lente.')
    elif 6 <= maandnummer <= 8:
        print('Het is nu zomer.')
    elif 9 <= maandnummer <= 11:
        print('Het is nu herfst.')
    elif maandnummer == 0:
        print('Dit is helaas niet mogelijk, voer een ander nummer in.')
    else:
        print('Het is nu winter.')

seizoen(maandnummer)


