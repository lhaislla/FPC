def pesquisa_binaria(lista, valor):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == valor:
            return meio
        elif lista[meio] > valor:
            direita = meio - 1
        else: # lista[meio] < valor
            esquerda = meio + 1
    return -1
lista = [0, 7, 23, 29, 45, 52, 57, 60, 77,93,100]
print(pesquisa_binaria(lista, 77))

