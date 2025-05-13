
oracion = "¿Que te parece el reto?"

palabras = oracion.split()

longitud_maxima = max(len(palabra) for palabra in palabras)
    
print("*" * (longitud_maxima + 4))
for palabra in palabras:
    print(f"* {palabra.ljust(longitud_maxima)} *")
print("*" * (longitud_maxima + 4))


