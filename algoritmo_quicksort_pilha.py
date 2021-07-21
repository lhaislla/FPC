# Algoritimo da 3VA
from random import randint
class Pilha:

    def __init__(self):
        self.pilha= []
    def vazia(self):
        return self.pilha == []
    def topo(self):
        return self.pilha[len(self.pilha) - 1]
    def push(self,x):
        self.pilha.append(x)
    def pop_pilha(self):
        return self.pilha.pop()
    def pilha_nao_vazia (self):
        if self.pilha == []:
            return False
        else:
            return True

class Algoritmos:
    #lista = []
    def __init__ (self):
        self.pilha = Pilha()

    def __repr__(self): 
        return "%s" % (self.lista)
    
    def get_nome(self): 
        return self.lista

    def dividir(self,arr,l,h):
        i = ( l - 1 )
        x = arr[h]
        for j in range(l , h):
            if arr[j] <= x:
                i = i+1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[h] = arr[h],arr[i+1]
        return (i+1)

    def quicksortPilha(self,lista,l = 0,h = 0):
        self.pilha.push(l)
        self.pilha.push(h)
        while self.pilha.pilha_nao_vazia():
            h = self.pilha.pop_pilha()
            l = self.pilha.pop_pilha()

            p = self.dividir( lista, l, h )

            if p-1 > l:
                self.pilha.push(l)
                self.pilha.push( p - 1 )
            if p+1 < h:
                self.pilha.push( p + 1 )
                self.pilha.push( h )
                
    def ordemCrescente(self,arr, n = 0, t = True):#refatorar
        for i in range(len(arr)-1):
            x = arr[n]
            y = arr[n+1]
            if y >= x :
                n += 1
            else:
                t = False
        return t
        
        
def Principal():
    lista = []
    algoritmos = Algoritmos()
    lista_desordenada = []
    lista_ordenada = []
    while len(lista) != 1000:
        for i in range(0,1000):
            lista.append(randint(1,5000))
        lista_desordenada = lista
        
        lista_ordenada = lista    
    
    print(lista_desordenada)
    print('***************************************************************************************')
    algoritmos.quicksortPilha(lista_ordenada,0 ,len(lista_ordenada)-1)
    print(lista_ordenada)
    
    if algoritmos.ordemCrescente(lista_ordenada) == True :
        resposta = "lista ordenada"
        print(resposta)
    else:
        resposta = "lista desordenada"
        print(resposta)
    return(lista)

Principal()
