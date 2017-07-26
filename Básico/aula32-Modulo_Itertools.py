from itertools import permutations

lista = [1, 2, 3]

for p in permutations(lista):
    print(p)

from itertools import combinations

print()

for c in combinations(lista, 2):
    print(c)