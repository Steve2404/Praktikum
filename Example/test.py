# anniversaire = ["anniversaire", "Étienne"]
# tache = ["tache", "ranger la cuisine"]
# rende_vous = ["rende-vous", "10.00", "11.00", "reunion professionnelle"]
# aujourd_hui = [anniversaire, tache, rende_vous]

# for activite in aujourd_hui:
#     match activite:
#         case["anniversaire", personne]:
#             print(f"Pensez a souhaiter un joyeux anniversaire a {personne}")
#         case ["tache", objet]:
#             print(f"Pensez a {objet}.")
#         case ["rende-vous", debut, fin, objet]:
#             print(f"Rende-vous prevu de {debut} a {fin}: {objet}")

# Trie de l inventaire:
inventaire = [
    ("pommes", 22),
    ("melon", 4),
    ("poire", 18),
    ("fraises", 76), 
    ("prunes", 51)
]
inventaire_inverse = [(qtt, nom_fruit) for nom_fruit, qtt in inventaire]
inventaire = [(nom_fruit, qtt) for qtt, nom_fruit in sorted(inventaire_inverse, reverse=True)]
for elt in inventaire:
    print(elt)