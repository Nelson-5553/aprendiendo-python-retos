# sin funciones de python
with open('./document/cuento.txt', 'r') as file:
     conteo = 0
     for line in file:
        if line.strip():
            conteo += 1
            print(f"{conteo}: {line.strip()}")

# con funciones de python
with open ('./document/cuento.txt', 'r') as file:
    lineas = file.readlines()
    print(len(lineas))
