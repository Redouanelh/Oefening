def count():
    list = []
    with open ('kaartnummers.txt', 'r') as a:
        line = a.readlines()
        aantal_lines = len(line)
        strip = [a.strip() for a in line]

        for x in strip:
            gesplit = x.split(',')
            list.append(gesplit)
    kaartnummer = max(list)
    regel = list.index(kaartnummer)

    print('Dit bestand bestaat uit {} regels.'.format(aantal_lines))
    print('Het grootste kaartnummer binnen dit bestand is: {}, en dat getal staat op regel {}.'.format(kaartnummer[0], regel + 1 ))

count()
