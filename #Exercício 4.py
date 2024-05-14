# Exercício 4

def maior(lista):
    maior_numero = lista[0] #Supoe que o maior número é o primeiro
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero #retorna o maior número

numeros = []
for c in range(0,5):
    numero = int(input('Digite um número: '))
    numeros.append(numero)


    
maior_numero = maior(numeros)
print(f'O maior número digitado é: {maior_numero}')
