def addition(number1,number2):
    return number1 + number2
def subtraction(number1,number2):
    return number1 - number2
def multiplicaton(number1,number2):
    return number1 * number2
def division(number1,number2):
    return number1 / number2

keuze = (input("wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren) i) ")).lower()

n1 = int(input("geef getal op "))

while True:


    if keuze == "a":

        n2 = int(input("geef getal 2e op "))
        antwoord = addition(n1,n2)

    elif keuze == "b":

        n2 = int(input("geef getal 2e op "))
        antwoord = subtraction(n1,n2)

    elif keuze == "c":

        n2 = int(input("geef getal 2e op "))
        antwoord = multiplicaton(n1,n2)
        
    elif keuze == "d":

        n2 = int(input("geef getal 2e op "))
        antwoord = division(n1,n2)

    elif keuze == "e":
        n2 = 1
        antwoord = addition(n1,n2)

    elif keuze == "f":
        n2 = 1
        antwoord = addition(n1,n2)

    elif keuze == "g":
        n2 = 2
        antwoord = multiplicaton(n1,n2)
    elif keuze == "h":
            n2 = 2
            antwoord = division(n1,n2)

    elif keuze == "i":
        break
    n1= antwoord
    print(antwoord)
    keuze = (input("wat wilt u doen met deze antwoord ? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? ")).lower()

  
#moet ook werke met floet 