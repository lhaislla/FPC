class Node():
    """ Classe que define um nodo simples de uma Estrutura de dados: (info, NextNodo)"""
    def __init__(self, data, nextNode=None):
        """Construtor do Nodo"""
        self.data = data
        self.nextNode = nextNode

    def __str__(self):
        return str(self.data)
    
    def getData(self):
        "Retorna o Dado armazenado no nodo"
        return self.data
    
    def setData(self, data):
        "Atribui valor ao Dado do nodo"
        self.data = data

    def getNextNode(self):
        "Retorna a referencia do proximo nodo"
        return self.nextNode

    def setNextNode(self, data):
        "Ajusta a referencia do proximo nodo"
        self.nextNode = data
class Lista():
    def get_inicio(self):
        return self.__inicio

    def get_fim(self):
        return self.__fim

    def set_inicio(self, data):
        self.__inicio = data
        
    def set_fim(self, data):
        self.__fim = data

    def __init__(self): 
        "Construtor da Lista"
        self.__inicio = None
        self.__fim = None

    def __str__(self):
        "Override do Estatuto STRING"
        if self.lista_esta_vazia():
            return ''
        node_atual = self.__inicio
        string = ''
        while node_atual is not None:
            string += str(node_atual.getData())
            node_atual = node_atual.getNextNode()
        return string

    def lista_esta_vazia(self):
        return self.__inicio is None

    def inserir_no_inicio(self, data):
        "Insere elemento no Inicio da lista"
        novo_node = Node(data) # instancia de um novo nodo
        if self.lista_esta_vazia(): #Insersao para Lista vazia
            self.__inicio = self.__fim = novo_node
        else: #Insersao para lista nao vazia
            novo_node.setNextNode(self.__inicio)
            self.__inicio = novo_node

    def inserir_no_fim(self, data):
        novo_node = Node(data)  #instancia de um novo nodo
        if self.lista_esta_vazia(): #Se a lista esta vazia
            self.__inicio = self.__fim = novo_node
        else:
            self.__fim.setNextNode(novo_node)
            self.__fim = novo_node
    
    
    def remove_do_inicio(self):
        "Remove o nodo inicial da lista"
        if self.lista_esta_vazia():
            return 'Remocao de Lista vazia nao permitida'
        valor_primeiro_node = self.__inicio.getData()
        if self.__inicio is self.__fim:
            self.__inicio = self.__fim = None
        else:
            self.__inicio = self.__inicio.getNextNode()
        return valor_primeiro_node

    def remove_do_fim(self):
        "Remove o ultimo nodo da lista"
        if self.lista_esta_vazia():
            return 'Remocao de Lista vazia nao permitida'
        valor_ultimo_node = self.__fim.getData()
        if self.__inicio is self.__fim:
            self.__inicio = self.__fim = None
        else:
            node_atual = self.__inicio
            while node_atual is not self.__fim:
                node_atual = node_atual.getNextNode()
            node_atual.setNextNode(None)
            self.__fim = node_atual
        return valor_ultimo_node
class Fila(Lista):

    def colocar_na_fila(self, data):
        self.inserir_no_fim(data)
   
    def tirar_da_fila(self):
        return self.remove_do_inicio()
class Pilha(Lista):
    
    def colocar_na_pilha(self, data):
        self.inserir_no_inicio(data)
    
    def tirar_da_pilha(self):
        return self.remove_do_inicio()