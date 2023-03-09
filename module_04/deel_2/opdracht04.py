from fruitmand import fruitmand
import random



vraag = int(input('aantal?'))


for x in range(vraag):
    random1 = random.choice(fruitmand)
    print(random1['name'])

