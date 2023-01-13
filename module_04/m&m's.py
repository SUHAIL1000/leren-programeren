import random
M_en_Ms = ("oranje", "blauw", "groen", "bruin","geel")

vraag = int(input("Hoeveel M&Ms er aan de zak toegevoegd worden?: "))
zak = []
for u in range(vraag):
    kleur = random.choice(M_en_Ms)


    zak.append(kleur)

print(zak)

