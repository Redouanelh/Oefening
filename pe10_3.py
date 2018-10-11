gebruiker = input('Please insert your username: ')
beginstation = input('Please enter your starting position: ')
eindstation = input('Please enter your final position: ')

invoerstring = gebruiker + beginstation + eindstation

a = [ord(c) for c in invoerstring]

def code(invoerstring):
    b = [(3 + c) for c in a]
    invoerstring_code = [chr(c) for c in b]
    final = ''.join(invoerstring_code)
    print('De naam: ', invoerstring, 'levert: ', final, 'op.')

code(invoerstring)


