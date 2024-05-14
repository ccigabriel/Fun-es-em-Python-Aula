# Exercício 5
import random

numeros = []


def sorteia():
    sorteio = [random.randint(0, 99) for c in range(0, 5)]
    numeros.extend(sorteio)  # adiciona os números sorteados na lista


sorteia()
print(f'Os números sorteados foram: {numeros}')
