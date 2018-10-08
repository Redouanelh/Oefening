invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
list = invoer.split('-') #list zonder streepjes
new_list = [int(x) for x in list]

max = max(list) #klopt
min = min(list) #klopt
length = len(list) #klopt
sort = sorted(new_list) #klopt
som = sum(new_list) #klopt
gemiddelde = som/length #klopt

print('Gesorteerde list van ints:', sort)
print('Grootste getal:', max,', en het kleinste getal is:',min)
print('Aantal getallen:', length, 'en de som van de getallen is:', som)
print('Het gemiddelde is:', gemiddelde)




