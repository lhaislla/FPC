#Entradas do programa/ Declaração de váriaveis 
entrada = input("Digite sua entrada: ").split()
entrada = [int(x) for x in entrada]
QTDE_CONTAINERS = entrada[0]
TAM_CONTAINER = entrada[1]
TAM_OVERFLOW = entrada[2]
QTDE_INSERCOES = entrada[3]
OP = entrada[4:len(entrada)]
ELEMENTOS_INSERIDOS = OP[0:QTDE_INSERCOES]
ELEMENTOS_BUSCA = OP[8:len(OP)]
TAM_TOTAL = QTDE_CONTAINERS * TAM_CONTAINER + TAM_OVERFLOW

def f_hash(QTDE_CONTAINERS,OP,TAM_CONTAINER,ELEMENTOS_INSERIDOS, TAM_OVERFLOW):
    cont = 0
    add = 0 
    qtd = []
    tabela = [None] * TAM_TOTAL
    while len(OP) != TAM_TOTAL:
        # Condição para chamar a busca, caso não encontre o valor a ser inserido
        if OP[cont] != ELEMENTOS_INSERIDOS[cont]:
            # Busca do  elemento na tabela 
            if OP[cont] == ELEMENTOS_BUSCA[cont]:
                add +=1
                for i in tabela:
                    if tabela[i]== ELEMENTOS_BUSCA[cont]:
                        print(tabela[i])
            #Condição se não encontrar na busca 
            else: 
                add += 1
        # Condição para inserir o valor no conteiner, caso encontre o valor a ser inserido é feito o calculo da hash
        else:
            chave = OP[cont]
            hash = chave % QTDE_CONTAINERS
            container = hash * TAM_CONTAINER + TAM_OVERFLOW
            tabela[container]= chave
            add += 1
        qtd.append(add)
    cont += 1
    return(qtd)
print(f_hash(QTDE_CONTAINERS,OP,TAM_CONTAINER,ELEMENTOS_INSERIDOS, TAM_OVERFLOW))
resultado = []
while OP != []:
    remove = OP.pop(0)
    resultado.append(f_hash(QTDE_CONTAINERS,remove,TAM_CONTAINER,ELEMENTOS_INSERIDOS, TAM_OVERFLOW))      
    entrega = ' '.join(str(e) for e in resultado)
    if OP == []:
        break