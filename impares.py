'''
Leia um valor inteiro x. Em seguida apresente os 6 valores 
ímpares consecutivos a partir de x, um valor por linha, 
inclusive o x ser for o caso.

Entrada
    A entrada será um valor inteiro positivo.

Saída
    A saída será uma sequência de seis números ímpares.
    
Caso de teste:
    entrada:
        x = 8
    saida: 
        9 11 13 15 17 19
'''

x = int(input(" Digite um número: "))

'''def impar(x):
    cont = 0
    while cont < 12:
        if x % 2 != 0:
            print(x)
        cont += 1
        x += 1'''

def impar(x):
    impares = [n for n in range(x,x+12) if n % 2 != 0]
    for n in impares:
        print(n)
       

if __name__ == "__main__":
    impar(x)