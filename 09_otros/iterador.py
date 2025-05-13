# Crear una lista
lista = [1, 2, 3, 4]

# Obtener el iterador de la lista
iterador = iter(lista)

# Usar el iterador para obtener elementos
print(next(iterador))  # Imprime: 1
print(next(iterador))  # Imprime: 2
print(next(iterador))  # Imprime: 3
print(next(iterador))  # Imprime: 4
# print(next(iterador))  # Imprime: 5

# Crear una cadena
texto = "hola mundo"

# Obtener el iterador de la cadena
iterador_texto = iter(texto)

# Iterar a través de la cadena
for caracter in iterador_texto:
    print(caracter)

limite = 10
# Crear un iterador para números pares hasta 10 # range(start, stop, step)
iterador_pares = iter(range(0, limite + 1, 2))

# Iterar a través de los números pares
for numero in iterador_pares:
    print(numero)

def mi_generador():
    yield 1
    yield 2
    yield 3

# Usar el generador
for valor in mi_generador():
    print(valor)