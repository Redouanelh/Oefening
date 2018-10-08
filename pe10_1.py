bruin = {'Boxtel', 'Best', 'Breukenlaan', 'Eindhoven', 'Helmond \'t Hout', 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Breukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}

overeenkomsten = groen.intersection(bruin)
verschillen = bruin.difference(groen)
union = groen.union(bruin)

print('De overeenkomst tussen de twee lijnen zijn:', overeenkomsten, '\n')

print('Lijn bruin verschilt t.o.v. lijn groen met de volgende stations:', verschillen, '\n')

print('Dit zijn alle stations van lijn groen en lijn bruin bij elkaar:', union)
