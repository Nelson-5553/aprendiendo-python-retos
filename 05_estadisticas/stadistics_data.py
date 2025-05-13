import csv
import statistics

monthly_sales = {}
with open('./document/monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
# print(sales)

#Sacar la media de ventas

mean_sales = statistics.mean(sales)
print(f"la media de las ventas mensuales es {mean_sales}")

#mediana
median_sales = statistics.median(sales)
print(f"la mediana de las ventas mensuales es {median_sales }")

#Moda
mode_sales = statistics.mode(sales)
print(f"la moda de las ventas mensuales es {mode_sales}")

#Desviacion estandar

stdev_sales = statistics.stdev(sales)
print(f"la Desviacion estandar de las ventas mensuales es {stdev_sales}")

#Hallar varianza
stdev_sales = statistics.variance(sales)
print(f"la varianza estandar de las ventas mensuales es {stdev_sales}")

# Mayor venta
max_sale = max(sales)

# Menor venta
min_sale = min(sales)

range_sale = max_sale - min_sale

print(f"El rango de ventas es {range_sale}")