import random
kaarten = ["harten","klaveren","schop pen","ruiten"]
special_kaarten = [ "boer", "vrouw", "heer","aas"]
deck = ["jokers ","jokers 2"]

for u in kaarten:
    for x in special_kaarten:
        deck.append(f"{u},{x}")
    for e in range(2,11,1):
        deck.append(f"{u},{e}") 
random.shuffle(deck) 
print(deck)
for i in range(1,8): 
    kaart = deck[0]
    print(f"kaart {i}: {kaart} ") 
    deck.remove(kaart) 
print(f" 47 kaarten =  {deck}") 



