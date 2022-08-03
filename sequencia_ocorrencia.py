'''
Pergunta 4
Você possui um arranjo(chamado myArray) com 10 elementos(inteiros de 1 a 9). 
Escreva um programa em Python que imprima o número o qual 
tenha mais ocorrências em sequência no arranjo e também imprima 
o número de vezes que ele apareceu.

O código que gera o arranjo já está escrito, mas você pode editá-lo 
para tentar outros valores. Ao clicar no botão de recarregar você pode 
retornar ao valor original o qual será usado para avaliar a questão como 
correta ou incorreta durante a execução do programa.

Seu programa deverá analisar o arranjo da esquerda para direita de 
maneira que se dois números atenderem as condições descritas, apenas a
 primeira ocorrência(à esquerda) seja considerada. A saída para o arranjo
  deste exemplo (1,2,2,5,4,6,7,8,8,8) seria:
Longest: 3
Number: 8

No exemplo, a maior sequência é o número 8 aparecendo 3 vezes seguidas. 
Observe que o código devera imprimir exatamente como descrito para que assim a
 questão seja considerada válida.'''


myArray = [1,2,2,4,5,6,7,8,8,8] 

'''def ocorrencia(myArray):
    Longest = 0
    Number = 0
    for i in myArray:
        if myArray[i] == myArray[i+1]:
            Number = myArray[i+1]
            Longest += 1
 
        else:
            myArray[i+1]
            Longest = 0
    print(f'Longest: {Longest}' , f'Number: {Number}')
ocorrencia(myArray)'''

def conta_ocorrencias(myArray ):
    ocorrencias = {}
    for c in myArray :
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    
    for Number, Longest in ocorrencias.items():
       pass
    print(f"Longest: {Longest}")
    print(f"Number: {Number} ")

   
conta_ocorrencias(myArray)