# Definimos una función que calcula el área de diferentes polígonos

def areas (poligono, base=None, Altura=None , lado=None):
    if poligono == "Triangulo":
         area = (base * Altura) / 2
         return area
    elif poligono == "Cuadrado":
         area = lado * lado
         return area
    elif poligono == "Rectangulo":
         area = base * Altura
         return area
         


print("El área es:", areas("Triangulo", base=5, Altura=10))
print("El área es:", areas("Cuadrado", lado=5))
print("El área es:", areas("Rectangulo", base=5, Altura=10))