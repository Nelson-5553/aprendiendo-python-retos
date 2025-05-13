player1 = input("Elige Piedra, Papel o Tijera jugador 1: ")
player2 = input("Elige Piedra, Papel o Tijera jugador 2: ")

rules = {
    "Tijera":"Papel",
    "Papel":"Piedra",
    "Piedra":"Tijera"
}
if player1 not in rules or player2 not in rules:
    print("entrada no valida")
else:
    if player1 == player2:
        print("Empate")
    elif rules[player1] == player2:
        print (f"jugador 1 gano usando {player1} y jugador 2 perdio con {player2}")
    else:
        print (f"jugador 2 gano usando {player2} y jugador 1 perdio con {player1}")
