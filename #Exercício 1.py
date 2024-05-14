# Exercício 1
largura = float(input('Informe a largura do terreno: '))
comprimento = float(input('Informe o comprimento do terreno: '))


def area(l, c):
    s = l * c
    print(
        f'A área de um terreno com largura {largura} e comprimento {comprimento} é de {s}')


area(largura, comprimento)
