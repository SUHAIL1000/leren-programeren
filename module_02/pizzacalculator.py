# suhail habibi
#opdracht: pizzacalculator 

smallAmount = 5 #enkel prijs small 
mediumAmount = 8 #enkel prijs small 
largeAmount = 11 #enkel prijs small

btw = 9 #btw prijs
small =int(input("hoeveel small pizza's wilt uw?:"))
medium =int(input("hoeveel medium pizza's wilt uw?:"))
large =int(input("hoeveel large pizza's wilt uw?:"))

smallprice = int(small * smallAmount)
mediumprice = int(medium*mediumAmount)
largeprice = int(large*largeAmount)

print(f"{small} small pizza €{small} €{small}  ")
print(f"{medium} medium pizza €{medium} €{medium}  ")
print(f"{large} large pizza €{large} €{large}  ")


