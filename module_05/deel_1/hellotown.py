def mijn_function(getal):
    lege_lijstje = []
    for k in range(1,getal+1):
        lege_lijstje.append(f"Hello from function town {k}! ")
    return lege_lijstje

for z in mijn_function(8):
    print(z)

