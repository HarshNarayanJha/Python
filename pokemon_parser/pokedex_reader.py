import glob

pkmns = glob.glob(f"pkmns/*.txt")

# for pkmn in pkmns:
#     print(pkmn)

pk_name_or_id = input("Enter Pokemon Name or National Pokedex Number: ")
if pk_name_or_id.isnumeric():
    file_name = ""
    for pkmn in pkmns:
        if pk_name_or_id == pkmn.split("\\")[-1].split("-")[0]:
            file_name = pkmn
else:
    file_name = ""
    for pkmn in pkmns:
        if pk_name_or_id.upper() == pkmn.split("\\")[-1].split("-")[1].split(".")[0]:
            file_name = pkmn

data = []
with open(file_name, 'r') as fp:
    data = fp.readlines()

pk_id = data[0].strip("\n][")
pk_name = data[1].split('=')[1].strip("\n")
type_1 = ""
type_2 = ""
pk_dex = ""
for dat in data:
    if dat.startswith("Pokedex"):
        pk_dex = dat.split('=')[1].strip("\n")
    elif dat.startswith("Type1"):
        type_1 = dat.split("=")[1].strip("\n")
    elif dat.startswith("Type2"):
        type_2 = dat.split("=")[1].strip("\n")

print(f"\nNational Pokedex Index: {pk_id}")
print(f"{pk_name},")
if type_2:
    print(f"A {type_1.title()} and {type_2.title()} type pokemon.")
else:
    print(f"A {type_1.title()} type pokemon.")
print(f"{pk_dex}")