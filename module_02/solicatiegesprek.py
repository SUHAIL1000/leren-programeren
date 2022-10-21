print ("------------------------------------------------")
print ("| solicitatieformulier van de dircteur voor de habibi_jewels ")
print ("| er wordt u een aantal relevante vragen gesteld... ")
print ("| Gelieve die naar eer en geweten in te vullen ")
print ("| Als blijkt dat u aan de critaira voldoet dan komt ") 
print ("|uw in aanmerking voor een serius sollicitatiegesprek")
print ("|Ontspan maar blijf wakker, hier komen de vragen")
print ("|-----------------------------------------------")

diploma = input ("Bent u in bezit van een Diploma MBO-4 ondernemen? ja/nee:")
rijbewijs = input ("Bent u in bezit van een geldig Vrachtwagen rijbewijs? ja/nee:")
hoed = input ("Bent u in bezit van een hoge hoed? ja/nee:")
manVrouw = input ("Bent u een vrouw of een man?:")

if manVrouw == "man":
     snor = input ("heeft uw een snor?")
     if snor == "ja" :
        snorlengte = int(input ("hoe lang is uw snor"))

if manVrouw == "vrouw": 
     krullen = input("heeft uw rode krullen")
     if krullen ==  "ja" :
        krullenlengte = int(input("hoe lang zijn uw krullen"))

naam = input("wat is uw naam? ")
if naam == "r":
        raise NameError("r opdonderen")
lengte = int(input("hoe lang bent uw? "))
gewicht =  int(input("hoeveel weegt uw? "))
certificaat = input("Heeft Certificaat “Overleven met gevaarlijk personeel? ")
praktijk =  int(input("Meer dan 4 jaar praktijkervaring met dieren-dressuur? "))
jongleren = int(input("meer dan 5 jaar ervaring met jongleren"))
acrobatiek = int(input("meer dan 3 jaar praktijkervaring met acrobatiek"))
leeftijd = int(input("hoe oud bent uw? "))
ps4 = ("heeft uw ps4")
kleren = ("heeft uw kleren")

if diploma == "ja" and rijbewijs == "ja" and hoed == "ja" or hoed == "nee" and (manVrouw == "vrouw" and krullen == "ja" and krullenlengte > 20 or manVrouw == "man" and snor == "ja" and snorlengte > 10 and lengte > 1.50 and gewicht > 10 ) and certificaat == "ja" and (praktijk > 4 or jongleren > 5 or acrobatiek > 5):

        print("gefeliciteerd uw bent geslaagd")

else:
        print("uw bent komt niet aan de voorwaarden") 
 
 
