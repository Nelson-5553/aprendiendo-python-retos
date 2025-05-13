# archivo linea por linea

# with open ('./document/cuento.txt', 'r') as file:
#     for line in file:
#         print(line.strip())


#Agregar a una lista

# with open ('./document/cuento.txt', 'r') as file:
#     lineas = file.readlines()
#     print(lineas)

# Añadir text
# with open ('./document/cuento.txt', 'a') as file:
#   file.write("\n\nBy:ChatGPT Nelson")

# Reescribir text
with open ('./document/cuento1.txt', 'w') as file:
  file.write("\n\nBy:ChatGPT Nelson")