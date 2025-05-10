def add(a, b):
    return a +b
    
def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divide(a, b):
    return a / b


def calculator():
    while True:
        print("Ingrese una opcion")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        option = input("Ingresa su opcion (1, 2, 3, 4, 5): ")

        if option == 5:
            print("Saliendo ...")
            break
        
        if option in ["1","2","3","4"]:
            num1=float(input("Ingresa el primer numero: "))
            num2=float(input("Ingresa el segundo numero: "))

            if option == "1":
                print("La suma:", add(num1, num2))
            elif option == "2":
                print("La resta:", subtract(num1, num2))
            elif option == "3":
                print("La Multiplicacion:", multiplication(num1, num2))
            elif option == "4":
                print("La Division:", divide(num1, num2))
        
        else:
            print("Ingrese una opcion valida, porfavor intenta de nuevo")

calculator()