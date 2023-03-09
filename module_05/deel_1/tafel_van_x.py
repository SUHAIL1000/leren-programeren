
def getal():
    getal = int(input("voer een getal in "))
    print (f"de tafel van {getal} is:")
    for k in range(1,11):
        som = getal * k
        print (f"{k} x {getal} = {som}")
getal()

