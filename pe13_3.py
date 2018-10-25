import xmltodict

def xml(filename):
    with open(filename) as xmlfile:
        filecontent = xmlfile.read()
        xmldictionary = xmltodict.parse(filecontent)
        return xmldictionary

dic = xml('opdr13_3.xml')

def codename():
    'Stap 1'
    listname = []
    listcode = []
    listcodename = [listcode, listname]

    for x in dic['Stations']['Station']:
        code = x['Code']
        listcode.append(code)
    for y in dic['Stations']['Station']:
        type = y['Type']
        listname.append(type)
    for a in zip(*listcodename):
        print(' - '.join(a))

print('Dit zijn de codes en types van de 4 stations: ')
codename()
print('')

def codesynoniem():
    'Stap 2'
    listcode = []
    for x in dic['Stations']['Station']:
        code = x['Code']
        listcode.append(code)
    for y in dic['Stations']['Station']:
        if y['Synoniemen'] is not None:
            print(listcode[0], '-', y['Synoniemen'])



print('Dit zijn alle stations met één of meer synoniemen: ')
codesynoniem()
print('')

def codelangenaam():
    'Stap 3'
    listcode = []
    listlangenaam = []
    listcodelangenaam = [listcode, listlangenaam]
    for x in dic['Stations']['Station']:
        code = x['Code']
        listcode.append(code)
    for y in dic['Stations']['Station']:
        langenaam = y['Namen']['Lang']
        listlangenaam.append(langenaam)
    for a in zip(*listcodelangenaam):
        print(' - '.join(a))

print('Dit is de lange naam van elk station: ')
codelangenaam()














