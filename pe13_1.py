import xmltodict

def xml (filename):
    with open(filename) as xmlfile:
        filecontent = xmlfile.read()
        xmldictionary = xmltodict.parse(filecontent)
        return xmldictionary

dic = xml('opdr13_1.xml')


for x in dic['artikelen']['artikel']:
    name = x['naam']
    print(name)