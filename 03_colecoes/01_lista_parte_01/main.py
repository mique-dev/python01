# declaração de lista
nomes = ["fulano", "beltrano", "ciclano", "João", "Maria", "Ana", "José", "Carla"]

import os
import time
os.system("cls")

# ordena a lista em ordem alfabética
nomes.sort()

# re-exibir lista completa em ordem alfabética

print("\nOrdem alfabética: \n")
for nome in nomes:
    print(nome)

nomes.sort(reverse=True)
print("\nOrdem alfabética reversa:\n")
for nome in nomes:
    print(nome)