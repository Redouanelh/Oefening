s = "Guido van Rossum heeft programmeertaal Python bedacht."

for klinker in s:
    if klinker in ('aeiouAEIOU'):
        print(klinker)
