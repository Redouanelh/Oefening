studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
new_list = []
new_list2 = []

def gemiddelde_per_student(studentencijfers):
    for item in studentencijfers:
        a = sum(item)/len(item)
        new_list.append(a)
    return new_list

print(gemiddelde_per_student(studentencijfers))

def gemiddelde_van_alle_studenten(studentencijfers):
    for item2 in studentencijfers:
        b = sum(item2)/len(item2)
        new_list2.append(b)
    totaal_gemiddelde = sum(new_list2)/len(new_list2)
    return totaal_gemiddelde

print(gemiddelde_van_alle_studenten(studentencijfers))







