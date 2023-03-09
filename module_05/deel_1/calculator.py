def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2


keuze = " "

while not keuze in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
    
    keuzen = input("Wat wilt uw doen ? : a) getallen optellen : b) getallen afrtekken : c) getallen vermenigvuldigen d) getallen delen : e) getallen ophogen : f) getallen : g) getallen verdubbelen h) getalen halveren  ")
    if keuze == "i":
        exit()