n = int(input(""))

def palavras_fib(n):
    if n <= 0:
        return 'b'
    elif n == 1:
        return 'a'
    else:
     
        return  palavras_fib(n-1) + palavras_fib(n-2)

print (palavras_fib(n))


    
