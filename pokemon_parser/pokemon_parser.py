import os
if not os.path.exists('./pkmns/'):
    os.mkdir('./pkmns/')

pokemon_file = open('pokemon.txt', 'r')
lines = pokemon_file.readlines()
pokemon_file.close()

# for i in range(len(lines)):
#     lines[i] = lines[i].strip("\n")

pkmns = []
buffer = []
for line in lines:
    if line.startswith("#"):
        if len(buffer) > 0:
            pkmns.append(buffer.copy())
        buffer.clear()
    else:
        buffer.append(line)

for pkmn in pkmns:
    pk_id = pkmn[0].strip("\n][")
    pk_name = pkmn[2].split("=")[1].strip("\n")
    pkmn[-1] = pkmn[-1].strip("\n")
    with open(f"./pkmns/{pk_id}-{pk_name}.txt", 'w') as pk:
        pk.writelines(pkmn)
