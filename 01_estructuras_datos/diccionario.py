numbers = {1:"uno", 2:"dos", 3:"tres"}
print(numbers[2])

informacion = {"nombre": "Nelson",
               "apellido": "Jimenez",
               "altura": 1.70,
               "edad":21}

print(informacion)

del informacion["edad"]
print(informacion)

claves = informacion.keys()
print(claves)
print(type(claves))

values = informacion.values()
print(values)

item = informacion.items()
print(item)

contacto ={
           "Nelson": { "nombre": "Nelson",
               "apellido": "Jimenez",
               "altura": 1.70,
               "edad":21},
            "Naty": { "nombre": "Naty",
               "apellido": "Jimenez",
               "altura": 1.65,
               "edad":15},
        }

print(contacto["Naty"]["edad"])