
def suma(a, b):
    result = a + b
    return result

def resta(a, b):
    result = a - b
    return result

def division(a, b):
    if b == 0:
        raise ValueError("El divisor no puede sr igual a 0")
    result = a // b
    return result

def multplicacion(a, b):
    result = a * b
    return result

if __name__ == "__main__":
    print('Operacioenes')
    res_1 = suma(3,4)
    print(f"Suma {res_1}")
    print(division(10, 7))