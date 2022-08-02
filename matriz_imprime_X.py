#teste1
'''Escreva um programa em Python que imprima X usando a letra X e use underline como espaço.
 O tamanho do X é baseado na variável n a qual vai indicar o tamanho da letra a ser 
 impressa(em uma matrix n x n). Por exemplo, para n = 5 você terá:

X___X
_X_X_
__X__
_X_X_
X___X

e para n = 6:

X____X
_X__X_
__XX__
__XX__
_X__X_
X____X

Se n for igual a zero, imprima "ERROR".

O código para o tamanho de n está aí, você pode editá-lo 
para encontrar outros valores e pode, em seguida, clicar
 em recarregar para assim retornar ao valor original o
  qual será usado para validar seu código durante o teste. 
  Observe que o código devera imprimir exatamente como
   descrito para que assim a questão seja considerada 
   válida(o caractere "X" deve ser maiúsculo e underlines "_" para os espaços).'''

n = int(input('Digite o valor de n: '))

def cria_matriz(n):   
    
   
    if n == 0:
        print("ERROR")
    else:     
        mat = []
        for i in range(n): #Monstando a matriz
            linha = []
            for j in range (n):
                linha.append('_')
            mat.append(linha)
        
        
        DP = [] # Diagonal principal i=j
        DS = [] # Diagonal Secundaria i + j 

        for  i in range (n):
            for j in range (n):
                mat[i][j]
                if i == j: #DP 
                    mat[i][j] = 'X'
                    DP.append(mat[i][j])
                elif i + j == n - 1: # DS
                    mat[i][j] = 'X'
                    DS.append(mat[i][j])
        return mat   

def preenche(matriz):
    for linha in matriz:
        print(*linha, sep = '')

preenche(cria_matriz(n))