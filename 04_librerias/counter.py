from collections import Counter

def contar_ventas(productos):
    return Counter(productos)

productos = ['laptop', 'smartphone', 'smartphone', 'laptop', 'tablet']
resultado = contar_ventas(productos)
print(resultado)  # Output: Counter({'laptop': 2, 'smartphone': 2, 'tablet': 1})