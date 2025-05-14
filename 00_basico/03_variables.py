"""
*******************************************************************
*                                                                 *
*           ¡Bienvenido al mundo de las variables!                *
*   En esta sección aprenderás qué son las variables y cómo se    *
*   utilizan en Python para almacenar datos como texto, números,  *
*                  y muchos otros tipos de información.           *
*                                                                 *
*   ¡Vamos a comenzar desarrollando juntos tus habilidades en     *
*            programación desde lo más básico con Python!         *
*                                                                 *
*******************************************************************
"""

# Cadena de texto (string)
nombre = "Pepe"

# Entero (int)
edad = 21

# Booleano (bool)
booleano = True  # o False

# Número decimal (float)
flotante = 2.4

# Lista (list)
lista = [1, 2, 3, "cuatro"]

# Tupla (tuple)
tupla = (10, 20, 30)

# Diccionario (dict)
diccionario = {"nombre": "Pepe", "edad": 21}

# Conjunto (set)
conjunto = {1, 2, 3, 4}

# Ningún valor / vacío (NoneType)
nulo = None

# Bytes
datos_bytes = b"Hola"

# Complex (número complejo)
complejo = 3 + 4j

# # puedes usar print para mostrar el valor de las variables.
print(nombre)
print(edad)

#concatenacion con comas
print ("Soy", nombre, "y tengo", edad, "años de edad" )

# #concatenacion con operador par
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

# # Las f-strings permiten insertar expresiones dentro de cadenas de texto.
print (f"soy {nombre} y tengo\n {edad} años de edad" )


# # El parámetro sep permite especificar cómo separar los elementos al imprimir.
print("Nunca", "pares", "de", "aprender", sep=", ")

# # El parámetro end cambia lo que se imprime al final de la llamada a print. 
print("Nunca", end=" ")
print("pares de aprender")