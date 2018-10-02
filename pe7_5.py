zin = input('Type hier een zin waarvan ik het gemiddelde zal berekenen.: ')

woorden = zin.split()

gemiddelde_lengte = sum(len(woord) for woord in woorden) / len(woorden)

print(gemiddelde_lengte)