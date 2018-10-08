lijst = eval(input("Geef lijst met minimaal 10 strings: "))
new_list = []

def count(lijst):
    for w in lijst:
        if len(w) == 4:
            new_list.append(w)
    return w

count(lijst)

print('De nieuw list met alle 4-letter woorden bestaat uit:',new_list)

#["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"] : kopiëer en plak deze lijst.
