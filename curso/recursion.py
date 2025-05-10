#Calcular factorial usando recuursion
def factorial(numero):
        if numero == 0:
            return 1
        else:
            result = numero * factorial(numero-1)
            return result

# numero = int(input("Ingresa el numero a resolver: "))
#print(factorial(numero))

#fibonacci

def fibonacci(numero1):
    if numero1 == 0:
        return 0
    elif numero1 == 1:
        return 1
    else:
        result1 = fibonacci(numero1 - 1) + fibonacci(numero1 - 2)
        return result1

#numero1 = int(input("Ingresa el número a resolver: "))
#print(fibonacci(numero1))

#fibonacci

def natural(numero1):
    if numero1 == 0:
        return 0
    elif numero1 == 1:
        return 1
    else:
        result1 = numero1 + natural(numero1 - 1)
        return  result1

numero2 = int(input("Ingresa el número a resolver: "))
print(natural(numero2))