new_list = []

def namen():
    while True:
        naam = input('Voer een naam in: ')
        if naam == '':
            break
        new_list.append(naam)
    return new_list

namen()
print(new_list)

from collections import Counter

print(Counter(new_list))
