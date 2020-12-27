from utils import *

DAY = day(__file__)
DATA = get_input(DAY)

xDATA="""
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
""".split("\n")

INGREDIENTS = {}
ALLERGENS = {}
for _ in DATA:
    if _:
        ingredients, allergens = _[:-1].split(" (contains ")
        ingredients = ingredients.split()
        allergens = ''.join(allergens).split(", ")
        for allergen in allergens:
            if allergen in ALLERGENS:
                ALLERGENS[allergen] &= set(ingredients)
            else:
                ALLERGENS[allergen] = set(ingredients)
        for ingredient in ingredients:
            INGREDIENTS[ingredient] = INGREDIENTS.get(ingredient, 0) + 1

SUSPECT = set()
for allergen in ALLERGENS:
    SUSPECT |= ALLERGENS[allergen]

CLEARED = set(INGREDIENTS) - SUSPECT

@part1
def func(expect=2203):
    acc = 0
    for c in CLEARED:
        acc += INGREDIENTS[c]
    return acc

@part2
def func(expect="fqfm,kxjttzg,ldm,mnzbc,zjmdst,ndvrq,fkjmz,kjkrm"):
    confirmed = []
    while ALLERGENS:
        for allergen, possible in ALLERGENS.items():
            if len(possible) == 1:
                ingredient = possible.pop()
                confirmed.append(allergen + ":" + ingredient)
                break
        for v in ALLERGENS.values():
            if ingredient in v:
                v.remove(ingredient)
        ALLERGENS.pop(allergen)
    return ','.join([_.split(":")[1] for _ in sorted(confirmed)])
