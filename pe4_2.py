CijferICOR = 6
CijferPROG = 7
CijferCSN = 7

gemiddelde = ((CijferCSN + CijferPROG + CijferICOR)/3)

beloning = ((CijferCSN + CijferPROG + CijferICOR)*30)

Overzicht = ('Mijn cijfers' + ' (gemiddeld een' + ' ' + str(gemiddelde) + ')' + ' leveren een beloning van ' + str(beloning) + ' op!')

print(Overzicht)