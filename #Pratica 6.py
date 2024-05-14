# Pratica 6
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 7, 4, 8]
dobra(valores)
print(valores)
