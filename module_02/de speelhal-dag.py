ticketkost = int(input("vul hier de ticket prijs in centen:"))
vrienden = int(input("vul hier de aantal personen in:"))
prijsVIP = int(input("vul hier de prijs van de VIP in centen:"))
permin = int(input("vul hier de VIP minuten in:"))    
Totalmin = int(input("vul hier de totale minuten in:"))

prijs = ticketkost * vrienden  +Totalmin / permin * prijsVIP * vrienden 

print (f"Dit geweldige dagje-uit met {vrienden} mensen in de speelhal met {Totalmin} minuten VR kost je maar {prijs} euro")