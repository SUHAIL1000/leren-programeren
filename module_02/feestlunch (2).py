crossantjes = int(input("vul hier de aantal crossantjes in:"))
prijsproduct = int(input("vul hier de prijs van het product in centen:"))
stokbroden = int(input("vul hier de aantal stokbroden:"))
prijsproduct1 = int(input("vul hier de prijs van het product in centen:"))
kortingsbonnen = int(input("vul hier de aantal kortingsbonnen:"))
kortingsprijs = int(input("vul hier de prijs van de kortingsbonnen in centen:"))

prijs = crossantjes * prijsproduct + stokbroden * prijsproduct1 - kortingsbonnen * kortingsprijs

print(f"De feestlunch kost je bij de bakker {prijs} euro voor de {crossantjes} crossantjes en de {stokbroden} stokbroden als de {kortingsbonnen} kortingbonnen nog geldig zijn!")