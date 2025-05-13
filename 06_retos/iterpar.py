limite = 10

iterador_pares = iter(range(0, limite + 1, 2))

iterador_impares = iter(range(1, limite + 1, 2))

for numero in iterador_pares:
    print(numero)

for numero in iterador_impares:
    print(numero)


