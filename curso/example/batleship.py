
"""
, crearás un juego de Batalla Naval (Battleship) en Python, donde dos jugadores colocan sus barcos en un tablero y se turnan para atacar las posiciones del oponente hasta que uno de los jugadores hunda todos los barcos del otro. Sigue estos pasos detallados para construir el juego.
Paso 1: Define la Clase Ship
Paso 2: Define Clases Específicas de Barcos
Paso 3: Define la Clase
Paso 4: Define la Clase BattleshipGame
Paso 5: Ejecuta el Juego
"""

class Ship:
    def __init__(self, name, size):
        self.name = name           # Sin coma
        self.size = size           # Sin coma
        self.positions = []        # Lista vacía
        self.hits = 0              # Número entero

    def place_ship(self, board, start_row, start_col, direction):
        positions = []

        # Verificar si el barco cabe en la dirección dada
        for i in range(self.size):
            if direction == 'H':
                row, col = start_row, start_col + i
            elif direction == 'V':
                row, col = start_row + i, start_col
            else:
                return False  # Dirección inválida

            # Verificar que no se salga del tablero
            if row >= len(board) or col >= len(board[0]):
                return False

            # Verificar que la celda esté vacía
            if board[row][col] != ' ':
                return False

            positions.append((row, col))

        # Colocar el barco en el tablero
        for row, col in positions:
            board[row][col] = self.name[0]

        self.positions = positions
        return True
