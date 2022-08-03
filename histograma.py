'''Escreva um código usando Python para criar um histograma(um gráfico para representar o
 número de ocorrências de cada número no arranjo). O arranjo se chama myArray poderá 
 possuir números de 1 a 5 e terá 10 elementos. O histograma deverá mostrar todos os 
 números de 1 a 5, mesmo que não existam no arranjo. Por exemplo, para o arranjo: myArray, 
 o resultado deveria ser exatamente:

1: *****
2: **
3: **
4:
5: *

O código que gera o arranjo já está escrito,
 mas você pode editá-lo para tentar outros valores. Ao 
 clicar no botão de recarregar você pode retornar ao valor original
  o qual será usado para validar seu código durante a execução do programa.
   Observe que o código devera imprimir exatamente como descrito para ser 
   considerado válido(repare nos espaços entre o ":" e o primeiro "*").'''

myArray = [1,2,1,3,3,1,2,1,5,1]

def histograma(myArray):
    ocorrencias = {}
    for c in myArray : # verifica as recorrencias 
        for i in range(1,5): # define o valor dos números
            if i not in ocorrencias.keys():
                key, value = i, 0
                ocorrencias.update({key: value})
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    for chave, valor  in ocorrencias.items(): #Faz a multiplicação de * e adiciona o separador
       resultado = (chave, valor * '*')
       print(*resultado, sep= ': ')
       
histograma(myArray)