# Ciclo For
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print(f"i es igual a: {i}")

# Rangos
for i in range(10):
    print(i)  # Imprime del 0 al 9

for i in range(3, 10):
    print(i)  # Imprime del 3 al 9

# Iteraciones condicionadas

frutas = ["manzana", "pera", "uva", "naranja", "tomate"]
for fruta in frutas:
    if fruta == "naranja":
        print("naranja encontrada")
 
#  Ciclo While

x = 0
while x < 5:
    print(x)
    x += 1