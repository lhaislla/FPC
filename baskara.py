"""
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”,
caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
    Leia três valores de ponto flutuante (double) A, B e C.

Saída
    Se não houver possibilidade de calcular as raízes, apresente a mensagem 
    "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto,
    com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
    
Casos de Teste:
    Caso 1 :
        Entrada: 
            10.0 20.1 5.1
        Saída:
            R1 = -0.29788
            R2 = -1.71212 
    Caso 2:
        Entrada: 
            0.0 20.0 5.0
            
        Saída:
            Impossivel calcular       
    Caso 3:
        Entrada: 
            10.3 203.0 5.0
            
        Saída:
            R1 = -0.02466
            R2 = -19.68408 
    Caso 4:
        Entrada: 
            10.0 3.0 5.0
        Saída:
            Impossivel calcular
    
    
    """

v = input().split()

def baskara(v):
    a, b, c = v

    a = float(a)
    b = float(b)
    c = float(c)

    if a == 0.0  or (b ** 2 - 4 * a * c) < 0:
        print('Impossivel calcular')
    else:
        x1 = (- b + (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
        x2 = (- b - (b ** 2 - 4 * a * c) ** (1/2) )/(2 * a)
        print('R1 = {:.5f}'.format(x1))
        print('R2 = {:.5f}'.format(x2))


if __name__ == "__main__":
    baskara(v)