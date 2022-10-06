# suhail habibi
#opdracht: pizzacalculator 

from xml.dom import ValidationErr


smallAmount = 5 #enkel prijs small 
mediumAmount = 8 #enkel prijs small 
largeAmount = 11 #enkel prijs small
a = 0

while a < 1:
    try:
        small =int(input("hoeveel small pizza's wilt uw?:"))
        medium =int(input("hoeveel medium pizza's wilt uw?:"))
        large =int(input("hoeveel large pizza's wilt uw?:"))
        a = 10
    except ValueError:
        print ("een nummer graag.")
        a = 0


smallprice = int(small * smallAmount)
mediumprice = int(medium*mediumAmount)
largeprice = int(large*largeAmount)


totaal = smallprice + mediumprice + largeprice

print(f"{small} small pizza €{smallprice}  ")
print(f"{medium} medium pizza €{mediumprice}  ")
print(f"{large} large pizza €{largeprice}  ")
print(f"uw totale prijs is €{totaal}")


