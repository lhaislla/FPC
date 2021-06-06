class Pilha(object):
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return len(self.items) == 0

  def push(self,exp):
    self.items.append(exp)

  def pop(self):
    self.items.pop()

  def peek(self):
    return self.items[-1]

  def size(self):
    return len(self.items)

def bem_formada(exp):
  pilha = Pilha()
  cont = 0
  while cont != len(exp):
    if exp[cont] == ')':
      if pilha.isEmpty() == False and (pilha.peek()) == '(':
        pilha.pop() 
      else:
        pilha.push(exp[cont])
        break
    elif exp[cont] == ']':
      if pilha.isEmpty() == False and (pilha.peek()) == '[':
        pilha.pop()
      else:
        pilha.push(exp[cont])
        break
    elif exp[cont] == '}':
      if pilha.isEmpty() == False and (pilha.peek())== '{':
        pilha.pop()
      else:
        pilha.push(exp[cont])
        break
    elif exp[cont] == "(" or exp[cont] == "[" or exp[cont] == "{":
        #Erro ao pegar as expressões 
        pilha.push(exp[cont])
    cont += 1
  return(pilha.isEmpty())

def verifica(bem_formada):
  if bem_formada == True:
    print('casamento perfeito')
  else: 
    print('casamento imperfeito')


exp= str(input(""))
bem_formada(exp)
verifica(bem_formada(exp))
