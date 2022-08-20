'''
Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

Entrada
    O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

Saída
    Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

Obs: Utilize ponto (.) para separar a parte decimal.

Caso de Teste:
    Caso 1:
        Entrada:
            576.73
        Saída:
            NOTAS:
            5 nota(s) de R$ 100.00
            1 nota(s) de R$ 50.00
            1 nota(s) de R$ 20.00
            0 nota(s) de R$ 10.00
            1 nota(s) de R$ 5.00
            0 nota(s) de R$ 2.00
            MOEDAS:
            1 moeda(s) de R$ 1.00
            1 moeda(s) de R$ 0.50
            0 moeda(s) de R$ 0.25
            2 moeda(s) de R$ 0.10
            0 moeda(s) de R$ 0.05
            3 moeda(s) de R$ 0.01
    Caso 2:
        Entrada:
            4.00
            
        Saída:
            NOTAS:
            0 nota(s) de R$ 100.00
            0 nota(s) de R$ 50.00
            0 nota(s) de R$ 20.00
            0 nota(s) de R$ 10.00
            0 nota(s) de R$ 5.00
            2 nota(s) de R$ 2.00
            MOEDAS:
            0 moeda(s) de R$ 1.00
            0 moeda(s) de R$ 0.50
            0 moeda(s) de R$ 0.25
            0 moeda(s) de R$ 0.10
            0 moeda(s) de R$ 0.05
            0 moeda(s) de R$ 0.01

    Caso 3:
        Entrada: 
            91.01
            
        Saída:
            NOTAS:
            0 nota(s) de R$ 100.00
            1 nota(s) de R$ 50.00
            2 nota(s) de R$ 20.00
            0 nota(s) de R$ 10.00
            0 nota(s) de R$ 5.00
            0 nota(s) de R$ 2.00
            MOEDAS:
            1 moeda(s) de R$ 1.00
            0 moeda(s) de R$ 0.50
            0 moeda(s) de R$ 0.25
            0 moeda(s) de R$ 0.10
            0 moeda(s) de R$ 0.05
            1 moeda(s) de R$ 0.01
'''


n = float(input())

def notas_moedas(n):
    n100 = n // 100
    n = n - n100*100

    n50 = n // 50
    n = n - n50*50

    n20 = n // 20
    n = n - n20*20

    n10 = n // 10
    n = n - n10*10

    n5 = n // 5
    n = n - n5*5

    n2 = n // 2
    n = n - n2*2

    n1 = n // 1
    n = n - n1*1
    n1=float('%.2f'% n1)
    n=float('%.2f'% n)

    m50 = n // 0.5
    n = n - m50*0.5
    m50=float('%.2f'% m50)
    n=float('%.2f'% n)

    m25 = n // 0.25
    n = n - m25*0.25
    m25=float('%.2f'% m25)
    n=float('%.2f'% n)

    m10 = n // 0.10
    n = n - m10*0.10
    m10=float('%.2f'% m10)
    n=float('%.2f'% n)

    m5 = n // 0.05
    n = n - m5*0.05
    m5=float('%.2f'% m5)
    n=float('%.2f'% n)

    m1 = n * 100
    m1=float('%.2f'% m1)
    n=float('%.2f'% n)

    print('NOTAS:')
    print('{} nota(s) de R$ 100.00'.format(int(n100)))
    print('{} nota(s) de R$ 50.00'.format(int(n50)))
    print('{} nota(s) de R$ 20.00'.format(int(n20)))
    print('{} nota(s) de R$ 10.00'.format(int(n10)))
    print('{} nota(s) de R$ 5.00'.format(int(n5)))
    print('{} nota(s) de R$ 2.00'.format(int(n2)))
    print('MOEDAS:')
    print('{} moeda(s) de R$ 1.00'.format(int(n1)))
    print('{} moeda(s) de R$ 0.50'.format(int(m50)))
    print('{} moeda(s) de R$ 0.25'.format(int(m25)))
    print('{} moeda(s) de R$ 0.10'.format(int(m10)))
    print('{} moeda(s) de R$ 0.05'.format(int(m5)))
    print('{} moeda(s) de R$ 0.01'.format(int(m1)))

if __name__ == "__main__":
    notas_moedas()