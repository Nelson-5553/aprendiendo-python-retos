
# Condiciones basicas

x = 1 
if x > 5:
    print("x es mayor que 5\n")
elif x == 5:
    print("X es igual que 5\n")
else:
    print("X es menor que 5\n")

print("afuera")

# Operadores logicos

z = 15
y = 10

if x > 10 and y > 25:
    print("Z es mayor que 10 y Y es mayor que 25")


if x > 10 or y > 25:
    print("Z es mayor que 10 o Y es mayor que 25")

if not x > 10:
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

