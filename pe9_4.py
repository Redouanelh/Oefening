def ticker():
    dictionary = {}
    with open('names.txt') as file:
        for line in file:
            key, value = line.split(":")
            dictionary[key] = value

    jaja= input('Enter a symbol: ')
    for company, symbol in dictionary.items():
        if jaja in symbol:
            print(company)


    neenee = input('Enter a company: ')
    for company, symbol in dictionary.items():
        if neenee in company:
            print(symbol)


ticker()