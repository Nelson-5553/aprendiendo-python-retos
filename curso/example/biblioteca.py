class Book:

    def __init__ (self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def barrow(self):
        if self.available:
            self.available = False
            print(f"el libro {self.title} a sido prestado")
        else:
            print(f"El libro {self.title} ya se encuentra prestado")
    
    def return_book(self):
         self.available = True
         print(f"El libro {self.title} a sido devuelto")

class User:
    def __init__ (self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
    
    def barrow_book(self, book):
        if book.available:
            book.barrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.title}")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {self.title} no se encuentra en la lista de prestados")
    
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro {book.title} a sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} a sido registrado")
    
    def show_available_books(self):
        print("Los libros disponibles son: \n")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")

# Objetos de la clase libros

book1 = Book("1984", "George Orwell")
book2 = Book("Cien años de soledad", "Gabriel García Márquez")
book3 = Book("Don Quijote de la Mancha", "Miguel de Cervantes")
book4 = Book("To Kill a Mockingbird", "Harper Lee")
book5 = Book("El Principito", "Antoine de Saint-Exupéry")

# Objetos de la clase user

user1 = User("Ana", 101)
user2 = User("Luis", 102)
user3 = User("Carla", 103)
user4 = User("Miguel", 104)
user5 = User("Sofía", 105)

# Creamos biblioteca

library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

#Registramos usuarios

library.register_user(user1)
library.register_user(user2)
library.register_user(user3)

#Motrar libros disponible

library.show_available_books()

# realizar prestamo

user1.barrow_book(book1)

#Motrar libros disponible

library.show_available_books()

#Devolver libro

user1.return_book(book1)
