def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if n == a:
            return print(f'O número {n} pertence a sequência de Fibonacci.')
        a, b = b, a + b
    return print(f'O número {n} NÃO pertence a sequência de Fibonacci.')

num_terms = int(input("Insira um número: "))
fibonacci(num_terms)