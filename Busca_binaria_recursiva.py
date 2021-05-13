def pesquisa_binaria_recursiva(lista, esquerda, direita, valor):
    # Caso base: Não tem o elemento que esta sendo procurado 
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # Valor procurado esta no meio da lista  
    if lista[meio] == valor:
        return meio
    # 3. referencia errada, continua com a  busca. 
    elif lista[meio] > valor:
        return pesquisa_binaria_recursiva(lista, esquerda, meio - 1, valor)
        
    else: # A[meio] < item
        return pesquisa_binaria_recursiva(lista, meio + 1, direita, valor)


lista = [0, 7, 23, 29, 45, 52, 57, 60, 77,93,100]
print( pesquisa_binaria_recursiva(lista, 0, len(lista) - 1, 100))