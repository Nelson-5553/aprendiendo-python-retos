nombre = "Nelson Jimenez"
edad = 21
saludo = "Hola"

print(nombre)
print(edad)
print(saludo)

# uedes usar print para mostrar el valor de las variables.
print (saludo, "Soy", nombre, "y tengo", edad, "años de edad" )

# Las f-strings permiten insertar expresiones dentro de cadenas de texto.
print (f"{saludo} soy {nombre} y tengo\n {edad} años de edad" )

#concatenacion
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")

# El parámetro sep permite especificar cómo separar los elementos al imprimir.
print("Nunca", "pares", "de", "aprender", sep=", ")

# El parámetro end cambia lo que se imprime al final de la llamada a print. 
print("Nunca", end=" ")
print("pares de aprender")