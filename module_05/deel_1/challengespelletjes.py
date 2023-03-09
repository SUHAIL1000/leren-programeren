spel = 24.95
aantal = 60

hoeveelheid = int(input("hoeveel spel wil je inkopen"))
leverancier = (aantal -1 )*0.25
inkoopeprijs = (spel / 100 * 60)


totaal = (inkoopeprijs * hoeveelheid + leverancier )

print (totaal)

