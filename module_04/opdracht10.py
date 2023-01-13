from fruitmand import fruitmand
from operator import itemgetter

nieuw_list = sorted(fruitmand,key=itemgetter("weight"),reverse=True)

for fruit in nieuw_list:
    print("fruitsoort :",fruit["name"])
    print("fruitgewicht :",fruit["weight"]/1000,"kg")
