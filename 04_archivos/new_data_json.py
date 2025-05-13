import json

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2024-07-01'
}

with open ("./document/products.json", mode="r") as file:
    products = json.load(file)
    products.append(new_product)

    with open ("./document/products.json", mode="w") as file:
        json.dump(products, file, indent=4)
    
