import csv

#Leer archivo
# with open ('./document/products.csv', 'r') as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row)

with open ('./document/products.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row["name"]}\nPrecio: {row["price"]}\n\n")