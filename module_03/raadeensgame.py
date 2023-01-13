import random

jaofnee = input("wil je getal raden ja of nee : ")
if jaofnee.lower() == "ja":
    print("oke ")
else:
    print("exit")
    exit()
AANTAL_RONDES = 3
ronde = 0
punten = 0

while ronde <3:

    geheim_getal = random.randint(1, 1000)
    print(geheim_getal)
    pogingen = 0
    while pogingen < 10:  
        geraden_getal = int(input("Raad een getal tussen 1 en 1000: "))
        if geraden_getal == geheim_getal:
                print("goed")
                punten += 1
                ronde += 1
                break
        verschil = abs(geraden_getal - geheim_getal)
        pogingen += 1 
    
        if geraden_getal > geheim_getal:
            print("Lager")
        elif geraden_getal < geheim_getal:
            print("Hoger")
        if verschil <= 20:
            print("erg warm")
        elif verschil <= 50:
            print("warm")
    if ronde <3:
        ronden_ja_of_nee = input("wil je nog een keer raden ja of nee?: ")
        if ronden_ja_of_nee != "ja":
            break
        else:
            print(f"je hebt {punten} Punt(en)")

print(f"je score is {punten} en je hebt {ronde} rondes gespeeld")

        
        
