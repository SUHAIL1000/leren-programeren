def addition (number1, number2):
    return number1 + number2
def subtraction (number1, number2):
    return number1 - number2
def multiplication (number1, number2):
    return number1 * number2
def division (number1, number2):
    return number1 / number2

keuze = " "
while not keuze in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
    keuze = input("Wat wilt u doen? A = getallen optellen, B = getallen aftrekken, C = getallen vermenigvuldigen, D = getallen delen, E = getal ophogen, F = getal verlagen, G = getal verdubbelen of H = getal halveren?, type 'niks' als je niks wilt doen: ").lower()
    if keuze == "niks":
        exit()

aantal = -1
while True:
    if aantal > -1 and keuze != 'i' and keuze in ('a', 'b', 'c', 'd'):
        number1 = aantal
        number2 = int(input("Geef de 2e getal op: "))



    elif keuze in ('e', 'f', 'g', 'h'):
        number1 = int(input("Geef een getal op: "))

    else:
        exit()

    if keuze == "a":
        aantal = addition(number1, number2)
        print(aantal)
    elif keuze == "b":
        aantal = subtraction(number1, number2)
        print(aantal)
    elif keuze == "c":
        aantal = multiplication(number1,number2)
        print(aantal)
    elif keuze == "d":
        aantal = division(number1,number2)
        print(aantal)
    elif keuze == "e":
        aantal = addition(number1,number2)
        print(aantal)
    elif keuze == "f":
        aantal = subtraction(number1,number2)
        print(aantal)
    elif keuze == "g":
        aantal = multiplication(number1,number2)
        print(aantal)
    elif keuze == "h":
        aantal = division(number1,number2)
        print(aantal)
    
