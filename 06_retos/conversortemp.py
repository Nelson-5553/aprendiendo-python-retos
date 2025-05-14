"""
/*
 * Crea una función que transforme grados Celsius en Fahrenheit
 * y viceversa.
 *
 * - Para que un dato de entrada sea correcto debe poseer un símbolo "°"
 *   y su unidad ("C" o "F").
 * - En caso contrario retornará un error.
 */
"""

def conversor(conversion ,valor):
    if conversion == 3:
        print("Saliendo...")
        return  
    
    if conversion == 1:
        result = (valor * 9/5) + 32
        print (f"El resultado de grados celsius a faranheit es: {result}")
    elif conversion == 2:
        result = (valor - 32) * 5/9 
        print (f"El resultado de grados faranheit a celsius es: {result}")
    else:
        print("no ha introducido una opcion valida")

print("Conversor de grados farenheit y celsius: \n")
print("1. Celsius a Farenheit")
print("2. Farenheit a Celsius")
print("3. Salir")

opcion = int(input("Elige una opcion: "))
if opcion != 3:
    valor = int(input("Coloca un valor: "))
else:
    valor = 0
conversor(opcion ,valor)
    
