class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
         print(f"Hola mi nobre es {self.name} y tengo {self.age} años")

person1 = Person("Ana", 12)
person2  = Person("Luis", 30)

person1.greet()
person2.greet()

