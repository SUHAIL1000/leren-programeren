# # getal = int(input("voer een getal in "))
# # print (f"de tafel van {getal} is:")
# # for k in range(1,11):
# #     som = getal * k
# #     print (f"{k} x {getal} = {som}")
# lijst=[12,34,56,7,8]
# for k in lijst: 
#    print (k)

# getal_1= int(input("voer getalt in "))
# getal_2 = int(input("voer getalt in "))

# if getal_1 < getal_2:
#     print (getal_2)
# else :
#     print (getal_1 ) 

# mijn_lijst = ["anton","berat","cors","dirck","eduard"]
# leeftijden = [16,17,12,29,15]
# for naam,leeftijd in zip(mijn_lijst,leeftijden):
#     print(f"hello {naam} je  bent {leeftijd} oud")
# mijn_lijst_3 = list(zip (mijn_lijst,leeftijden))
# print(mijn_lijst_3)

# antwoord = ("voer je of nee")
# while antwoord not in ("voer ja of nee"):
#     print("het is goed")

# while True:
#     antwoord = input("voer ja of nee")
#     if antwoord in ("ja,nee"):
#         break                                            

# mijn_dict = {
#     123456789: "jouke corbijn",
#     123456789: "jan janssen",
#     123456789: "ogulcan dinc",
#     123456789: "renson koolj",

# }
# for val in mijn_dict.values():
#     print(val)

# for val in mijn_dict.keys():
#     print(val)
# print(dir(mijn_dict))

# mijn_lijst = [1]

# print(dir(mijn_lijst))

#mijn_naam_lijst ={}


# while True:
#     naam = input("wat is je naam (stop om te stoppen)?")

#     if naam == "stop":
#         break
#     if naam in mijn_naam_lijst:
#         if input("wilt uw bijwerken? ja/nee") !="ja":
#             continue
#     leeftijd = int(input("Wat is je leeftijd"))
    
#     mijn_naam_lijst[naam] = leeftijd

# Maak een lege boodschappenlijst aan
# Maak een lege boodschappenlijst aan



# for x in range (1,11):
    
#     print (x)

# def vraag_een_getal(vraag: str) -> int:
#     while True:
#         try:
#             lefftijd = int(input("voer je leeftijd in"))
#             break 
#         except ValueError:
#             print("je moet een getal invoeren ")
#             continue 
        
#     return getal

# leeftijd = vraag_een_getal("Voer leeftijd in:")

# def lengte(vraag: str) -> str:
#     lengte = input("hoe heet  ben je ")
#     lengte  = lengte.lower()

#     return lengte 

# lengte  = lengte("hoe heet  je ")
# print(lengte)

# def naam(vraag: str) -> str:
#     naam = input("hoe heet je ")
#     naam = naam.lower()
#     return naam

# naam = naam("hoe heet je ")
# print (f"{naam}"
