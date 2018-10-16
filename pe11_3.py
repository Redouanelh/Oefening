import csv

list = []
new_list = []

with open('opdr11.3.csv', 'a', newline='') as csvv:
    writer = csv.writer(csvv, delimiter=';')

    while True:
        naam = input("Geef je naam: ")
        if naam == 'einde':
            break
        speeldatum = input("Geef je speeldatum: ")
        score = input("Geef je score: ")

        list.extend([naam, speeldatum, score])

        writer.writerow(list)
        break

with open('opdr11.3.csv', 'r') as information:
    reader = csv.reader(information, delimiter=';')
    for row in reader:
        new_list.append(row[2])


a = max(new_list)
print(a)


with open('opdr11.3.csv', 'r') as information:
    reader = csv.reader(information, delimiter=';')
    for row in reader:
        if a == row[2]:
            print('Highest score is: {} on {} by {}'.format(row[2], row[1], row[0]))