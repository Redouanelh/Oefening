with open('kaartnummers.txt') as f:
    for line in f:
        f1= line.split()
        print(f1[1], f1[2], 'heeft kaartnummer:', f1[0])