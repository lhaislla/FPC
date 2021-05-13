def busca_sequencial(lista, valor):
    pos = 0
    estado= False	
    while pos < len(lista) and not estado:
        if lista[pos] == valor:
            estado = True
        else:
            pos = pos+1
    return estado
lista1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(busca_sequencial(lista1, 42))
