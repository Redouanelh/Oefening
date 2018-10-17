import csv

#list = []
new_list = []

#with open('opdr11.4.csv', 'a', newline='') as csvv:
    #writer = csv.writer(csvv, delimiter=';')

    #while True:
        #artikelnummer = input("Artikelnummer: ")
        #artikelcode = input("Artikelcode: ")
        #naam = input("Naam: ")
        #voorraad = input('Voorraad: ')
        #prijs = input('Prijs: ')

        #list.extend([artikelnummer, artikelcode, naam, voorraad, prijs])

        #writer.writerow(list)
        #break

with open('opdr11.4.csv', 'r') as information:
    reader = csv.reader(information, delimiter=';')
    max = 0
    min = 500
    name = ''
    name2 = ''
    for row in reader:
        prijs = float(row[4])
        voorraad = int(row[3])
        if prijs > max:
           max = prijs
           name = row[2]
        if voorraad < min:
            min = voorraad
            name2 = row[0]
        new_list.append(int(row[3]))

total = sum(new_list)

print('Het duurste artikel is de {} met als prijs {},- euro.'.format(name, max))
print('Er zijn slechts {} exemplaren in voorraad met nummer {}.'.format(min, name2))
print('In totaal hebben wij {} producten in ons magazijn liggen.'.format(total))