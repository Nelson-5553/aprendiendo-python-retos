class Pet:
    registro = [] 

    def __init__(self, name: str, animal_type: str, age: int):
        self.name = name
        self.animal_type = animal_type.lower()
        self.age = age
        Pet.registro.append(self)

    def show_info(self):
        print (f"Hola me llamo {self.name} y soy un {self.animal_type} ya tengo {self.age} de edad")
    
    def make_sound(self):
        if self.animal_type == "perro":
            print ("¡Guau!")

        elif self.animal_type == "gato":
            print ("Miau!")

        else: 
            print ("¡Sonido desconocido!")

    @classmethod
    def show_all_pets(cls):
        for mascota in cls.registro:
            mascota.show_info()
            mascota.make_sound()
            print("---")
        
        
while True:
    name = input("Escribe el nombre de tu mascota: ")
    tipo = input("¿Es un perro, un gato u otro?: ")
    edad = input("¿Cuántos años tiene?: ")

    Pet(name, tipo, edad)

    cont = input("¿Quieres agregar otra mascota? (s/n): ").lower()
    if cont != 's':
        break

print("\n--- Lista de mascotas registradas ---")
Pet.show_all_pets()









    