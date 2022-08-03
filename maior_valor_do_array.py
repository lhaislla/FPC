'''
Pergunta 2
Você tem um arranjo(chamado myArray) com 5 elementos(inteiros de 1 a 100).
 Escreva um programa usando Python(clique no botão "i" no
  canto superior direito para ver a sintaxe) que imprima 
  o maior número do arranjo(se repetido, imprima apenas uma vez).

O código que prepara o arranjo já está escrito, mas 
se você preferir pode editá-lo para tentar outros valores.
 Ao clicar no botão de recarregar você pode retornar ao valor
  original o qual será usado para avaliar a questão como correta 
  ou incorreta durante a execução do programa.

IMPORTANTE: Imprima apenas o maior número como saída
 e nenhum outro texto. Por exemplo, 
 para o arranjo indicado, a saída deverá ser: 35
'''

myArray = [13,2,4,35,1]

#Outra forma:

'''def maior_arranjo(myArray):
   maior = 0
   for c in range(0, len(myArray)):
    if c == 0:
        maior = myArray[c]
    else:
        if myArray[c] > maior :
            maior = myArray[c]
            return maior
   

print(maior_arranjo(myArray))'''

#Outra forma:

'''def maior_valor(myArray ):
    try:
        if len(myArray ) == 0:
            return None

        maior = myArray [0]

        for valor in myArray :
            if valor > maior:
                maior = valor

        return maior
    except TypeError:
        return myArray 

print(maior_valor(myArray))'''

#Outra forma:
def verificaMaior(myArray):
  max_trip = myArray[0]
  for val in myArray:
    if max_trip < val :
      max_trip = int(val)
  return max_trip

print(verificaMaior(myArray))