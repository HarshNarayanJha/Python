import csv
import random

pkmns = {}

fp = open('pokemon_all_gen1-7.csv', 'r')
reader = csv.reader(fp)
headers = next(reader)

for line in reader:
    _id = int(line[0])
    pkmns[_id] = {}
    # print(line)
    for h, val in zip(headers[1:], line[1:]):
        if val.isnumeric(): val = int(val)
        pkmns[_id][h] = val

# rand_id = random.choice(list(pkmns.keys()))
# print(pkmns[rand_id]['Pokedex'])
# name = input(">>> ")
# if pkmns[rand_id]['Name'] == name: print("Yes")
# else: print(pkmns[rand_id]['Name'])
hp = {}
for i in pkmns:
    hp[i] = pkmns[i]['Sp Atk']

max_hp = min(hp.values())
for i in hp:
    if hp[i] == max_hp:
        print(pkmns[i]['Name'])
        print(max_hp)