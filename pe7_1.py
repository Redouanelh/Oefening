def convert(C):
    fahrenheit = (C * 1.8) + 32
    return fahrenheit

def table():
    print('{:>3}{:>7}'.format('F', 'C'))
    for celcius in range(-30,50,10):
        print('{:>5}{:>7}'.format(round(convert(celcius), 2), round(float(celcius), 2)))

table()







