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

aantal = -1
while True:
    if aantal > -1 and keuze != 'i' and keuze in ('a', 'b', 'c', 'd'):
        n1 = aantal
        n2 = int(input("Geef de 2e getal op: "))

    elif aantal > -1 and keuze != 'i' and keuze in ('e', 'f', 'g', 'h'):
        n1 = aantal
 
    elif keuze in ('a', 'b', 'c', 'd'):
     n1 = int(input("geef een getal op :"))
     n2 = int(input("geef nog een getal op :"))

    elif keuze in ('e', 'f', 'g', 'h'):
        n1 = int(input("Geef een getal op: "))
    else: 
        exit()