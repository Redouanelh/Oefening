cijfers = {'Redouan': 9.5, 'Hakan': 2.0, 'Jan': 6.0, 'Kees': 9.1, 'Ben': 8.0, 'Floor': 9.8, 'Daan': 4.0, 'Bas': 7.6}
new_list = []


naam = input('Voer je naam in om het behaalde cijfer te zien: ')
cijfer = cijfers[naam]

print('Jij hebt als cijfer een dikke', cijfer, '!', '\n')


def max(cijfers):
    for name, shit in cijfers.items():
        if shit >= 9:
            print(name, shit)

print('De mensen met een cijfer boven de 9.0 zijn:\n''')

max(cijfers)

