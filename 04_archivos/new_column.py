import csv

file_path = "./document/products.csv"
file_path_update = "./document/products_update.csv"

with open (file_path , mode="r") as file:
    csv_reader = csv.DictReader(file)
    #Otener nombres de columnas
    fieldnames = csv_reader.fieldnames + ['Total_value'] + ["Total_value_2"]

    with open (file_path_update, mode="w") as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader() # Escribir encabezados

        for row in csv_reader:
            row['Total_value'] = float(row['price']) * int(row['quantity'])
            row['Total_value_2'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)

      