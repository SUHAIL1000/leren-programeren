import random
kleuren = ["rood","blauw","groen","geel","bruin"]

hoeveelheid = int(input("Hoeveel M&Ms er aan de zak toegevoegd worden?: "))
zak = {} 

getal = 1
for u in range(hoeveelheid):
    random_k = random.choice(kleuren)
    if random_k not in zak:
        
        zak[random_k] =1
    elif random_k in zak:
        zak[random_k] +=1

print(zak)