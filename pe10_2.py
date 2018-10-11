import random

a = random.randrange(1, 7)
b = random.randrange(1, 7)

gevangenis = []

def monopolyworp():
    while True:
        print('Welcome!\nType something to start rolling the dices!')
        antwoord = input('Choice: ')
        if antwoord != '1':
            print('You need to insert 1 to start rolling!')
            break
        if antwoord == '1':
            print('Now rolling ...\n')
        if a != b:
            print('You rolled', a , 'and', b, 'which gives you a total of', a + b, '!')
            break
        print('You rolled the same number, Let\'s try that again!\n')
        gevangenis.append('a')
        if len(gevangenis) == 3:
            print('You doubled three times, time to go to prison mate!')
            break


monopolyworp()



