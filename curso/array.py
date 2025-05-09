# Array de strings
to_do = ["Comer", "Dormir", "Bañarme", "Jugar"]
print("Lista de tareas:", to_do)

# Array de números
numbers = [1, 2, 3, 4, 5]
print("Números en la lista:", numbers)

# Indexación en lista con datos mixtos
mixtos = ["uno", 32, 3.14, True, [1, 3, 4]]
print("Longitud de la lista 'mixtos':", len(mixtos))
print("Elemento en la posición 1 de la sublista:", mixtos[4][1])

# Slicing de cadenas
string = "Hola mundo"
print("Primeros dos caracteres:", string[0:2])

# Agregar datos a un array
my_list = ["tijera", "papel", "piedra"]
my_list.append("pistola")
print("Lista después de agregar 'pistola':", my_list)

my_list.append([1, 3])
print("Lista después de agregar [1, 3] al final:", my_list)

# Insertar elemento en posición específica
my_list.insert(1, [1, 3])
print("Lista después de insertar [1, 3] en la posición 1:", my_list)

# Obtener el índice de un elemento
print("Índice de la primera aparición de [1, 3]:", my_list.index([1, 3]))

# Obtener el valor máximo y mínimo
numerosAleatorios = [73, 5, 91, 42, 67, 28, 19, 86, 13, 60]
print("Número mayor:", max(numerosAleatorios))
print("Número menor:", min(numerosAleatorios))

# eliminar datos
del numerosAleatorios[1:3]
print("Número mayor:", max(numerosAleatorios))
print("Número menor:", min(numerosAleatorios))


# Copiar listas

a = [1, 2, 3, 4, 5]
b = a

print(a)
print(b)

del a[1]

print(a)
print(b)

#ESPACIO EN MEMORAA
print(id(a))
print(id(b))

# slicing
c = a[:]
print(id(a))
print(id(b))
print(id(c))

a.append(3)

print(a)
print(b)
print(c)
