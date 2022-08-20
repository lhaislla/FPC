'''URI- 1035

    Leia 4 valores inteiros A, B, C e D. A seguir, 
    se B for maior do que C 
    e se D for maior do que A,
    e a soma de C com D for 
    maior que a soma de A e B 
    e se C e D, ambos, 
    forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", 
    senão escrever "Valores nao aceitos".

Entrada
    Quatro números inteiros A, B, C e D.

Saída
    Mostre a respectiva mensagem após a validação dos valores.

Caso de teste: 
    entrada: 5 6 7 8  saida: Valores nao aceitos

    entrada: 2 3 2 6 saida: Valores aceitos
'''
x = input().split()

'''def teste_selecao():
    entrada = []
    for i in range(0,4):
        num = int(input("Digite o valor: "))
        entrada.append(num)
    print(entrada)
    A = entrada[0]
    B = entrada[1]
    C = entrada[2]
    D = entrada[3]
    print(A, B, C, D)
    if (B > C) and (D > A ) and (C + D) > (A + B) and (C > 0 and  D > 0) and (A % 2  == 0):
        print("Valores aceitos")
    else:
        print("Valores  não aceitos")'''
def teste_selecao(x):
    a, b, c, d = x
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')

if __name__ == "__main__":
    teste_selecao(x)