def fibonacci(limite):
    a, b = 0, 1
    while a < limite:
        yield a
        a, b = b, a + b

# Usar el generador para la serie de Fibonacci hasta 10
for numero in fibonacci(20):
    print(numero)