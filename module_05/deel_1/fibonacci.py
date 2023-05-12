vraag = int(input("geef getal "))

def fibonacci(fibo):
    teler = 0
    teler_02 = 1


    for x in range (vraag -2):
        getal_1 = fibo[teler]
        getal_02 = fibo[teler_02]
        antwoord = getal_1 + getal_02
        fibo.append(antwoord)
        teler += 1
        teler_02 += 1

    guldensnede =  antwoord/getal_02
    return guldensnede



start = [0,1]
print(fibonacci(start))