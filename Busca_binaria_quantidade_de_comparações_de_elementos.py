#Função busca que retorna a quantidade de comparações 
def busca(lista, item, qtd):
    if len(lista) == 0:
        return qtd
    else:
        if len(lista) % 2 == 0:
            meio = (len(lista)// 2) -1
        elif len(lista)% 2 != 0 :
            meio =(len(lista) // 2) 
        if lista[meio] == item:
            qtd += 1
            return qtd
        else:
            if item < lista[meio]:
                qtd += 1
                return busca(lista[:meio], item, qtd)
            else:
                qtd += 1
                return busca(lista[meio+1:], item, qtd)
    return qtd

# Tratamento da entrada: 
'''A entrada deve ser:  
exemplo: 15 9 11 15 20 25 29 32 41 44 50 60 65 72 91 99 60 45 20 8 9 19
Sendo o primeiro número a quantidade de elementos da lista,
Após os elementos da lista, terão os elementos a serem buscados'''

entrada = input("Digite sua entrada: ").split()
entrada = [int(x) for x in entrada]
tam_busca = entrada[0]
lista = entrada[1:tam_busca + 1] 
lista_itens= entrada[tam_busca +1 : len(entrada)]
resultado =[]

# Chamada da função até que a lista_Itens esteja vazia: 
while lista_itens != []:
    remove = lista_itens.pop(0)
    resultado.append(busca(lista, remove, 0))      
    entrega = ' '.join(str(e) for e in resultado)
    if lista_itens == []:
        print(entrega)
