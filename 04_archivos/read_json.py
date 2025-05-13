import json

with open ("./document/products.json", mode="r") as file:
    products = json.load(file)
    
    for product in products:
        # print(product)
        print(f"El  producto {product["name"]} con precio de {product["price"]}")