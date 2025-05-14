"""
En python podemos crear condiciones 

¿que son las condiciones?

es una estructura de control que permite tomar decisiones en el flujo de un programa 
según una condición booleana (True o False). Los condicionales comunes 
incluyen if, else if, else. 

"""

# Condiciones basicas

x = 1 


# Si x es mayor que 5 
if x > 5:
    print("x es mayor que 5\n")
# si x es igual que 5
elif x == 5:
    print("X es igual que 5\n")
# si no se produce nisguno de los anteriores dados se asume que es menor
else:
    print("X es menor que 5\n")


# Operadores logicos
# Este tema no se toco tanto en la seccion de operadores pero aqui te tengo un buen ejemplo que te puede servir

z = 15
y = 10

# Si Z es mayor que 10  Y y es mayor que 25
if z > 10 and y > 25:
    print("Z es mayor que 10 y Y es mayor que 25")

# Si Z es mayor que 10 o y es mayor que 25
if z > 10 or y > 25:
    print("Z es mayor que 10 o Y es mayor que 25")

# Si Z no es mayor que 10
if not z > 10:
    print ("Z no es mayor que 10")

# Codiciones anidadas

is_member = False
age = 15

if is_member:
    if age >= 15:
        print("Tienes acceso ya que eres miembro y mayor de 15")
    else:
        print("Tienes acceso pero es menor de 15")
else:
    print("No eres mienbro")

# Te invito aque  sigas probando mas condiciones es mas te dejare un reto que te gustara

