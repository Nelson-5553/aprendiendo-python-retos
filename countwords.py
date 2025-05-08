def countwords(oracion):
    contador = {}
    palabras = oracion.split()
    
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    
    return contador

palabra = "hola mundo a todos hola todos"
resultado = countwords(palabra)
print(resultado)
