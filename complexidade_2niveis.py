entrada = input().split()
total = 0
nivel1 = 0
nivel2 = 0
nivel3 = 0
nivel4 = 0


n = 0

for i in range(len(entrada)):
    op = entrada[i]
    if entrada[i] == 'LOOP':
        n+=1
        if n == 2:
            nivel3 += nivel2 
            if nivel4 == 0:
                nivel4 = nivel1
            nivel2 = 0
            nivel1 = 0

        if nivel2 > 0:
            total += nivel2
            nivel2 = 0

        if entrada[i+1].isnumeric() == True:
            nivel1 = int(entrada[i+1])

    elif entrada[i] == 'OP':
        if entrada[i+1].isnumeric() == True:
            nivel2 += int(entrada[i+1])

    elif entrada[i] == 'FIMLOOP':
        n -= 1
        if n == 0 and nivel4 == 0:
            total += nivel1 * nivel2
            nivel1 = 0
            nivel2 = 0
        elif n == 0 and nivel3 > 0 and nivel4 > 0:
            temp = nivel2 + nivel3
            total += temp * nivel4
            nivel1 = 0
            nivel2 = 0
            nivel3 = 0
            nivel4 = 0
        if n > 0 and nivel3 > 0:
            temp = nivel1 * nivel2
            nivel3 += temp
            nivel1 = 0
            nivel2 = 0

    elif entrada[i] == 'FIM' and nivel2 > 0:
        total += nivel2
        nivel2 = 0

print(total)
