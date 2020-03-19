class Pilha(object):
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return len(self.items) == 0

  def push(self,exp):
    self.items.append(exp)

  def pop(self):
    return self.items.pop(-1)

  def peek(self):
    return self.items[-1]

  def size(self):
    return len(self.items)
  def mostra(self):
    return self.items

entrada = input("Qual a sua função? ").upper().split()

def complexidade(funcao):
    pilha = Pilha()
    cont = 0
    valor = 0
    contador2 = 0
    while cont != len(funcao):
    
        contador2 = 0
        if funcao[cont] == 'FIM':
          while contador2 == 0:
            numero = pilha.pop()
            if numero.isnumeric() == True:
              operador = pilha.pop()
              if operador == 'OP':
                valor += int(numero)
              elif operador == 'LOOP':
                valor = valor * int(numero)
                contador2 += 1
            elif numero == 'INICIO':
              break      
        else:
            pilha.push(funcao[cont])
        cont += 1
  
    print(valor)

complexidade(entrada)
    
