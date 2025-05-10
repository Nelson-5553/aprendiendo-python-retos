list = [x ** 3 for x in range(1, 11)]
print("los cuadrados son: ", list)

celsius = [0, 10, 20, 30, 40]
fahrenheint = [(temp * 9/5) * 32 for temp in celsius]
# print("la conversion es ", fahrenheint)

# numeros pares
evens = [x for x in range(1, 21) if x % 2 == 0]
# print(evens)

matrix =[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],    
    ]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
print(transposed )
