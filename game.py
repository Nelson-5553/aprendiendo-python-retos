import random as r

my_list = ["tijera", "papel", "piedra"]


def game(choice, ramdom):
    if choice == ramdom:
        return "el juego a empatado", choice, "y tu oponente", ramdom
    elif choice == "papel" and ramdom == "piedra":
        return "ganaste elegiste", choice, "y tu oponente", ramdom
    elif choice == "piedra" and ramdom == "papel":
        return "perdiste elegiste", choice, "y tu oponente", ramdom
    elif choice == "tijera" and ramdom == "papel":
        return "ganaste elegiste", choice, "y tu oponente", ramdom
    elif choice == "papel" and ramdom == "tijera":
        return "perdiste elegiste", choice, "y tu oponente", ramdom
    elif choice == "piedra" and ramdom == "tijera":
        return "ganaste elegiste", choice, "y tu oponente", ramdom
    elif choice == "tijera" and ramdom == "piedra":
        return "perdiste elegiste", choice, "y tu oponente", ramdom
    
random = r.choice(my_list)
choice = "piedra"

print(game(choice, random))