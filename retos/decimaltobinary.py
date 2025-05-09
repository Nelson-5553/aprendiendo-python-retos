def binary(number):
    binario = []
    if not isinstance(number, int):
        return "ingresa un numero"
    else:
        while number > 0:
            residuo = number % 2
            binario.append(residuo)
            number = number // 2  # División entera
        binario.reverse()
        return ''.join(str(bit) for bit in binario)

# Pedir número por consola
numero_usuario = int(input("Escribe un número entero: "))
print(binary(numero_usuario))


# division = number / 2
# result = division % 2

# print(math.floor(division), ":", math.floor(result))