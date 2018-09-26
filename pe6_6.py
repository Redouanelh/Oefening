lijst1 = ['a', 'b', 'c']
lijst2 = ['d', 'e', 'f']

print(lijst1)
print('Nu gaat het gewijzigd worden.')

def wijzig(letterlijst):
    lijst = lijst1.clear()
    lijst1.extend(lijst2)

wijzig(lijst1)

print(lijst1)