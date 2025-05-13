import random

# Generar un numero entero aleatorio

# for i in range(10):
    # random_number = random.randint(1, 100)
    # print(random_number)

# randomizar palabras
list =["Agua", "Tiera", "Aire", "Viento"]
random_words = random.choice(list)
print(random_words)

cards = ["As", "Reina", "Rey", "Jota", "10" ]
random.shuffle(cards)
print(cards)
